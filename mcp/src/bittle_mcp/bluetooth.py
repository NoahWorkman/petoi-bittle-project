"""
Bluetooth connection handler for Petoi Bittle.

Uses bleak for cross-platform Bluetooth LE support.
Bittle's BiBoard uses Bluetooth SPP (Serial Port Profile) over BLE.

Connection details:
- Baud rate: 115200 (handled by the device)
- Protocol: UART over BLE
"""

import asyncio
import logging
from typing import Optional

try:
    from bleak import BleakClient, BleakScanner
    BLEAK_AVAILABLE = True
except ImportError:
    BLEAK_AVAILABLE = False

logger = logging.getLogger("bittle-mcp.bluetooth")

# Bittle BLE UART Service UUIDs (Nordic UART Service)
UART_SERVICE_UUID = "6e400001-b5a3-f393-e0a9-e50e24dcca9e"
UART_TX_CHAR_UUID = "6e400002-b5a3-f393-e0a9-e50e24dcca9e"  # Write to this
UART_RX_CHAR_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # Read from this


class BittleConnection:
    """Manages Bluetooth connection to Petoi Bittle."""

    def __init__(self):
        self._client: Optional[BleakClient] = None
        self._address: Optional[str] = None
        self._connected: bool = False

    @property
    def is_connected(self) -> bool:
        """Check if connected to Bittle."""
        return self._connected and self._client is not None

    @property
    def address(self) -> Optional[str]:
        """Get connected device address."""
        return self._address

    async def scan(self, timeout: float = 10.0) -> list[dict]:
        """Scan for nearby Bittle devices.

        Args:
            timeout: Scan duration in seconds

        Returns:
            List of discovered devices with name and address
        """
        if not BLEAK_AVAILABLE:
            logger.error("bleak not installed")
            return []

        logger.info(f"Scanning for Bittle devices ({timeout}s)...")
        devices = await BleakScanner.discover(timeout=timeout)

        bittle_devices = []
        for device in devices:
            name = device.name or ""
            if "bittle" in name.lower() or "petoi" in name.lower():
                bittle_devices.append({
                    "name": name,
                    "address": device.address
                })
                logger.info(f"Found: {name} ({device.address})")

        return bittle_devices

    async def connect(self, address: str) -> bool:
        """Connect to Bittle at the given Bluetooth address.

        Args:
            address: Bluetooth MAC address (e.g., "XX:XX:XX:XX:XX:XX")

        Returns:
            True if connected successfully
        """
        if not BLEAK_AVAILABLE:
            raise RuntimeError("bleak not installed. Run: pip install bleak")

        if self._connected:
            await self.disconnect()

        logger.info(f"Connecting to {address}...")

        self._client = BleakClient(address)
        try:
            await self._client.connect(timeout=10.0)
            self._address = address
            self._connected = True
            logger.info(f"Connected to {address}")

            # Set up notification handler for responses
            await self._client.start_notify(UART_RX_CHAR_UUID, self._notification_handler)

            return True
        except Exception as e:
            logger.error(f"Connection failed: {e}")
            self._client = None
            self._connected = False
            raise

    async def disconnect(self) -> None:
        """Disconnect from Bittle."""
        if self._client:
            try:
                await self._client.disconnect()
            except Exception as e:
                logger.warning(f"Disconnect error: {e}")
            finally:
                self._client = None
                self._connected = False
                logger.info("Disconnected")

    async def send(self, command: str) -> None:
        """Send a command to Bittle.

        Args:
            command: Serial command to send (e.g., "ksit", "kwkF")
        """
        if not self._connected or not self._client:
            raise RuntimeError("Not connected to Bittle")

        # Add newline if not present (Bittle expects newline-terminated commands)
        if not command.endswith("\n"):
            command = command + "\n"

        data = command.encode("utf-8")
        logger.debug(f"Sending: {command.strip()}")

        try:
            await self._client.write_gatt_char(UART_TX_CHAR_UUID, data)
        except Exception as e:
            logger.error(f"Send failed: {e}")
            raise

    def _notification_handler(self, sender, data: bytearray) -> None:
        """Handle incoming data from Bittle."""
        try:
            message = data.decode("utf-8").strip()
            if message:
                logger.debug(f"Received: {message}")
        except Exception as e:
            logger.warning(f"Failed to decode response: {e}")


class MockBittleConnection(BittleConnection):
    """Mock connection for testing without hardware."""

    async def connect(self, address: str) -> bool:
        if self._connected:
            await self.disconnect()
        logger.info(f"[MOCK] Connected to {address}")
        self._address = address
        self._connected = True
        self._client = object()  # sentinel so is_connected returns True
        return True

    async def disconnect(self) -> None:
        logger.info("[MOCK] Disconnected")
        self._client = None
        self._connected = False

    async def send(self, command: str) -> None:
        if not self._connected or not self._client:
            raise RuntimeError("Not connected to Bittle")
        logger.info(f"[MOCK] Sent: {command}")

    async def scan(self, timeout: float = 10.0) -> list[dict]:
        logger.info("[MOCK] Scanning...")
        return [{"name": "MockBittle", "address": "00:00:00:00:00:00"}]
