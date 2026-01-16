# Petoi Bittle Project - Claude Context

## Hardware
- **Robot:** Bittle X v2
- **Board:** BiBoard V1.0
- **Voice Module:** Petoi Voice Command Module (has built-in speaker with pre-recorded phrases)
- **Controller:** Micro:bit V2 with joystick module
- **AI Vision:** Petoi AI Vision Module (not yet installed)

## Project Status
- ✅ Controller working (Bluetooth tested and connected)
- ✅ Voice module working (English, audio enabled)
- ⏳ Test robot bark melody (`b20,16,0,16,18,16,0,8,20,8`)
- ⏳ Link bark to voice command trigger
- ⏳ Controller customization (customize button mappings)
- ⏳ MCP Server (control Bittle from Claude Code via Bluetooth)
- ⏳ AI Vision module (future - Totoro recognition, family recognition)

## Key Documentation
| File | Purpose |
|------|---------|
| `docs/PROJECT_PLAN.md` | Roadmap with 4 phases and milestones |
| `docs/MCP_PLAN.md` | MCP server design and implementation plan |
| `mcp/README.md` | MCP server setup and usage guide |
| `docs/reference-links.md` | All external links, serial commands, voice triggers |
| `docs/controller-map.md` | Physical button layout and commands |
| `docs/controller-configuration.md` | Setup guide |

## MCP Server (mcp/)
The MCP server is implemented and ready for testing:

```bash
# Install
cd mcp && uv sync

# Register with Claude Code (flags BEFORE server name)
claude mcp add --scope user bittle -- uv --directory /path/to/mcp run python -m bittle_mcp

# Verify
claude mcp list
```

### MCP Tools Available
| Tool | Description |
|------|-------------|
| `connect(address)` | Connect via Bluetooth |
| `disconnect()` | Disconnect |
| `status()` | Connection status |
| `send(command)` | Send command (sit, walk, hello, bark) |
| `move(direction, gait)` | Move with gait |
| `play_sound(sound)` | Play bark sound |
| `list_commands()` | Show all commands |

## Quick Reference

### Voice Module Serial Commands
Send via Petoi Desktop App → Skill Composer → text field → Send:
- `XAa` - Switch to English
- `XAb` - Switch to Chinese
- `XAc` - Enable audio response
- `XAd` - Disable audio response

### Custom Sounds
- **Robot Bark:** `b20,16,0,16,18,16,0,8,20,8`

### Controller Button Mappings
| Button | Command |
|--------|---------|
| A | hello |
| B | sit |
| C (P12) | crawl |
| D (P13) | walk |
| E (P14) | trot |
| F (P15) | rest |
| Joystick | forward/back/left/right |

### Key Source Files
- `ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js` - Controller button mappings
- `ESP32_Microbit_Controller/controller/OpenCatEsp32_micorbit_BittleR/src/voice.h` - Voice module code
- `ESP32_Microbit_Controller/controller/OpenCatEsp32_micorbit_BittleR/src/sound.h` - Sound/melody code

## Common Bittle Commands
**Movement:** `walk`, `trot`, `crawl`, `forward`, `back`, `left`, `right`
**Poses:** `sit`, `rest`, `balance`, `stand`
**Tricks:** `hello`, `pee`, `stretch`, `pushup`
**Melodies:** `b` followed by note,duration pairs (e.g., `b20,16,0,16,18,16`)
