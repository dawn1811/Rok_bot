import subprocess
import traceback
from ppadb.client import Client as PPADBClient
from utils import resource_path
from utils import build_command
from filepath.file_relative_paths import FilePaths

class Adb:
    def __init__(self, host="127.0.0.1", port=5037):
        self.client = PPADBClient(host, port)

def start_adb_server():
    try:
        subprocess.run([Adb, "start-server"], check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error starting ADB server: {e}") from e

def connect_to_device(self, device_id):
        try:
            device = self.client.device(device_id)
            if device is None:
                raise RuntimeError(f"Could not connect to device: {device_id}")
            return device
        except RuntimeError as e:
            traceback.print_exc()
            return None

def get_client_devices(self):
        return self.client.devices()

def enable_adb(host="127.0.0.1", port=5037, device_id="emulator-5554"):
    adb_path = resource_path(FilePaths.ADB_EXE_PATH.value)
    try:
        subprocess.run([adb_path, "start-server"], check=True, capture_output=True, text=True)
        adb = Adb(host, port)
        if adb.client.version() != 41:
            raise RuntimeError(f"Error: ADB version 41 required, but found {adb.client.version()}")
        device = adb.connect_to_device(device_id)
        if device is None:
            raise RuntimeError(f"Could not connect to device: {device_id}")
        return adb, device

    except (RuntimeError, subprocess.CalledProcessError) as e:
        traceback.print_exc()
        raise RuntimeError(f"Error initializing ADB: {e}") from e
