# Micro:bit Controller Configuration

## Your Current Firmware
- **File:** microbit-JoyStick.hex
- **Location:** `firmware/microbit-JoyStick.hex`
- **Status:** Already flashed to Micro:bit V2

## Quick Reference

See [controller-map.md](./controller-map.md) for complete physical layout and pin mappings.

## Button & Joystick Mappings (from test code reference)

### Joystick Controls
- **Right** (X ≤ 200): "right" command
- **Left** (X ≥ 800): "left" command
- **Back** (Y ≤ 200): "back" command
- **Forward** (Y ≥ 800): "forward" command
- **Neutral** (X: 500-550, Y: 500-550): "balance" command

### Physical Buttons
**Joystick Module Buttons:**
- **P12 (C)**: "crawl" gait
- **P13 (D)**: "walk" gait
- **P14 (E)**: "trot" gait
- **P15 (F)**: "rest" command

**Micro:bit Buttons:**
- **A**: "hello" greeting
- **B**: "sit" command

## How to View Your Configuration in MakeCode

Since the source code isn't published separately, you need to import your hex file:

1. Go to https://makecode.microbit.org
2. Click **Import** → **Import File**
3. Select: `firmware/microbit-JoyStick.hex` from this repo
4. View the blocks or switch to JavaScript to see exact mappings

## Source Code Reference
- Test implementation: https://github.com/PetoiCamp/ESP32_Microbit_Controller/blob/main/Joystick/Microbit_joystick/JoyStickTest.js
- Full repo: https://github.com/PetoiCamp/ESP32_Microbit_Controller

## Bluetooth Communication
- Protocol: UART over Bluetooth
- Target: ESP32 BiBoard on Bittle
- Commands: String-based (e.g., "walk", "sit", "forward")

## Notes
- The actual microbit-JoyStick.hex may have different/additional commands
- Import into MakeCode to see the complete configuration
- Visual LED indicators show movement directions
- Dead zone prevents jitter when joystick is neutral
