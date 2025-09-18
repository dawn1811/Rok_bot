from tkinter import Frame, Label, Entry, Button, LabelFrame
from tkinter import N, W, LEFT, CENTER
from gui.selected_device_frame import SelectedDeviceFrame
from gui.creator import write_device_config, load_device_config
import adb
import re
import traceback



RUNNING = "running"
DISCONNECTED = "disconnected"
CONNECTED = "connected"


class DeviceListFrame(Frame):

    def __init__(self, notebook, main_frame, cnf={}, **kwargs):
        Frame.__init__(self, notebook, kwargs)
        self.windows_size = [kwargs["width"], kwargs["height"]]

        self.devices_config = load_device_config()

        self.main_frame = main_frame
        self.adb_client, _ = adb.enable_adb(device_id="emulator-5554") 
        adf = AddDeviceFrame(self, main_frame)
        dlt = DeviceListTable(self, main_frame, adb_client=self.adb_client) 

        for config in self.devices_config:
            dlt.add_row(
                config.get("name", "None"), config["ip"], config["port"], self.adb_client
            )

        adf.set_on_add_click(
            lambda name, ip, port: dlt.add_row(name, ip, port, self.adb_client)
        )
        adf.grid(row=0, column=0, pady=(10, 0), sticky=N + W)
        dlt.grid(row=1, column=0, pady=(10, 0), sticky=N + W)


class DeviceListTable(Frame):
    def __init__(self, parent, main_frame, adb_client, cnf={}, **kwargs):  
        Frame.__init__(self, parent, kwargs)
        self.main_frame = main_frame
        self.adb_client = adb_client
        self.title = Label(self, text="Devices:")
        self.title.grid(row=0, column=0, sticky=W, padx=(5, 0))
        self.device_rows = []

    def add_row(self, name, ip, port, adb_client):
        try:
            new_row = DeviceRow(self, self.main_frame, name, ip, port, adb_client)
            new_row.set_on_display_click(self.on_display_click)
            new_row.set_on_del_click(self.on_delete_click)
            self.device_rows.append(new_row)
            self.render()

        except Exception as e:
            traceback.print_exc()
            return

    
    def render(self):
        for i in range(len(self.device_rows)):
            self.device_rows[i].grid(
                row=i + 1, column=0, sticky=W, padx=(10, 0), pady=(10, 0)
            )


class DeviceRow(Frame):
    def __init__(self, device_list_table, main_frame, name, ip, port, adb_client, cnf={}, **kwargs): # fixed comma
        Frame.__init__(self, device_list_table, kwargs)
        self.main_frame = main_frame
        self.name = name
        self.ip = ip
        self.port = port

        self.device = adb_client.connect_to_device(f"{ip}:{port}")
        self.device_frame = None

        
    def set_on_display_click(self, on_click=lambda self: self):
        def callback():
            device = adb_client.connect_to_device(f"{self.ip}:{self.port}")
            if device is None:
                return
            if self.device_frame is None:

                width, height = self.master.master.windows_size
                self.device_frame = SelectedDeviceFrame(
                    self.main_frame, device, width=width, height=height, adb_client=adb_client # added missing adb_client parameter
                )
                self.device_frame.grid(row=0, column=0, sticky=N + W)
                self.device_frame.grid_forget()
            on_click(self)

        self.display_btn.config(command=callback)