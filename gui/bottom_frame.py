from tkinter import Frame, Label, N, W
import webbrowser
import threading

from utils import get_last_info
from version import version

GITHUB_URL = "https://github.com/yuceltoluyag/Rise-of-Kingdoms-Bot"


class BottomFrame(Frame):
    """Bottom bar for version info and update link."""

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = Label(self, text="Welcome to use Rise of Kingdoms Bot, see update on")
        self.link  = Label(self, text="GitHub", fg="blue", cursor="hand2")

        self.label.grid(row=0, column=0, sticky=N + W)
        self.link.grid(row=0, column=1, sticky=N + W)

        self.link.bind("<Button-1>", lambda e: webbrowser.open_new(GITHUB_URL))

        # Load update message asynchronously
        threading.Thread(target=self._check_updates, daemon=True).start()

    def _check_updates(self):
        try:
            info = get_last_info()
            latest_version = info.get("version", version)

            # Show version notice if available
            if latest_version > version:
                self.label.config(text=f"There is a new version {latest_version}, download at")
                return

            if info.get("shouldUpdateInfo"):
                label_info = info.get("label", {})
                if label_info.get("update"):
                    self.label.config(text=label_info.get("text", self.label.cget("text")))
                    self.label.grid(row=label_info.get("row", 0), column=label_info.get("column", 0))
                else:
                    self.label.grid_forget()

                link_info = info.get("link", {})
                if link_info.get("update"):
                    self.link.config(text=link_info.get("text", self.link.cget("text")))
                    self.link.bind(
                        "<Button-1>",
                        lambda e: webbrowser.open_new(info.get("url", GITHUB_URL)),
                    )
                    self.link.grid(row=link_info.get("row", 0), column=link_info.get("column", 1))
                else:
                    self.link.grid_forget()

        except Exception as e:
            print(f"[BottomFrame] Failed to check updates: {e}")
