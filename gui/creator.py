import os
import traceback
import json
from tkinter import (
    Button, BooleanVar, Checkbutton, Label, StringVar, Frame,
    OptionMenu, Entry, TRUE, FALSE, N, W, LEFT
)

from utils import resource_path
from bot_related.bot_config import BotConfig
from filepath.file_relative_paths import FilePaths


# ──────────────── SAVE PATH SETUP ────────────────
def ensure_save_folder_exists():
    save_folder_path = resource_path(FilePaths.SAVE_FOLDER_PATH.value)
    if not os.path.exists(save_folder_path):
        os.makedirs(save_folder_path)


# ──────────────── BUTTON FACTORY ────────────────
def button(frame, on_click=lambda v: v, **kwargs):
    btn = Button(frame, **kwargs)

    def command():
        on_click(btn)

    btn.config(command=command)
    return btn


# ──────────────── CHECKBOX FACTORY ────────────────
def checkbox_fn_creator(name, text):
    def title_checkbox(app, parent, on_click=lambda v: v):
        variable = BooleanVar()
        variable.set(TRUE if getattr(app.bot_config, name) else FALSE)

        def command():
            setattr(app.bot_config, name, variable.get())
            write_bot_config(app.bot_config, prefix="pc_bot")
            on_click(variable.get())

        checkbox = Checkbutton(
            parent, text=text, variable=variable, command=command
        )
        return checkbox, variable

    return title_checkbox


# ──────────────── ENTRY FACTORY ────────────────
def entry_int_fn_creator(name, begin_text, end_text=None):
    def entry(app, parent):
        str_value = StringVar()
        str_value.set(str(getattr(app.bot_config, name)))

        frame = Frame(parent)
        label = Label(frame, text=begin_text)
        entry = Entry(frame, textvariable=str_value)

        def creator(attr_name):
            def validate_cmd(value, action_type):
                if action_type == "1":
                    if not value.isdigit() or value.startswith("0"):
                        return False
                setattr(app.bot_config, attr_name, int(value or "1"))
                write_bot_config(app.bot_config, prefix="pc_bot")
                return True
            return validate_cmd

        entry.config(
            width=10,
            validate="key",
            validatecommand=(frame.register(creator(name)), "%P", "%d"),
        )

        label.grid(row=0, column=0, sticky=N + W, padx=5)
        entry.grid(row=0, column=1, sticky=N + W, padx=5)

        if end_text is not None:
            Label(frame, text=end_text).grid(row=0, column=2, sticky=N + W, padx=5)

        return frame, None
    return entry


# ──────────────── TRAINING SELECTOR FACTORY ────────────────
def train_fn_creator(name, train_attr_name, upgrade_attr_name):
    lv_training_options = ["1", "2", "3", "4", "5", "Disabled"]
    lv_upgrade_options = ["1", "2", "3", "4", "5", "All", "Disabled"]

    def num_to_option_value(num):
        return str(num + 1) if 0 <= num <= 4 else "All" if num == 5 else "Disabled"

    def option_value_to_num(v):
        return int(v) - 1 if v.isdigit() else (5 if v == "All" else -1)

    def train(app, parent):
        frame = Frame(parent)
        name_tag = Label(frame, text=name)

        # Upgrade dropdown
        def update_command(v):
            setattr(app.bot_config, upgrade_attr_name, option_value_to_num(v))
            write_bot_config(app.bot_config, prefix="pc_bot")

        upgrade_label = Label(frame, text="Upgrade Lv.")
        upgrade_variable = StringVar(value=num_to_option_value(getattr(app.bot_config, upgrade_attr_name)))
        upgrade_option = OptionMenu(frame, upgrade_variable, *lv_upgrade_options, command=update_command)

        # Training dropdown
        def train_command(v):
            setattr(app.bot_config, train_attr_name, option_value_to_num(v))
            write_bot_config(app.bot_config, prefix="pc_bot")

        train_label = Label(frame, text="Training Lv.")
        train_variable = StringVar(value=num_to_option_value(getattr(app.bot_config, train_attr_name)))
        train_option = OptionMenu(frame, train_variable, *lv_training_options, command=train_command)

        name_tag.config(width=8, anchor=N + W, justify=LEFT)
        upgrade_option.config(width=8)
        train_option.config(width=8)

        frame.columnconfigure(0, weight=5)
        name_tag.grid(row=0, column=0)
        train_label.grid(row=0, column=2)
        train_option.grid(row=0, column=3)
        upgrade_label.grid(row=0, column=4)
        upgrade_option.grid(row=0, column=5)

        return frame, None

    return train


# ──────────────── FILE I/O (PC-native) ────────────────
def load_bot_config(prefix):
    try:
        ensure_save_folder_exists()
        config_file_path = resource_path(FilePaths.SAVE_FOLDER_PATH.value + f"{prefix}_config.json")
        if not os.path.exists(config_file_path):
            config = BotConfig()
            write_bot_config(config, prefix)
        else:
            with open(config_file_path) as f:
                config_dict = json.load(f)
                config = BotConfig(config_dict)
    except Exception:
        traceback.print_exc()
        config = BotConfig()
    return config


def write_bot_config(config, prefix):
    with open(
        resource_path(FilePaths.SAVE_FOLDER_PATH.value + f"{prefix}_config.json"),
        "w",
    ) as f:
        json.dump(config.__dict__, f, indent=2)


def load_building_pos(prefix):
    try:
        ensure_save_folder_exists()
        path = resource_path(FilePaths.SAVE_FOLDER_PATH.value + f"{prefix}_building_pos.json")
        if not os.path.exists(path):
            building_pos = {}
            write_building_pos(building_pos, prefix)
        else:
            with open(path) as f:
                building_pos = json.load(f)
    except Exception:
        traceback.print_exc()
        building_pos = {}
    return building_pos


def write_building_pos(building_pos, prefix):
    with open(
        resource_path(FilePaths.SAVE_FOLDER_PATH.value + f"{prefix}_building_pos.json"),
        "w",
    ) as f:
        json.dump(building_pos, f, indent=2)
