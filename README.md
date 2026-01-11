# Petoi Bittle Project

Setup guide for controlling Bittle Petoi X v2 with Micro:bit joystick controller.

## Hardware

- **Robot:** Bittle Petoi X v2
- **Controller:** Micro:bit V2 with joystick module
- **Requirements:** 2x AAA batteries for controller

## Setup Process

### 1. Install Petoi Desktop App (Mac)

1. Download from [GitHub Releases](https://github.com/PetoiCamp/OpenCat/releases/latest)
2. Look for Mac `.dmg` file in Assets
3. Double-click `.dmg` and drag to Applications
4. Right-click app → Hold Shift → Click Open (bypass security)

### 2. Check/Update Bittle Firmware

1. Power OFF Bittle
2. Connect via USB to Mac
3. Open Petoi Desktop App
4. Select serial port (e.g., `/dev/cu.usbserial-*`)
5. Check current firmware version
6. Update if needed via Firmware Uploader

### 3. Setup Micro:bit Controller

1. Download `microbit-JoyStick.hex` from [Petoi docs](https://docs.petoi.com/extensible-modules/joystick-with-micro-bit)
2. Connect Micro:bit V2 to Mac via USB
3. Drag `.hex` file to Micro:bit drive
4. Wait for LED to stop flashing

### 4. Connect and Test

1. Install 2 AAA batteries in controller
2. Power on Bittle
3. Controller should auto-pair via Bluetooth
4. Test joystick movements

## Resources

- [Petoi Docs](https://docs.petoi.com/)
- [Micro:bit Joystick Guide](https://docs.petoi.com/extensible-modules/joystick-with-micro-bit)
- [OpenCat GitHub](https://github.com/PetoiCamp/OpenCat)

## Status

- [x] Petoi Desktop App installed
- [x] Firmware checked/updated
- [x] Micro:bit programmed with joystick firmware
- [ ] Bluetooth connection tested (pending Bittle battery charge)

## Notes

### Firmware Installation (Nov 9, 2024)
- Downloaded `microbit-JoyStick.hex` from [ESP32_Microbit_Controller repo](https://raw.githubusercontent.com/PetoiCamp/ESP32_Microbit_Controller/refs/heads/main/microbit-JoyStick.hex)
- File saved to `/firmware/microbit-JoyStick.hex` (1.4MB)
- Successfully flashed to Micro:bit V2
- Firmware flash takes ~15-30 seconds (yellow LED flashes during install)

### Troubleshooting
- **Red LED flashing 3x on Bittle**: Low battery - charge before testing
- **Hex file disappears from Micro:bit**: Normal behavior - file auto-programs and vanishes
- **Flashing takes time**: 1.4MB file requires 15-30 seconds to flash completely
