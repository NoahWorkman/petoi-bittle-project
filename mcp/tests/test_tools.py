"""Integration tests for MCP tool functions."""

import pytest

import bittle_mcp
from bittle_mcp import scan, connect, disconnect, send, move, play_sound, status, list_commands
from bittle_mcp.bluetooth import MockBittleConnection


@pytest.fixture(autouse=True)
def setup_mock_connection():
    """Inject a MockBittleConnection for every test."""
    mock = MockBittleConnection()
    bittle_mcp.bittle = mock
    yield mock
    bittle_mcp.bittle = None


# --- scan ---

async def test_scan_returns_mock_device(setup_mock_connection):
    result = await scan()
    assert "MockBittle" in result
    assert "00:00:00:00:00:00" in result


async def test_scan_custom_timeout(setup_mock_connection):
    result = await scan(timeout=5.0)
    assert "Found" in result


# --- connect ---

async def test_connect_valid_mac(setup_mock_connection):
    result = await connect("AA:BB:CC:DD:EE:FF")
    assert "Connected" in result


async def test_connect_valid_macos_uuid(setup_mock_connection):
    result = await connect("12345678-1234-1234-1234-123456789ABC")
    assert "Connected" in result


async def test_connect_invalid_address():
    result = await connect("not-a-mac")
    assert "Invalid address" in result


async def test_connect_invalid_short_mac():
    result = await connect("AA:BB:CC")
    assert "Invalid address" in result


# --- send ---

async def test_send_known_command(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await send("sit")
    assert "Sent" in result


async def test_send_unknown_command(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await send("unknown_garbage")
    assert "Unknown command" in result
    assert "Valid commands" in result


async def test_send_while_disconnected():
    result = await send("sit")
    assert "Not connected" in result


# --- move ---

async def test_move_forward_walk(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await move("forward", "walk")
    assert "Moving" in result


async def test_move_invalid_direction(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await move("up", "walk")
    assert "Unknown direction" in result


async def test_move_invalid_gait(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await move("forward", "gallop")
    assert "Unknown gait" in result


# --- play_sound ---

async def test_play_sound_bark(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await play_sound("bark")
    assert "Playing" in result


async def test_play_sound_unknown(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await play_sound("arbitrary_string")
    assert "Unknown sound" in result


# --- status ---

async def test_status_disconnected():
    result = await status()
    assert "Not connected" in result


async def test_status_connected(setup_mock_connection):
    await connect("AA:BB:CC:DD:EE:FF")
    result = await status()
    assert "AA:BB:CC:DD:EE:FF" in result


# --- disconnect ---

async def test_disconnect_when_not_connected():
    result = await disconnect()
    assert "Not connected" in result


# --- list_commands ---

async def test_list_commands_returns_content():
    result = await list_commands()
    assert len(result) > 0
    assert "sit" in result
    assert "walk" in result
