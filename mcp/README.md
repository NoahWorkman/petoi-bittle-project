# Bittle MCP Server

Control your Petoi Bittle robot via Bluetooth directly from Claude Code.

## Features

- Connect to Bittle via Bluetooth LE
- Send movement commands (walk, trot, crawl)
- Send pose commands (sit, rest, hello)
- Play custom sounds (bark melody)
- List available commands

## Requirements

- Python 3.10+
- macOS, Linux, or Windows with Bluetooth
- Petoi Bittle with BiBoard (Bluetooth enabled)

## Installation

```bash
cd mcp

# Using uv (recommended)
uv sync

# Or using pip
pip install -e .
```

## Finding Your Bittle's Bluetooth Address

### macOS
1. System Settings → Bluetooth
2. Turn on Bittle
3. Find "Bittle" or "Petoi" in the list
4. Click (i) to see the address

### Linux
```bash
bluetoothctl scan on
# Look for "Bittle" or "Petoi"
```

## Register with Claude Code

```bash
# Add the MCP server
claude mcp add bittle -- uv --directory /path/to/petoi-bittle-project/mcp run python -m bittle_mcp

# Or with absolute path
claude mcp add bittle -- uv --directory $(pwd) run python -m bittle_mcp
```

## Usage

Once registered, Claude Code can use these tools:

### Connect
```
Connect to Bittle at XX:XX:XX:XX:XX:XX
```

### Send Commands
```
Make Bittle sit
Make Bittle walk forward
Make Bittle do the hello trick
```

### Play Sounds
```
Make Bittle bark
```

## Available Tools

| Tool | Description |
|------|-------------|
| `connect(address)` | Connect to Bittle via Bluetooth |
| `disconnect()` | Disconnect from Bittle |
| `status()` | Get connection status |
| `send(command)` | Send a command (sit, walk, hello, etc.) |
| `move(direction, gait)` | Move with gait and direction |
| `play_sound(sound)` | Play a sound (bark) |
| `list_commands()` | List all available commands |

## Available Commands

### Poses
- `sit` - Sit down
- `rest` - Rest position
- `stand` - Stand up
- `balance` - Balance stance

### Tricks
- `hello` - Wave greeting
- `pee` - Pee pose
- `stretch` - Stretch
- `pushup` - Do pushups

### Movement
- `walk` / `trot` / `crawl` - Gait modes
- `forward` / `backward` / `left` / `right` - Directions

### Sounds
- `bark` - Robot bark melody

## Testing

```bash
# Test with MCP Inspector
npx @modelcontextprotocol/inspector uv --directory . run python -m bittle_mcp
```

## Troubleshooting

### "bleak not installed"
```bash
uv add bleak
# or
pip install bleak
```

### Connection fails
1. Make sure Bittle is powered on
2. Check Bluetooth is enabled on your computer
3. Verify the MAC address is correct
4. Try re-pairing in system Bluetooth settings

### Commands not working
1. Check connection status with `status()` tool
2. Make sure you're sending valid commands
3. Use `list_commands()` to see available commands

## Development

```bash
# Install dev dependencies
uv sync --dev

# Run tests
pytest
```

## License

MIT - See parent project LICENSE
