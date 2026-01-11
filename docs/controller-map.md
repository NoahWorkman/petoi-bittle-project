# Micro:bit Joystick Controller - Complete Map

## Physical Layout

```
                    [Touch/Logo]

        [D Button]


    [Joystick]    [A]  [B]    [C Button]    [F Button]


                    [E Button]
```

## All Controller Elements

### Micro:bit Built-in
| Element | Location | Pin | Function |
|---------|----------|-----|----------|
| Button A | Left of Micro:bit | Built-in | Command: "hello" / "Hi" |
| Button B | Right of Micro:bit | Built-in | Command: "sit" |
| Touch/Logo | Center top of Micro:bit | Built-in | Special functions (timed lock) |

### Joystick Module
| Element | Location | Pin | Function |
|---------|----------|-----|----------|
| Joystick X-axis | Center left | Analog | Left/Right movement |
| Joystick Y-axis | Center left | Analog | Forward/Back movement |
| Button C | Right side | P12 | Command: "crawl" gait |
| Button D | Top center | P13 | Command: "walk" gait |
| Button E | Bottom center | P14 | Command: "trot" gait |
| Button F | Far right | P15 | Command: "rest" |
| Buzzer | Internal | TBD | Audio feedback |
| Vibration Motor | Internal | TBD | Haptic feedback |

## Joystick Movement Mapping

### Axis Values
- **X-axis Range:** 0 (left) to 1023 (right)
- **Y-axis Range:** 0 (back) to 1023 (forward)
- **Neutral/Center:** X: 500-550, Y: 500-550

### Directional Commands
| Movement | X Value | Y Value | Command Sent |
|----------|---------|---------|--------------|
| Forward | ~500 | ≥ 800 | "forward" |
| Backward | ~500 | ≤ 200 | "back" |
| Left | ≥ 800 | ~500 | "left" |
| Right | ≤ 200 | ~500 | "right" |
| Neutral | 500-550 | 500-550 | "balance" |

### Diagonal Movements
Combine X and Y axis values for diagonal movement.

## Button Combinations

According to documentation, these combinations are supported:
- **A+B** (Micro:bit buttons)
- **C+E** (Joystick module buttons P12 + P14)
- **D+F** (Joystick module buttons P13 + P15)
- **E+F** (Joystick module buttons P14 + P15)

*Note: Specific commands for combinations depend on the firmware version.*

## Button Command Summary

| Button | Pin | Display | Command | Description |
|--------|-----|---------|---------|-------------|
| A | Built-in | "Hi" | "hello" | Greeting pose |
| B | Built-in | "Sit" | "sit" | Sit pose |
| C | P12 | "C" | "crawl" | Crawl gait mode |
| D | P13 | "W" | "walk" | Walk gait mode |
| E | P14 | "T" | "trot" | Trot gait mode |
| F | P15 | "Rest" | "rest" | Rest/sleep mode |
| Touch/Logo | Built-in | - | Special | Hold for timed lock |

## Special Features

### Timed Lock Feature
- **Activation:** Press and hold Touch/Logo button while keeping controller upright
- **Function:** Sends "rest" command to robot every 20 minutes
- **Use Case:** Limit playtime for kids

### Visual Feedback
- Micro:bit LED display shows movement direction
- LED indicators for button presses

### Communication
- **Protocol:** Bluetooth UART
- **Target:** ESP32 BiBoard on Bittle
- **Auto-pairing:** During Bittle bootup

## Power Requirements

- **Batteries:** 2x AAA batteries
- **Installation:** Battery compartment on controller

## Firmware Details

- **Current File:** microbit-JoyStick.hex (1.4 MB)
- **Platform:** Microsoft MakeCode
- **Source:** https://github.com/PetoiCamp/ESP32_Microbit_Controller
- **Bluetooth Range:** ~10 meters typical

## Notes

- Button functions may vary slightly by robot model (Bittle, Bittle X, Nybble)
- 300ms delay between detecting double-tap events
- Dead zone prevents joystick jitter at neutral position
- Import hex file into MakeCode to see complete configuration
