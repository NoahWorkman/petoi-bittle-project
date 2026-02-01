"""Tests for MockBittleConnection behavior."""

import pytest

from bittle_mcp.bluetooth import MockBittleConnection


@pytest.fixture
def conn():
    return MockBittleConnection()


async def test_connect_and_disconnect(conn):
    await conn.connect("AA:BB:CC:DD:EE:FF")
    assert conn.is_connected
    assert conn.address == "AA:BB:CC:DD:EE:FF"

    await conn.disconnect()
    assert not conn.is_connected


async def test_is_connected_initially_false(conn):
    assert not conn.is_connected


async def test_send_while_disconnected_raises(conn):
    with pytest.raises(RuntimeError):
        await conn.send("ksit")


async def test_double_connect_disconnects_first(conn):
    await conn.connect("AA:BB:CC:DD:EE:FF")
    await conn.connect("11:22:33:44:55:66")
    assert conn.is_connected
    assert conn.address == "11:22:33:44:55:66"


async def test_address_property(conn):
    assert conn.address is None
    await conn.connect("AA:BB:CC:DD:EE:FF")
    assert conn.address == "AA:BB:CC:DD:EE:FF"
