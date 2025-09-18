import threading
import sys
import os
from tkinter import Tk, N, W, END, Text, VERTICAL, Y, RIGHT, BOTH
from tkinter.ttk import Notebook, Frame, Button, Scrollbar, Label

from gui.setting_frame import SettingFrame          # keeps your old settings UI
from gui.bottom_frame import BottomFrame            # keeps your bottom status bar
from config import load_config
from bot_related import twocaptcha, haoi
from version import version
import config


# ────────────────────────────────────────────────
#  A simple frame that lets the user start/stop
#  the bot and shows its live text feed.
# ────────────────────────────────────────────────
class BotControlFrame(Frame):
    def __init__(self, master, bot, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.bot = bot

        # ---------- Buttons ----------
        self.start_btn = Button(self, text="Start Bot", command=self.start_bot)
        self.stop_btn  = Button(self, text="Stop Bot",  command=self.stop_bot, state="disabled")
        self.start_btn.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.stop_btn.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # ---------- Log output ----------
        self.log_box = Text(self, width=100, height=35, state="disabled", wrap="none")
        sb_y = Scrollbar(self, orient=VERTICAL, command=self.log_box.yview)
        self.log_box.configure(yscrollcommand=sb_y.set)

        self.log_box.grid(row=1, column=0, columnspan=2, sticky=N+W)
        sb_y.grid(row=1, column=2, sticky=N+W+Y)

        # Feed bot text updates here
        self.bot.text_update_event = self.update_log

    # ---- Button callbacks ---------------------------------------------------
    def start_bot(self):
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")

        # Launch the bot in a background thread so the UI stays responsive
        threading.Thread(target=lambda: self.bot.start(self.bot.do_task), daemon=True).start()
        self.update_log({"title": "Bot started", "text_list": []})

    def stop_bot(self):
        self.bot.stop()
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.update_log({"title": "Bot stopped", "text_list": []})

    # ---- Log rendering ------------------------------------------------------
    def update_log(self, text_dict):
        self.log_box.configure(state="normal")
        self.log_box.delete(1.0, END)

        title = text_dict.get("title", "")
        if title:
            self.log_box.insert(END, f"{title}\n{'=' * len(title)}\n\n")

        for line in text_dict.get("text_list", []):
            self.log_box.insert(END, line + "\n")

        self.log_box.configure(state="disabled")
        self.log_box.see(END)   # auto-scroll


# ────────────────────────────────────────────────
#  MainWindow – now PC-native, no ADB needed
# ────────────────────────────────────────────────
class MainWindow:
    def __init__(self, bot):
        # ── global config / captcha keys ────────────────────────────────────
        config.global_config = load_config()
        twocaptcha.key       = config.global_config.twocaptchaKey
        haoi.userstr         = config.global_config.haoiUser
        haoi.rebate          = config.global_config.haoiRebate

        # ── basic window setup ─────────────────────────────────────────────
        self.window = Tk()
        self.size   = config.global_config.screenSize

        self.window.title(f"Rise Of Kingdoms Bot (PC)  {version}")
        self.window.geometry(f"{self.size[0]}x{self.size[1]}")
        self.window.resizable(False, False)

        # ── notebook with tabs ─────────────────────────────────────────────
        notebook = Notebook(self.window, height=self.size[1] - 80)
        notebook.grid(row=0, column=0, sticky=N + W, pady=(10, 0))

        # Tab 1: Bot control & live log
        bot_frame = BotControlFrame(notebook, bot,
                                    width=self.size[0], height=self.size[1])
        bot_frame.grid_propagate(False)
        notebook.add(bot_frame, text="Bot Control")

        # Tab 2: Settings (reuse your old SettingFrame)
        setting_frame = SettingFrame(notebook,
                                     width=self.size[0], height=self.size[1])
        setting_frame.grid(row=0, column=0, sticky=N + W)
        setting_frame.grid_propagate(False)
        notebook.add(setting_frame, text="Settings")

        # ── bottom status bar (reuse) ──────────────────────────────────────
        bottom = BottomFrame(self.window,
                             width=self.size[0], height=self.size[1])
        bottom.grid(row=1, column=0, sticky=N + W, padx=10, pady=(10, 0))

    # -----------------------------------------------------------------------
    def run(self):
        self.window.mainloop()
