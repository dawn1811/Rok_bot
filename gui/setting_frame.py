from tkinter import (
    Frame, OptionMenu, StringVar, Label, Entry, LabelFrame,
    N, W, LEFT
)

from gui.creator import button          # if you still use it elsewhere
from config import write_config, HAO_I, TWO_CAPTCHA, NONE
import config


class SettingFrame(Frame):
    """Settings tab – lets the user choose screen size and CAPTCHA keys."""

    def __init__(self, master, **kwargs):
        # Proper keyword expansion:
        super().__init__(master, **kwargs)

        self.window_size = [kwargs.get("width", 470), kwargs.get("height", 450)]

        # Build sub-frames
        rows = [
            self._windows_resize_row(),
            self._option_row(),
            self._twocaptcha_row(),
            self._haoi_row(),
        ]

        # Grid them vertically with padding
        for r, widget in enumerate(rows):
            widget.grid(row=r, column=0, sticky=N + W, padx=10, pady=(10, 0))

    # ──────────────────────────────────────────────────────────────
    # 1) Pass-verification method dropdown
    # ──────────────────────────────────────────────────────────────
    def _option_row(self):
        f = Frame(self)

        Label(f, text="Pass Verification Method: ").grid(row=0, column=0, sticky=W)

        options  = [NONE, TWO_CAPTCHA, HAO_I]
        variable = StringVar(value=config.global_config.method)

        def on_select(val):
            config.global_config.method = val
            write_config(config.global_config)

        OptionMenu(f, variable, *options, command=on_select).grid(row=0, column=1, sticky=N + W)
        return f

    # ──────────────────────────────────────────────────────────────
    # 2) haoi keys
    # ──────────────────────────────────────────────────────────────
    def _haoi_row(self):
        lf = LabelFrame(self, text="haoi")

        # user key
        StringVarUser = StringVar(value=config.global_config.haoiUser)
        EntryUser = Entry(
            lf, textvariable=StringVarUser, width=53,
            validate="key",
            validatecommand=(lf.register(self._validator("haoiUser")), "%P")
        )
        Label(lf, text="user key:", width=10, anchor=W, justify=LEFT).grid(row=0, column=0, padx=(10,10), pady=(10,0))
        EntryUser.grid(row=0, column=1, padx=(0,10), pady=(10,0), sticky=N + W)

        # software key
        StringVarSoft = StringVar(value=config.global_config.haoiRebate)
        EntrySoft = Entry(
            lf, textvariable=StringVarSoft, width=53,
            validate="key",
            validatecommand=(lf.register(self._validator("haoiRebate")), "%P")
        )
        Label(lf, text="software key:", width=10, anchor=W, justify=LEFT).grid(row=1, column=0, padx=(10,10), pady=(0,10))
        EntrySoft.grid(row=1, column=1, padx=(0,10), pady=(0,10), sticky=N + W)

        return lf

    # ──────────────────────────────────────────────────────────────
    # 3) 2captcha key
    # ──────────────────────────────────────────────────────────────
    def _twocaptcha_row(self):
        lf = LabelFrame(self, text="2captcha")

        StringVarKey = StringVar(value=config.global_config.twocaptchaKey)
        EntryKey = Entry(
            lf, textvariable=StringVarKey, width=53,
            validate="key",
            validatecommand=(lf.register(self._validator("twocaptchaKey")), "%P")
        )
        Label(lf, text="user key:", width=10, anchor=W, justify=LEFT).grid(row=0, column=0, padx=(10,10), pady=(10,10))
        EntryKey.grid(row=0, column=1, padx=(0,10), pady=(10,10), sticky=N + W)

        return lf

    # ──────────────────────────────────────────────────────────────
    # 4) Window-size dropdown
    # ──────────────────────────────────────────────────────────────
    def _windows_resize_row(self):
        f = Frame(self)

        Label(f, text="Window Size (Restart to apply): ").grid(row=0, column=0, sticky=W)

        options = ["470 x 450", "470 x 550", "470 x 650", "470 x 750", "470 x 850"]
        current = f"{config.global_config.screenSize[0]} x {config.global_config.screenSize[1]}"
        variable = StringVar(value=current)

        def on_select(val):
            w, h = map(str.strip, val.split("x"))
            config.global_config.screenSize = [int(w), int(h)]
            write_config(config.global_config)

        OptionMenu(f, variable, *options, command=on_select).grid(row=0, column=1, sticky=N + W)
        return f

    # ──────────────────────────────────────────────────────────────
    # Helper – validator for any text Entry that writes to config
    # ──────────────────────────────────────────────────────────────
    @staticmethod
    def _validator(attr_name):
        def validate(value):
            if value != getattr(config.global_config, attr_name):
                setattr(config.global_config, attr_name, value)
                write_config(config.global_config)
            return True
        return validate
