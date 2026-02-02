"""
Bittle command definitions.

These are the serial commands that Bittle understands.
Commands are sent over Bluetooth at 115200 baud.

Reference: https://docs.petoi.com/
"""

# Basic commands (single letter or k<skill>)
COMMANDS: dict[str, str] = {
    # Poses
    "rest": "d",
    "sit": "ksit",
    "stand": "kup",
    "balance": "kbalance",
    "zero": "kzero",

    # Tricks
    "hello": "khi",
    "pee": "kpee",
    "stretch": "kstr",
    "pushup": "kpu",
    "sit_up": "ksup",
    "check": "kck",
    "boxing": "kbx",
    "wave": "kwh",

    # Gaits (movement modes)
    "walk": "kwk",
    "trot": "ktr",
    "crawl": "kcr",
    "run": "krn",

    # Directions (use with gait)
    "forward": "F",
    "backward": "B",
    "left": "L",
    "right": "R",

    # Combos
    "walk_forward": "kwkF",
    "walk_left": "kwkL",
    "walk_right": "kwkR",
    "walk_backward": "kwkB",
    "trot_forward": "ktrF",
    "crawl_forward": "kcrF",

    # System
    "gyro_on": "g",
    "gyro_off": "G",
    "pause": "p",
    # Custom sounds (note,duration pairs — notes 8-17 are reliably audible)
    "bark": "b14,4,17,4,14,4,17,4,14,2",
}

# Gaits for movement
GAITS: dict[str, str] = {
    "walk": "kwk",
    "trot": "ktr",
    "crawl": "kcr",
    "run": "krn",
}

# Directions for movement
DIRECTIONS: dict[str, str] = {
    "forward": "F",
    "backward": "B",
    "left": "L",
    "right": "R",
}
