# Bittle MCP Server Plan

Build a custom Model Context Protocol (MCP) server to control Bittle via Bluetooth from Claude Code.

## Why Build Our Own

- **Control** - No random dependencies from unknown repos
- **Simple** - Bittle just needs Bluetooth socket + serial commands
- **Extensible** - Add AI Vision module tools later
- **Learning** - MCP is a useful skill

## How Bittle Commands Work

Simple serial strings over Bluetooth at 115200 baud:

| Command | Code | Description |
|---------|------|-------------|
| Rest | `d` | Rest position |
| Forward | `F` | Step forward |
| Backward | `B` | Step backward |
| Left | `L` | Turn left |
| Right | `R` | Turn right |
| Walk | `kwk` | Walk gait |
| Trot | `ktr` | Trot gait |
| Crawl | `kcr` | Crawl gait |
| Sit | `ksit` | Sit pose |
| Hello | `khi` | Wave greeting |
| Balance | `kbalance` | Balance stance |
| Melody | `b<notes>` | Play buzzer tones |

## Architecture

```
Claude Code ←→ MCP Server ←→ Bluetooth ←→ Bittle (BiBoard)
                   ↓
            AI Vision Module (future)
```

## Directory Structure (Implemented)

```
petoi-bittle-project/
├── mcp/
│   ├── pyproject.toml           # Package config
│   ├── .python-version          # Python 3.11
│   ├── README.md                # MCP setup guide
│   └── src/
│       └── bittle_mcp/
│           ├── __init__.py      # Main MCP server with tools
│           ├── __main__.py      # Entry point
│           ├── commands.py      # Command definitions
│           ├── bluetooth.py     # BLE connection handler
│           └── vision.py        # AI Vision tools (Phase 2 - TODO)
```

## Phase 1: Basic MCP Server

### Goals
- Connect to Bittle via Bluetooth
- Send movement commands
- Send pose commands
- Play custom sounds (bark melody)

### MCP Tools to Implement

```python
@mcp.tool()
async def connect(address: str) -> str:
    """Connect to Bittle via Bluetooth MAC address"""

@mcp.tool()
async def disconnect() -> str:
    """Disconnect from Bittle"""

@mcp.tool()
async def send(command: str) -> str:
    """Send command: rest, forward, walk, sit, hello, bark, etc"""

@mcp.tool()
async def move(gait: str, direction: str) -> str:
    """Move with gait (walk/trot/crawl) and direction (forward/left/right/back)"""

@mcp.tool()
async def play_sound(melody: str) -> str:
    """Play a buzzer melody (e.g., bark sound)"""

@mcp.tool()
async def status() -> str:
    """Get connection status"""
```

### Dependencies

```toml
[project]
dependencies = [
    "mcp",           # Official MCP SDK
    "pybluez2",      # Bluetooth (or bleak for BLE)
]
```

### Tasks
- [x] Set up Python project structure
- [x] Implement Bluetooth connection (using bleak)
- [x] Implement basic commands
- [ ] Test with Claude Code (needs robot)
- [x] Document setup process (mcp/README.md)

## Phase 2: AI Vision Integration

### Goals
- Read data from AI Vision module
- Detect objects (Totoro, faces)
- Trigger behaviors based on vision

### MCP Tools to Implement

```python
@mcp.tool()
async def vision_detect() -> dict:
    """Get current detection from AI Vision module"""

@mcp.tool()
async def vision_train(label: str) -> str:
    """Train vision to recognize a new object"""

@mcp.tool()
async def vision_on_detect(label: str, command: str) -> str:
    """Set behavior when object is detected"""
```

### Research Needed
- [ ] How does AI Vision module communicate? (I2C? Serial?)
- [ ] What data format does it return?
- [ ] Can we query it via the BiBoard?

## Phase 3: Advanced Features

- **Reactive behaviors** - See Totoro → do happy dance
- **Family recognition** - Different greetings per person
- **Voice + Vision + MCP** - Full integration
- **Logging/Learning** - Track what works

## Resources

### Official
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Petoi Bluetooth Docs](https://docs.petoi.com/communication-modules/dual-mode-bluetooth)

### Reference (not using, but useful to study)
- [pyBittle](https://github.com/EnriqueMoran/pyBittle) - Python Bittle library (16 stars)
- [pyBittle-mcp-server](https://github.com/cluesang/pyBittle-mcp-server) - Existing MCP attempt

### Bittle Serial Protocol
- Baud rate: 115200
- Commands: Single letters or `k<skill>` format
- Melodies: `b<note>,<duration>,<note>,<duration>,...`

## Getting Started

```bash
# Install dependencies
cd petoi-bittle-project/mcp
uv sync  # or: pip install -e .

# Find Bittle's Bluetooth address
# Mac: System Settings → Bluetooth → Bittle → (i) → Address

# Register with Claude Code (flags BEFORE server name!)
claude mcp add --scope user bittle -- uv --directory $(pwd) run python -m bittle_mcp

# Verify installation
claude mcp list

# Test with MCP Inspector
npx @modelcontextprotocol/inspector uv --directory . run python -m bittle_mcp
```

## Notes

- BiBoard uses Bluetooth SPP (Serial Port Profile)
- Default pairing PIN: 0000 or 1234
- Keep serial monitor closed when using Bluetooth (can't have both)
