from bot import Bot
from filepath.file_relative_paths import ImagePathAndProps
from gui.main_window import MainWindow  # Only if still needed

import os


def verify_template_paths():
    missing = []
    for entry in ImagePathAndProps:
        if not os.path.exists(entry.value):
            missing.append(entry.value)
    if missing:
        print("❌ Missing template files:")
        for path in missing:
            print("  -", path)
    else:
        print("✅ All template files found.")


def main():
    # Step 1: Check that all GUI image templates exist
    verify_template_paths()

    # Step 2: Start bot and GUI
    bot = Bot(config={})
    gui = MainWindow(bot=bot)  # If your PC version of MainWindow accepts a bot instance
    gui.run()


if __name__ == "__main__":
    main()
