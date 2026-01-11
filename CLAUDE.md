# Petoi Bittle Controller Project

## Project Plan
See `docs/PROJECT_PLAN.md` for the full project roadmap with three phases:
1. **Voice Commands** (Priority: High) - Fix non-working voice commands
2. **Controller Customization** (Priority: Medium) - Customize button mappings
3. **AI Vision Module** (Priority: Low) - Future integration

## Documentation
- `docs/reference-links.md` - All external links and quick reference for:
  - Voice module serial commands (`XAa`, `XAc`, etc.)
  - Voice triggers ("Play sound", "Be quiet", etc.)
  - BiBoard audio capabilities
  - AI Vision module docs
- `docs/controller-map.md` - Physical button layout and commands
- `docs/controller-configuration.md` - Setup guide

## Hardware
- **Board:** BiBoard V1.0
- **Voice Module:** Petoi Voice Command Module (has built-in speaker with pre-recorded phrases)
- **Controller:** Micro:bit V2 with joystick module

## Current Status: ✅ Controller Working!

### Completed
- [x] Petoi Desktop App installed
- [x] Bittle firmware updated
- [x] Micro:bit programmed with joystick firmware
- [x] Controller repository cloned to `/ESP32_Microbit_Controller/`
- [x] Documentation created
- [x] Batteries installed, Bluetooth connected
- [x] Controller tested and working

### Next Step
**Configure controller with new actions** - Customize button mappings to send different commands

## Quick Start: Customize Controller

### Current Button Mappings
| Button | Current Command |
|--------|----------------|
| C (P12) | crawl |
| D (P13) | walk |
| E (P14) | trot |
| F (P15) | rest |
| A | hello |
| B | sit |
| Joystick | forward/back/left/right |

### How to Customize

**Source Code Location:**
`/Users/noahworkman-studiom4/Projects/petoi-bittle-project/ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js`

**Key Lines to Edit:**
- Line 31: Button C (P12) command
- Line 36: Button D (P13) command
- Line 41: Button E (P14) command
- Line 46: Button F (P15) command
- Line 51: Button A command
- Line 56: Button B command

**Steps:**
1. Edit `JoyStickTest.js` - Change command strings (e.g., `"crawl"` → `"pee"`)
2. Import into MakeCode: https://makecode.microbit.org
3. Download new .hex file
4. Flash to Micro:bit (drag .hex to Micro:bit drive)

**Available Bittle Commands:**
Common commands: `walk`, `trot`, `crawl`, `sit`, `rest`, `hello`, `pee`, `stretch`, `pushup`, `balance`, `forward`, `back`, `left`, `right`

Find more: Check Petoi docs or test via Petoi Desktop App serial monitor

## Key Files

### Documentation
- `docs/controller-map.md` - Complete physical layout & all commands
- `docs/controller-configuration.md` - Setup guide
- `documentation/reference-links.md` - Web resources

### Firmware
- `firmware/microbit-JoyStick.hex` - Current firmware (1.4MB)

### Source Code
- `ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js` - Button mappings

## Resources

- **MakeCode Editor:** https://makecode.microbit.org
- **Petoi Docs:** https://docs.petoi.com/
- **Controller GitHub:** https://github.com/PetoiCamp/ESP32_Microbit_Controller
- **Product Page:** https://www.petoi.com/products/petoi-robot-controller-microbit-gamepad

## Testing Commands

**Via Petoi Desktop App:**
1. Connect Bittle via USB
2. Open serial monitor
3. Test commands directly (e.g., type `ksit`, `kwkF`)

**Via Controller:**
1. Power on Bittle (auto-pairs with controller)
2. Press buttons to test
3. LED shows feedback on Micro:bit

---
**Last Updated:** Nov 23, 2024
**Status:** Ready to customize button mappings
