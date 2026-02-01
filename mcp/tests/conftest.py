"""Shared fixtures for Bittle MCP tests."""

import pytest

from bittle_mcp.bluetooth import MockBittleConnection


@pytest.fixture
def mock_conn():
    """Provide a fresh MockBittleConnection."""
    return MockBittleConnection()
