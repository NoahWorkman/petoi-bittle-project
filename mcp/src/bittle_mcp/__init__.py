"""
Bittle MCP Server - Control Petoi Bittle robot via Bluetooth from Claude Code.

This MCP server exposes tools to:
- Connect to Bittle via Bluetooth
- Send movement commands (walk, trot, crawl)
- Send pose commands (sit, rest, hello)
- Play sounds (bark melody)
- Query status
"""

import asyncio
import logging
import re
import sys
from contextlib import asynccontextmanager

from mcp.server.fastmcp import FastMCP

from .commands import COMMANDS, GAITS, DIRECTIONS
from .bluetooth import BittleConnection

# Configure logging to stderr (CRITICAL: never use stdout with stdio transport)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr
)
logger = logging.getLogger("bittle-mcp")

# Global connection instance
bittle: BittleConnection | None = None


@asynccontextmanager
async def app_lifespan(server: FastMCP):
    """Handle server startup and shutdown."""
    global bittle
    bittle = BittleConnection()
    logger.info("Bittle MCP Server started")

    try:
        yield {"bittle": bittle}
    finally:
        if bittle and bittle.is_connected:
            await bittle.disconnect()
        logger.info("Bittle MCP Server stopped")


# Initialize MCP server
mcp = FastMCP("bittle", lifespan=app_lifespan)


@mcp.tool()
async def scan(timeout: float = 10.0) -> str:
    """Scan for nearby Bittle devices over Bluetooth LE.

    Args:
        timeout: Scan duration in seconds (default 10)
    """
    if bittle is None:
        return "Error: Server not initialized"

    try:
        devices = await bittle.scan(timeout=timeout)
    except Exception as e:
        logger.error(f"Scan failed: {e}")
        return f"Scan failed: {e}"

    if not devices:
        return "No Bittle devices found. Make sure Bittle is powered on and not connected to another device."

    lines = [f"  {d['name']}: {d['address']}" for d in devices]
    return f"Found {len(devices)} device(s):\n" + "\n".join(lines)


@mcp.tool()
async def connect(address: str) -> str:
    """Connect to Bittle via Bluetooth.

    Args:
        address: Bluetooth MAC address of Bittle (e.g., "XX:XX:XX:XX:XX:XX")
    """
    if bittle is None:
        return "Error: Server not initialized"

    # Validate address format: standard MAC (XX:XX:XX:XX:XX:XX) or macOS UUID
    mac_re = re.compile(r"^([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}$")
    uuid_re = re.compile(
        r"^[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12}$"
    )
    if not mac_re.match(address) and not uuid_re.match(address):
        return (
            "Error: Invalid address format. "
            "Expected MAC (XX:XX:XX:XX:XX:XX) or macOS UUID."
        )

    try:
        await bittle.connect(address)
        return f"Connected to Bittle at {address}"
    except Exception as e:
        logger.error(f"Connection failed: {e}")
        return f"Connection failed: {e}"


@mcp.tool()
async def disconnect() -> str:
    """Disconnect from Bittle."""
    if bittle is None:
        return "Error: Server not initialized"

    if not bittle.is_connected:
        return "Not connected"

    await bittle.disconnect()
    return "Disconnected from Bittle"


@mcp.tool()
async def status() -> str:
    """Get connection status."""
    if bittle is None:
        return "Server not initialized"

    if bittle.is_connected:
        return f"Connected to {bittle.address}"
    return "Not connected"


@mcp.tool()
async def send(command: str) -> str:
    """Send a command to Bittle.

    Args:
        command: Command name (rest, sit, walk, trot, crawl, hello, bark, etc.)

    Available commands:
    - Movement: forward, backward, left, right
    - Gaits: walk, trot, crawl
    - Poses: sit, rest, stand, balance
    - Tricks: hello, pee, stretch, pushup
    - Sounds: bark (plays robot bark melody)
    """
    if bittle is None:
        return "Error: Server not initialized"

    if not bittle.is_connected:
        return "Error: Not connected to Bittle"

    # Only allow known commands — no raw passthrough
    cmd = COMMANDS.get(command.lower())
    if cmd is None:
        valid = ", ".join(sorted(COMMANDS.keys()))
        return f"Unknown command: {command}. Valid commands: {valid}"

    try:
        await bittle.send(cmd)
        return f"Sent: {command} ({cmd})"
    except Exception as e:
        logger.error(f"Send failed: {e}")
        return f"Send failed: {e}"


@mcp.tool()
async def move(direction: str, gait: str = "walk") -> str:
    """Move Bittle in a direction with specified gait.

    Args:
        direction: Movement direction (forward, backward, left, right)
        gait: Movement gait (walk, trot, crawl). Default: walk
    """
    if bittle is None:
        return "Error: Server not initialized"

    if not bittle.is_connected:
        return "Error: Not connected to Bittle"

    gait_cmd = GAITS.get(gait.lower())
    dir_cmd = DIRECTIONS.get(direction.lower())

    if not gait_cmd:
        return f"Unknown gait: {gait}. Use: walk, trot, crawl"

    if not dir_cmd:
        return f"Unknown direction: {direction}. Use: forward, backward, left, right"

    try:
        # Set gait then direction
        await bittle.send(gait_cmd)
        await bittle.send(dir_cmd)
        return f"Moving: {gait} {direction}"
    except Exception as e:
        logger.error(f"Move failed: {e}")
        return f"Move failed: {e}"


@mcp.tool()
async def play_sound(sound: str = "bark") -> str:
    """Play a sound on Bittle's buzzer.

    Args:
        sound: Sound name (bark) or raw melody string (e.g., "b20,16,0,16,18,16")
    """
    if bittle is None:
        return "Error: Server not initialized"

    if not bittle.is_connected:
        return "Error: Not connected to Bittle"

    # Predefined sounds
    sounds = {
        "bark": "b14,4,17,4,14,4,17,4,14,2",
    }

    cmd = sounds.get(sound.lower())
    if cmd is None:
        valid = ", ".join(sorted(sounds.keys()))
        return f"Unknown sound: {sound}. Valid sounds: {valid}"

    try:
        await bittle.send(cmd)
        return f"Playing: {sound}"
    except Exception as e:
        logger.error(f"Sound failed: {e}")
        return f"Sound failed: {e}"


@mcp.tool()
async def sequence(steps: list[dict]) -> str:
    """Run a sequence of commands with delays between them.

    Each step is a dict with "command" (required) and "delay" in seconds (optional, default 1.0).
    Commands can be any valid send() command name or "bark" for sound.

    Example steps:
        [
            {"command": "walk_forward", "delay": 2.0},
            {"command": "pause"},
            {"command": "left", "delay": 1.0},
            {"command": "walk_forward", "delay": 2.0},
            {"command": "pause"},
            {"command": "bark"},
            {"command": "sit"}
        ]

    Args:
        steps: List of step dicts, each with "command" and optional "delay" (seconds to wait after)
    """
    if bittle is None:
        return "Error: Server not initialized"

    if not bittle.is_connected:
        return "Error: Not connected to Bittle"

    if not steps:
        return "Error: No steps provided"

    sounds = {"bark": "b14,4,17,4,14,4,17,4,14,2"}
    results = []

    for i, step in enumerate(steps):
        command = step.get("command", "")
        delay = step.get("delay", 1.0)

        # Resolve command: check sounds first, then regular commands
        cmd = sounds.get(command.lower()) or COMMANDS.get(command.lower())
        if cmd is None:
            valid = ", ".join(sorted(COMMANDS.keys()))
            results.append(f"Step {i + 1}: Unknown command '{command}'. Valid: {valid}")
            break

        try:
            await bittle.send(cmd)
            results.append(f"Step {i + 1}: {command}")
        except Exception as e:
            results.append(f"Step {i + 1}: Failed ({e})")
            break

        # Wait between steps (skip delay after the last step)
        if i < len(steps) - 1 and delay > 0:
            await asyncio.sleep(delay)

    return "Sequence complete:\n" + "\n".join(results)


@mcp.tool()
async def list_commands() -> str:
    """List all available Bittle commands."""
    commands_list = "\n".join([f"  {name}: {code}" for name, code in COMMANDS.items()])
    gaits_list = "\n".join([f"  {name}: {code}" for name, code in GAITS.items()])
    directions_list = "\n".join([f"  {name}: {code}" for name, code in DIRECTIONS.items()])

    return f"""Available Commands:
{commands_list}

Gaits:
{gaits_list}

Directions:
{directions_list}

Sounds:
  bark: b14,4,17,4,14,4,17,4,14,2
"""


def main():
    """Run the MCP server."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
