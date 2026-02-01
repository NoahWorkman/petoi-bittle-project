"""Tests for command dictionary validation."""

from bittle_mcp.commands import COMMANDS, GAITS, DIRECTIONS


def test_all_command_values_are_nonempty_strings():
    for name, code in COMMANDS.items():
        assert isinstance(code, str) and len(code) > 0, f"{name} has empty code"


def test_all_gaits_exist_in_commands():
    for name, code in GAITS.items():
        assert name in COMMANDS, f"Gait '{name}' not in COMMANDS"
        assert COMMANDS[name] == code


def test_all_directions_exist_in_commands():
    for name, code in DIRECTIONS.items():
        assert name in COMMANDS, f"Direction '{name}' not in COMMANDS"
        assert COMMANDS[name] == code


def test_no_duplicate_command_codes():
    codes = list(COMMANDS.values())
    seen = {}
    for name, code in COMMANDS.items():
        assert code not in seen, f"Duplicate code '{code}' for '{name}' and '{seen[code]}'"
        seen[code] = name


def test_calibrate_not_in_commands():
    assert "calibrate" not in COMMANDS
