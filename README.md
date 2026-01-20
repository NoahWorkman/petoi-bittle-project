# Petoi Bittle Project

A personal project for customizing and extending the Petoi Bittle X v2 robot dog with voice commands, custom controller mappings, and AI vision.

## Hardware

- **Robot:** [Petoi Bittle X v2](https://www.petoi.com/pages/bittle-open-source-bionic-robot-dog)
- **Board:** BiBoard V1.0
- **Controller:** [Micro:bit V2 with joystick module](https://www.petoi.com/products/petoi-robot-controller-microbit-gamepad)
- **Voice Module:** Petoi Voice Command Module
- **AI Vision:** Petoi AI Vision Module (future)

## Project Goals

1. **Voice Commands** - Get voice control working reliably ✅
2. **Controller Customization** - Custom button mappings for preferred actions (in progress)
3. **MCP Server** - Control Bittle from Claude Code via Bluetooth (in progress) 
4. **AI Vision** - Object recognition (Totoro stuffed animal) and family member recognition
5. **AI Vison 2.0 ** - Common undesirable garden plant vision training
   

## Quick Start

### Prerequisites
- [Petoi Desktop App](https://github.com/PetoiCamp/OpenCat/releases/latest)
- Micro:bit V2 with joystick module
- 2x AAA batteries for controller

### Setup
1. Install Petoi Desktop App
2. Connect Bittle via USB, update firmware if needed
3. Flash `firmware/microbit-JoyStick.hex` to your Micro:bit
4. Install batteries in controller
5. Power on Bittle - controller auto-pairs via Bluetooth

### Voice Module Setup
If voice commands aren't working, connect via USB and send these commands in Skill Composer:
- `XAa` - Switch to English
- `XAc` - Enable audio response

## Documentation

| File | Description |
|------|-------------|
| [docs/PROJECT_PLAN.md](docs/PROJECT_PLAN.md) | Full project roadmap and milestones |
| [docs/MCP_PLAN.md](docs/MCP_PLAN.md) | MCP server design for Claude Code integration |
| [docs/reference-links.md](docs/reference-links.md) | External links, serial commands, voice triggers |
| [docs/controller-map.md](docs/controller-map.md) | Physical button layout and all commands |
| [docs/controller-configuration.md](docs/controller-configuration.md) | Controller setup guide |

## Controller Button Mappings

| Button | Command |
|--------|---------|
| A | hello |
| B | sit |
| C (P12) | crawl |
| D (P13) | walk |
| E (P14) | trot |
| F (P15) | rest |
| Joystick | forward/back/left/right |

## Customizing the Controller

1. Edit `ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js`
2. Import into [MakeCode](https://makecode.microbit.org)
3. Download new .hex file
4. Flash to Micro:bit (drag .hex to Micro:bit drive)

## Common Bittle Commands

**Movement:** `walk`, `trot`, `crawl`, `forward`, `back`, `left`, `right`

**Poses:** `sit`, `rest`, `balance`, `stand`

**Tricks:** `hello`, `pee`, `stretch`, `pushup`

**Melodies:** `b` followed by note,duration pairs (e.g., `b20,16,0,16,18,16,0,8,20,8` for a robot bark)

## Resources

- [Petoi Documentation](https://docs.petoi.com/)
- [OpenCat GitHub](https://github.com/PetoiCamp/OpenCat)
- [ESP32 Microbit Controller](https://github.com/PetoiCamp/ESP32_Microbit_Controller)
- [MakeCode for Micro:bit](https://makecode.microbit.org)

## License

MIT License - See [LICENSE](LICENSE) for details.

This project includes code from:
- [PetoiCamp/ESP32_Microbit_Controller](https://github.com/PetoiCamp/ESP32_Microbit_Controller) (MIT License)
- [PetoiCamp/OpenCat](https://github.com/PetoiCamp/OpenCat) (MIT License)
- Adafruit libraries (BSD/LGPL)

See LICENSE file for full attribution.
