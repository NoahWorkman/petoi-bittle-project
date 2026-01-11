# Petoi Bittle Project Plan

## Overview
Long-term project to fully customize and expand capabilities of Petoi Bittle X v2 robot dog.

## Current Status
- Controller connected via Bluetooth (working)
- Default button mappings active (not customized)
- Voice commands not working
- AI Vision module not yet integrated

---

## Phase 1: Voice Commands (Priority: High)

### Goal
Get voice commands working reliably with Bittle.

### Current Issue
Voice commands are not functioning - needs diagnosis.

### Tasks
- [ ] Diagnose why voice commands aren't working
  - Check if voice module is properly connected
  - Verify firmware supports voice commands
  - Test via Petoi Desktop App serial monitor
- [ ] Document available voice commands
- [ ] Test basic voice recognition
- [ ] Configure custom voice triggers if supported

### Resources
- [Petoi Voice Command Module docs](https://docs.petoi.com/extensible-modules/voice-command-module)

---

## Phase 2: Bluetooth Controller Customization (Priority: Medium)

### Goal
Customize controller button mappings to preferred actions.

### Current State
Controller connected and working with default mappings:
| Button | Current | Desired |
|--------|---------|---------|
| C (P12) | crawl | TBD |
| D (P13) | walk | TBD |
| E (P14) | trot | TBD |
| F (P15) | rest | TBD |
| A | hello | TBD |
| B | sit | TBD |

### Tasks
- [ ] Test all available Bittle commands via serial monitor
- [ ] Create list of favorite/useful commands
- [ ] Design custom button mapping layout
- [ ] Edit `JoyStickTest.js` with new mappings
- [ ] Compile and flash new firmware to Micro:bit
- [ ] Test and iterate

### Files to Edit
- `ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js`

### Process
1. Edit source code
2. Import to MakeCode (https://makecode.microbit.org)
3. Download .hex file
4. Flash to Micro:bit

---

## Phase 3: AI Vision Module (Priority: Low - Future)

### Goal
Integrate AI Vision module with specific recognition targets.

### Hardware
- Petoi AI Vision module (owned, not yet installed)

### Milestone 3.1: Basic Setup
Get the vision module working correctly.
- [ ] Read AI Vision module documentation
- [ ] Install module on Bittle
- [ ] Connect and configure
- [ ] Test basic object detection
- [ ] Verify camera feed and recognition works

### Milestone 3.2: Totoro Recognition
Train/configure to recognize Totoro stuffed animal.
- [ ] Research custom object training options
- [ ] Capture reference images of Totoro
- [ ] Train or configure recognition model
- [ ] Test Totoro detection reliability
- [ ] Create custom behavior when Totoro is detected (e.g., happy reaction)

### Milestone 3.3: Family Member Recognition
Recognize and respond to family members.
- [ ] Research face recognition capabilities
- [ ] Capture reference images of each family member
- [ ] Train face recognition for each person
- [ ] Create personalized responses per family member
- [ ] Test recognition accuracy and distance

### Resources
- [Petoi AI Vision Module docs](https://docs.petoi.com/extensible-modules/ai-vision-module)
- [MU Vision Sensor docs](https://morpx-docs.readthedocs.io/)

---

## Available Bittle Commands Reference

### Movement
- `walk` / `wkF` - Walk forward
- `back` / `bk` - Walk backward
- `left` / `wkL` - Turn left
- `right` / `wkR` - Turn right
- `trot` / `tr` - Trot gait
- `crawl` / `cr` - Crawl gait
- `bound` - Bounding gait

### Poses
- `sit` - Sit down
- `rest` - Rest position
- `balance` - Balance stance
- `stand` - Stand up

### Tricks
- `hello` - Wave hello
- `pee` - Pee pose
- `stretch` - Stretch
- `pushup` - Do pushups
- `check` - Check around
- `table` - Table pose

### Other
- `forward` - Step forward
- `back` - Step back
- `gyro` - Toggle gyroscope

### Custom Sounds
- **Robot Bark:** `b20,16,0,16,18,16,0,8,20,8`
  - Send via serial monitor to test
  - Can be linked to a voice command trigger

---

## Notes

### Session Log
- **Jan 2026**: Created GitHub repo, established project plan. Fixed voice module (was stuck in Chinese) - sent `XAa` to switch to English, `XAc` to enable audio. Created robot bark melody.
- **Nov 2024**: Initial setup, controller working

### Questions to Research
- What causes voice command issues?
- Can controller and voice work simultaneously?
- Vision module compute requirements?
- Custom skill creation process?

---

## Quick Reference

### Key Paths
- Controller source: `ESP32_Microbit_Controller/Joystick/Microbit_joystick/JoyStickTest.js`
- Firmware: `firmware/microbit-JoyStick.hex`
- Controller docs: `docs/controller-map.md`

### Key URLs
- MakeCode: https://makecode.microbit.org
- Petoi Docs: https://docs.petoi.com/
- OpenCat GitHub: https://github.com/PetoiCamp/OpenCat
