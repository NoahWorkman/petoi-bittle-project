# Petoi Bittle Reference Links

## Official Documentation

### Controller Resources
- [Joystick with Micro:bit - Official Docs](https://docs.petoi.com/extensible-modules/joystick-with-micro-bit)
- [Petoi Micro:bit Controller Product Page](https://www.petoi.com/products/petoi-robot-controller-microbit-gamepad)
- [ESP32 Micro:bit Controller GitHub Repo](https://github.com/PetoiCamp/ESP32_Microbit_Controller)

### Source Code
- [JoyStickTest.js Source Code](https://github.com/PetoiCamp/ESP32_Microbit_Controller/blob/main/Joystick/Microbit_joystick/JoyStickTest.js)
- [Micro:bit Joystick Directory](https://github.com/PetoiCamp/ESP32_Microbit_Controller/tree/main/Joystick/Microbit_joystick)

### Firmware
- [microbit-JoyStick.hex Download](https://raw.githubusercontent.com/PetoiCamp/ESP32_Microbit_Controller/refs/heads/main/microbit-JoyStick.hex)

## Voice Command Module
- [Voice Command Module - Official Docs](https://docs.petoi.com/extensible-modules/voice-command-module)
- Serial commands:
  - `XAa` - Switch to English
  - `XAb` - Switch to Chinese
  - `XAc` - Enable audio response
  - `XAd` - Disable audio response
  - `XAe` - Start learning custom commands
  - `XAf` - Stop learning
  - `XAg` - Clear all learning data
- Voice triggers (say these out loud):
  - "Bing-bing" - Switch to English
  - "Di-di" - Switch to Chinese
  - "Play sound" - Enable voice reactions
  - "Be quiet" - Disable voice reactions
  - "Start learning" - Record custom commands (up to 10)
  - "Stop learning" - Stop recording
  - "Clear the learning data" - Delete all recordings

## BiBoard Documentation
- [BiBoard V0 Overview](https://docs.petoi.com/biboard/biboard-v0)
- Audio capabilities:
  - DAC + Class-D amplifier (not just a buzzer)
  - Can play MP3 files via SPIFFS/FAT filesystem
  - ESP32 dacWrite() for higher quality audio
- [XTronical ESP32 Audio Guide](https://www.xtronical.com/basics/audio/dacs-on-esp32/)

## AI Vision Module
- [AI Vision Module - Official Docs](https://docs.petoi.com/extensible-modules/ai-vision-module)
- [MU Vision Sensor Documentation](https://morpx-docs.readthedocs.io/)

## Petoi General Resources
- [Petoi Documentation Home](https://docs.petoi.com/)
- [OpenCat GitHub Repository](https://github.com/PetoiCamp/OpenCat)
- [OpenCat Releases (Desktop App)](https://github.com/PetoiCamp/OpenCat/releases/latest)

## Development Tools
- [Microsoft MakeCode for Micro:bit](https://makecode.microbit.org)
  - Use this to import and view your microbit-JoyStick.hex configuration

## Community
- [Petoi Forum](https://www.petoi.camp/forum)
- [Bittle X micro:bit Remote Control Discussion](https://www.petoi.camp/forum/general-discussions/bittle-x-micro-bit-remote-control)

## Third-Party Controller Options
- [ELECFREAKS Joystick:bit V2](https://shop.elecfreaks.com/products/elecfreaks-micro-bit-joystick-bit-v2-remote-controller-without-acrylic-handle)
- [Waveshare Joystick for micro:bit](https://www.waveshare.com/wiki/Joystick_for_micro:bit)
- [Yahboom Micro:bit Handle](https://category.yahboom.net/products/basicgamehandle)

## Local Documentation
- [Controller Configuration Guide](./controller-configuration.md)
- [Complete Controller Map](./controller-map.md)
