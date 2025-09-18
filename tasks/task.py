from bot_related.device_gui_detector import GuiName, GuiDetector
from bot_related.bot_config import TrainingAndUpgradeLevel, BotConfig
from bot_related import haoi, twocaptcha
from bot_related import aircve as aircv
from config import HAO_I, TWO_CAPTCHA
from filepath.file_relative_paths import (
    GuiCheckImagePathAndProps,
    ImagePathAndProps,
    BuffsImageAndProps,
    ItemsImageAndProps,
)
from datetime import datetime, timedelta
from utils import aircv_rectangle_to_box, stop_thread, resource_path
from enum import Enum

import config
import traceback
import time
import os
import shutil
import cv2
import numpy as np
import random


from filepath.constants import (
    RESOURCES,
    SPEEDUPS,
    BOOSTS,
    EQUIPMENT,
    OTHER,
    MAP,
    HOME,
    WINDOW,
    GREEN_HOME,
)
from random import randrange, uniform


class Task:
    center = (640, 360)

    def __init__(self, bot):
        self.bot = bot
        self.device = bot.device
        self.gui = bot.gui
        self.debug_mode = False  # Debug mode is off by default

        # Debug settings
        self.debug_dir = "debug_images"


        # Initialize debug mode based on configuration file
        try:
            print("Debug: Starting bot, checking debug folder...")
            self.clean_debug_directory_completely()  # Ensure clean debug folder on start
            config_file_path = None

            if hasattr(self.bot.device, "save_file_prefix"):
                config_file_path = resource_path(
                    FilePaths.SAVE_FOLDER_PATH.value
                    + "{}_config.json".format(self.bot.device.save_file_prefix)
                )
                print(f"Debug: Configuration file: {config_file_path}")

            if config_file_path and os.path.exists(config_file_path):
                with open(config_file_path) as f:
                    config_dict = json.load(f)
                    self.debug_mode = config_dict.get("debug_mode", False)
                    print(f"Debug: debug_mode from configuration file: {self.debug_mode}")
            elif hasattr(self.bot, "config") and hasattr(self.bot.config, "debug_mode"):
                self.debug_mode = self.bot.config.debug_mode
                print(f"Debug: debug_mode from bot config: {self.debug_mode}")

            if self.debug_mode:
                print("Debug: Debug mode enabled")
                if hasattr(self.gui, "debug"):
                    self.gui.debug = True
        except Exception as e:
            print(f"Debug: Error initializing debug mode: {str(e)}")
            traceback.print_exc()
            self.debug_mode = False



    def to_ascii(self, text):
        """Converts Turkish characters to ASCII characters."""
        char_map = {
            "ç": "c", "Ç": "C", "ğ": "g", "Ğ": "G", "ı": "i", "İ": "I",
            "ö": "o", "Ö": "O", "ş": "s", "Ş": "S", "ü": "u", "Ü": "U"
        }
        return "".join(char_map.get(c, c) for c in text)


    def call_idle_back(self):
        """Calls back idle commander."""
        self.set_text(insert="Calling back idle commander")
        self.back_to_map_gui()
        while True:
            _, _, commander_pos = self.gui.check_any(
                ImagePathAndProps.HOLD_ICON_SMALL_IMAGE_PATH.value
            )
            if commander_pos:
                x, y = commander_pos
                self.tap(x - 10, y - 10, 2)
                x, y = self.center
                self.tap(x, y)
                self.tap(x, y, 1)
            else:
                return
            _, _, return_btn_pos = self.gui.check_any(
                ImagePathAndProps.RETURN_BUTTON_IMAGE_PATH.value
            )
            if return_btn_pos:
                x, y = return_btn_pos
                self.tap(x, y, 1)
            else:
                return

    def heal_troops(self):
        """Heals troops in the hospital."""
        self.set_text(insert="Healing Troops")
        heal_button_pos = (960, 590)
        self.back_to_home_gui()
        self.home_gui_full_view()
        self.tap(
            self.bot.building_pos["hospital"][0],
            self.bot.building_pos["hospital"][1],
            2,
        )
        self.tap(285, 20, 0.5)
        _, _, heal_icon_pos = self.gui.check_any(
            ImagePathAndProps.HEAL_ICON_IMAGE_PATH.value
        )
        if not heal_icon_pos:
            return
        self.tap(heal_icon_pos[0], heal_icon_pos[1], 2)
        self.tap(heal_button_pos[0], heal_button_pos[1], 2)
        self.tap(
            self.bot.building_pos["hospital"][0],
            self.bot.building_pos["hospital"][1],
            2,
        )
        self.tap(
            self.bot.building_pos["hospital"][0],
            self.bot.building_pos["hospital"][1],
            2,
        )

    def back_to_home_gui(self):
        """Navigates back to the home GUI."""
        loop_count = 0
        while True:
            result = self.get_curr_gui_name()
            gui_name, info = ["UNKNOW", None] if result is None else result
            if gui_name == GuiName.HOME.name:
                break
            elif gui_name == GuiName.MAP.name:
                x_pos, y_pos = info
                self.tap(x_pos, y_pos)
            elif gui_name == GuiName.WINDOW.name:
                self.back(1)
            else:
                self.back(1)
            loop_count += 1
            time.sleep(0.5)
        return loop_count


    def find_home(self):
        """Finds and taps the green home button if available"""
        has_green_home, _, pos = self.gui.check_any(
            ImagePathAndProps.GREEN_HOME_BUTTON_IMG_PATH.value
        )
        if has_green_home:
            x, y = pos
            self.tap(x, y, 2)


    def home_gui_full_view(self):
        """Adjusts the view on the home screen for better visibility."""
        self.tap(60, 540, 0.5)
        self.tap(1105, 200, 1)
        self.tap(1220, 35, 2)
        self.tap(43, 37, 3)
        self.tap(42, 38, 3)


    def find_building_title(self):
        """Locates the building title mark on the screen."""
        result = self.gui.has_image_props(
            ImagePathAndProps.BUILDING_TITLE_MARK_IMG_PATH.value
        )
        if result:
            return aircv_rectangle_to_box(result["rectangle"])
        return None

    def menu_should_open(self, should_open=False):
        """Opens or closes the menu based on the should_open flag."""
        (
            path,
            size,
            box,
            threshold,
            least_diff,
            gui,
        ) = ImagePathAndProps.MENU_BUTTON_IMAGE_PATH.value
        x0, y0, x1, y1 = box
        c_x, c_y = x0 + (x1 - x0) / 2, y0 + (y1 - y0) / 2
        is_open, _, _ = self.gui.check_any(
            ImagePathAndProps.MENU_OPENED_IMAGE_PATH.value
        )
        if should_open and not is_open:
            self.tap(c_x, c_y, 0.5)
        elif not should_open and is_open:
            self.tap(c_x, c_y, 0.5)


    def back_to_map_gui(self):
        """Navigates back to the map GUI."""
        loop_count = 0
        while True:
            result = self.get_curr_gui_name()
            gui_name, pos = ["UNKNOW", None] if result is None else result
            if gui_name == GuiName.MAP.name:
                break
            elif gui_name == GuiName.HOME.name:
                x_pos, y_pos = pos
                self.tap(x_pos, y_pos)
            elif gui_name == GuiName.WINDOW.name:
                self.back(1)
            else:
                self.back(1)
            loop_count += 1
            time.sleep(0.5)
        return loop_count


    def get_curr_gui_name(self):
        """Gets the current GUI name."""
        if not self.isRoKRunning():
            self.set_text(insert="Game is not running, trying to start it")
            self.runOfRoK()
            start = time.time()
            while time.time() - start <= 300 and self.isRoKRunning():
                result = self.gui.get_curr_gui_name()
                if result:
                    return result
                time.sleep(5)
            return None # Return None if the game doesn't start within the timeout



        for _ in range(2):  # Retry a few times
            result = self.gui.get_curr_gui_name()
            gui_name, _ = ["UNKNOW", None] if result is None else result

            # Check and handle verification screens
            if gui_name in (
                GuiName.VERIFICATION_VERIFY.name,
                GuiName.VERIFICATION_CHEST.name,
                GuiName.VERIFICATION_CHEST1.name,
            ):
                self.check_captcha() # Use check_captcha instead of check_capcha
            else:
                return result



    def pass_verification(self):
        """Handles the verification process (captcha)."""
        try:
            self.set_text(insert="Passing verification")
            box = (400, 70, 880, 625)
            ok = [780, 680] # This variable is not used
            img = self.gui.get_curr_device_screen_img()
            img = img.crop(box)

            if config.global_config.method == HAO_I:
                pos_list = haoi.solve_verification(img)
            elif config.global_config.method == TWO_CAPTCHA:
                pos_list = twocaptcha.solve_verification(img)
            else: # Handle cases where method is not defined.
                self.set_text(insert="Error: Unrecognized Captcha Method")
                return None

            if pos_list is None:
                self.set_text(insert="Failed to pass verification")
                return None

            for pos in pos_list:
                self.tap(400 + pos[0], pos[1] + 70, 1)
            self.tap(randrange(700, 800), randrange(565, 605), 5) # This tap was outside the captcha area

        except Exception as e:
            self.tap(100, 100) #  Why tap at (100, 100) on error? This seems arbitrary.
            traceback.print_exc()
        return pos_list


    def check_captcha(self):
        """Checks and solves CAPTCHA. Always operates without debug mode."""

        original_debug_mode = self.debug_mode
        self.debug_mode = False

        try:
            for title_path in (
                 ImagePathAndProps.VERIFICATION_VERIFY_TITLE_IMAGE_PATH.value,
                 ImagePathAndProps.VERIFICATION_VERIFY_BUTTON_IMAGE_PATH.value,
            ):
                found, _, pos = self.gui.check_any(title_path)
                if found:
                    self.set_text(insert="CAPTCHA verification screen detected")
                    self.tap(pos[0], pos[1] + 258 if title_path == ImagePathAndProps.VERIFICATION_VERIFY_TITLE_IMAGE_PATH.value else pos[1], 1)
                    time.sleep(5)
                    self.pass_verification()
                    return  # Exit after handling

            found, _, pos = self.gui.check_any(
                GuiCheckImagePathAndProps.VERIFICATION_CHEST_IMG_PATH.value,
                GuiCheckImagePathAndProps.VERIFICATION_CHEST1_IMG_PATH.value,
            )
            if found:
                self.set_text(insert="CAPTCHA chest detected")
                self.tap(pos[0], pos[1], 1)
                time.sleep(5)
                self.pass_verification()


        finally:
            self.debug_mode = original_debug_mode




    def has_buff(self, checking_location, buff_img_props):
        """Checks if a buff is active."""
        if checking_location == HOME:
            self.back_to_home_gui()
        elif checking_location == MAP:
            self.back_to_map_gui()
        else:
            return False
        has, _, _ = self.gui.check_any(buff_img_props)
        return has

    def use_item(self, using_location, item_img_props_list):
        """Uses an item from inventory."""
        if using_location == HOME:
            self.back_to_home_gui()
        elif using_location == MAP:
            self.back_to_map_gui()
        else:
            return False

        items_icon_pos = (930, 675)
        use_btn_pos = (980, 600)
        tabs_pos = {
            RESOURCES: (250, 80),
            SPEEDUPS: (435, 80),
            BOOSTS: (610, 80),
            EQUIPMENT: (790, 80),
            OTHER: (970, 80),
        }

        for item_img_props in item_img_props_list:
            path, size, box, threshold, least_diff, tab_name = item_img_props
            self.menu_should_open(True)  # Open menu
            self.tap(*items_icon_pos, 2)  # Open items window
            self.tap(*tabs_pos[tab_name], 1)  # Tap on the correct tab
            _, _, item_pos = self.gui.check_any(item_img_props) #check the item
            if item_pos: #if item is found
                self.tap(*item_pos, 0.5) #tap the item
                self.tap(*use_btn_pos)  # Tap "Use"
                return True #exit after using the item.

        return False



    def back(self, sleep_time=0.5):
        """Simulates the back button press."""
        cmd = "input keyevent 4"
        self.device.shell(cmd)
        time.sleep(sleep_time)


    def swipe(self, x_f, y_f, x_t, y_t, times=1, duration=300):
        """Swipes from one point to another."""
        cmd = f"input swipe {x_f} {y_f} {x_t} {y_t} {duration}"
        for _ in range(times):
            self.device.shell(cmd)
            time.sleep(duration / 1000 + 0.2)



    def zoom(self, x_f, y_f, x_t, y_t, times=1, duration=300, zoom_type="out"):
        """Zooms in or out."""
        cmd_hold = f"input swipe {x_t} {y_t} {x_t} {y_t} {duration + 50}"  # Hold at the end point
        cmd_swipe = f"input swipe {x_f} {y_t} {x_f} {y_t} {duration}" if zoom_type == "out" else f"input swipe {x_t} {y_t} {x_f} {y_f} {duration}"

        for _ in range(times):
            self.device.shell(cmd_hold)
            self.device.shell(cmd_swipe)
            time.sleep(duration / 1000 + 0.7)




    def move_map(self, direction="up"):
        """Moves the map view."""
        #duration of swipe is fixed at 200ms
        if direction == "down":
            cmd = "input swipe 200 300 200 200 200"
        elif direction == "right":
            cmd = "input swipe 200 300 100 300 200"
        elif direction == "left":
            cmd = "input swipe 200 300 300 300 200"
        else: # default is up
            cmd = "input swipe 200 300 200 400 200"


        self.device.shell(cmd)
        time.sleep(0.3)



    def tap(self, x, y, sleep_time=0.1, long_press_duration=-1):
        """Taps a specific coordinate on the screen."""
        if long_press_duration > -1:
            cmd = f"input swipe {x} {y} {x} {y} {long_press_duration}"
            sleep_time = long_press_duration / 1000 + 0.2
        else:
            cmd = f"input tap {x} {y}"

        self.device.shell(cmd)
        time.sleep(sleep_time)



    def isRoKRunning(self):
        """Checks if Rise of Kingdoms is running."""
        cmd = "dumpsys window windows | grep mCurrentFocus"
        output = self.device.shell(cmd)
        return "com.lilithgame.roc.gp/com.harry.engine.MainActivity" in output

    def runOfRoK(self):
        """Starts Rise of Kingdoms."""
        cmd = "am start -n com.lilithgame.roc.gp/com.harry.engine.MainActivity"
        self.device.shell(cmd)

    def stopRok(self):
        """Stops Rise of Kingdoms."""
        cmd = "am force-stop com.lilithgame.roc.gp"
        self.device.shell(cmd)

    def set_text(self, **kwargs):
        """Updates the text displayed in the bot's output."""
        dt_string = datetime.now().strftime("[%H:%M:%S]")
        title_key = "title"
        text_list_key = "text_list"
        insert_key = "insert"
        remove_key = "remove"
        replace_key = "replace"
        index_key = "index"
        append_key = "append"

        if title_key in kwargs:
            self.bot.text[title_key] = kwargs[title_key]
            print(kwargs[title_key])

        if replace_key in kwargs:
            index = kwargs.get(index_key, 0)  # Default index if not provided
            self.bot.text[text_list_key][index] = (
                f"{dt_string} {kwargs[replace_key].lower()}"
            )
            print(f"\t* {self.bot.text[text_list_key][index]}")

        if insert_key in kwargs:
            index = kwargs.get(index_key, 0)  # Default index if not provided
            self.bot.text[text_list_key].insert(
                index, f"{dt_string} {kwargs[insert_key].lower()}"
            )
            print(f"\t* {self.bot.text[text_list_key][index]}")


        if append_key in kwargs:
            self.bot.text[text_list_key].append(
                f"{dt_string} {kwargs[append_key].lower()}"
            )
            print(f"\t* {dt_string} {kwargs[append_key].lower()}")

        if remove_key in kwargs and kwargs.get(remove_key, False):
            self.bot.text[text_list_key].clear()

        self.bot.text_update_event(self.bot.text)


    def do(self, next_task):
        """Placeholder for task execution."""
        return next_task


    def enable_debug(self):
        """Enables debug mode."""
        self.debug_mode = True
        self.gui.debug = True # Update GuiDetector debug mode
        print("Debug mode enabled")

    def disable_debug(self):
        """Disables debug mode."""
        self.debug_mode = False
        self.gui.debug = False # Update GuiDetector debug mode
        print("Debug mode disabled")

    def toggle_debug(self):
        """Toggles debug mode."""
        self.debug_mode = not self.debug_mode
        self.gui.debug = self.debug_mode  # Sync with GuiDetector
        print(f"Debug mode {'enabled' if self.debug_mode else 'disabled'}")
        return self.debug_mode  # Return the new state




    def save_debug_image(self, prefix):
        """Saves a screenshot to the debug_images folder."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_prefix = "".join(
                c for c in prefix if c.isalnum() or c in "_-"
            )  # Sanitize filename
            filename = f"{safe_prefix}_{timestamp}.png"
            filepath = os.path.join(self.debug_dir, filename)

            os.makedirs(
                self.debug_dir, exist_ok=True
            )  # Create directory if it doesn't exist

            screen_img = self.gui.get_curr_device_screen_img_byte_array()
            with open(filepath, "wb") as f:
                f.write(screen_img)
            print(f"Debug: Screenshot saved: {filepath}")
            return filepath

        except Exception as e:
            print(f"Debug: Error saving screenshot: {str(e)}")
            traceback.print_exc()
            return None



    def create_reference_image(self, x, y, width, height, output_path):
        """Creates a reference image by cropping a region from a screenshot."""

        if not self.debug_mode:
            return False

        try:
            screen_img_bytes = self.gui.get_curr_device_screen_img_byte_array()
            nparr = np.frombuffer(screen_img_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            h, w = img.shape[:2]

            # Clamp coordinates to image boundaries
            x = max(0, min(x, w - 1))
            y = max(0, min(y, h - 1))
            width = max(1, min(width, w - x))
            height = max(1, min(height, h - y))


            cropped = img[y : y + height, x : x + width]

            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            cv2.imwrite(output_path, cropped)

            print(f"Debug: Reference image created: {output_path}")
            return True

        except Exception as e:
            print(f"Debug: Error creating reference image: {str(e)}")
            traceback.print_exc()
            return False



    def debug_image_match(self, image_path_and_props, screen_img=None):
        """Shows debug information for image matching and optionally saves images."""
        if not self.debug_mode:
            return self.gui.check_any(image_path_and_props)

        try:
            if screen_img is None:
                screen_img = self.gui.get_curr_device_screen_img_byte_array()

            np_arr = np.frombuffer(screen_img, np.uint8)
            screen_cv_img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            path, size, box, threshold, least_diff, gui = image_path_and_props
            ref_img_path = resource_path(path)
            ref_cv_img = cv2.imread(ref_img_path)

            if ref_cv_img is None:
                print(f"Debug: Could not load reference image: {path}")
                return False, None, None


            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            image_name = os.path.basename(path).split(".")[0]

            screen_debug_path = os.path.join(
                self.debug_dir, f"screen_{image_name}_{timestamp}.png"
            )
            ref_debug_path = os.path.join(
                self.debug_dir, f"ref_{image_name}_{timestamp}.png"
            )

            cv2.imwrite(screen_debug_path, screen_cv_img)
            cv2.imwrite(ref_debug_path, ref_cv_img)

            result = aircv.find_template(ref_cv_img, screen_cv_img, threshold)


            print(f"Debug: Image Matching - {os.path.basename(path)}")
            print(f"Debug: Reference Image Size: {ref_cv_img.shape}")
            print(f"Debug: Screen Image Size: {screen_cv_img.shape}")
            print(f"Debug: Match Threshold: {threshold}")

            if result:
                confidence = result["confidence"]
                match_pos = result["result"]
                print(f"Debug: Match Found - Position: {match_pos}")
                print(f"Debug: Match Confidence: {confidence}")


                match_x, match_y = match_pos
                h, w = ref_cv_img.shape[:2]
                top_left = (int(match_x - w / 2), int(match_y - h / 2))
                bottom_right = (int(match_x + w / 2), int(match_y + h / 2))


                result_img = screen_cv_img.copy() # make a copy before modifying it
                cv2.rectangle(result_img, top_left, bottom_right, (0, 255, 0), 2)
                cv2.circle(result_img, (int(match_x), int(match_y)), 5, (0, 0, 255), -1)



                result_debug_path = os.path.join(
                    self.debug_dir, f"match_{image_name}_{timestamp}.png"
                )
                cv2.imwrite(result_debug_path, result_img)
                print(f"Debug: Match image saved: {result_debug_path}")

                return True, gui, match_pos

            else:
                print("Debug: No Match Found")


                h1, w1 = ref_cv_img.shape[:2]
                h2, w2 = screen_cv_img.shape[:2]
                if abs(h1 / h2 - 1) > 0.2 or abs(w1 / w2 - 1) > 0.2:
                    print("Debug: Size difference detected.")

                # Check color similarity using histograms (you can add more sophisticated checks here)
                ref_hsv = cv2.cvtColor(ref_cv_img, cv2.COLOR_BGR2HSV)
                screen_hsv = cv2.cvtColor(screen_cv_img, cv2.COLOR_BGR2HSV)
                ref_hist = cv2.calcHist([ref_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
                screen_hist = cv2.calcHist([screen_hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
                cv2.normalize(ref_hist, ref_hist, 0, 1, cv2.NORM_MINMAX)
                cv2.normalize(screen_hist, screen_hist, 0, 1, cv2.NORM_MINMAX)

                color_similarity = cv2.compareHist(ref_hist, screen_hist, cv2.HISTCMP_CORREL)
                print(f"Debug: Color similarity: {color_similarity:.2f}")
                if color_similarity < 0.5:
                     print("Debug: Significant color difference detected.")



                # Threshold Suggestion:
                print(f"Debug: Current threshold: {threshold}")
                if threshold > 0.7:
                    print(f"Debug: Try a lower threshold value, e.g.: {threshold-0.1:.2f}")

                # Create and save a 'no match' debug image (you can customize this)
                no_match_img = screen_cv_img.copy()  # Create a copy to modify
                no_match_path = os.path.join(self.debug_dir, f"no_match_{image_name}_{timestamp}.png")
                cv2.imwrite(no_match_path, no_match_img)
                print(f"Debug: No-match image saved: {no_match_path}")



                return False, None, None

        except Exception as e:
            print(f"Debug: Error during image matching debug: {str(e)}")
            traceback.print_exc()
            return self.gui.check_any(image_path_and_props) # Fallback to regular check


    def debug_check_any(self, *props_list):
        """Performs debug image matching for multiple image properties."""
        if not self.debug_mode:
            return self.gui.check_any(*props_list)


        try:
            screen_img = self.gui.get_curr_device_screen_img_byte_array()
            start_time = time.time()

            for props in props_list:
                result = self.debug_image_match(props, screen_img)
                if result[0]: # If a match is found
                    elapsed_time = time.time() - start_time
                    print(f"Debug: Match time: {elapsed_time:.3f} seconds")
                    return result

            # If no match is found after checking all images:
            elapsed_time = time.time() - start_time
            print(f"Debug: No match found, total time: {elapsed_time:.3f} seconds")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            debug_img_path = os.path.join(self.debug_dir, f"no_match_any_{timestamp}.png")
            with open(debug_img_path, "wb") as f:
                f.write(screen_img)
            print(f"Debug: No-match image saved: {debug_img_path}")


            return False, None, None


        except Exception as e:
            print(f"Debug: Error in debug_check_any: {str(e)}")
            traceback.print_exc()
            return self.gui.check_any(*props_list)  # Fallback


    def clean_debug_directory_completely(self):
        """Completely cleans the debug directory."""
        try:
            if os.path.exists(self.debug_dir):

                file_count = 0 # Keep track of how many were deleted.
                for filename in os.listdir(self.debug_dir):
                    filepath = os.path.join(self.debug_dir, filename)
                    if os.path.isfile(filepath) or os.path.islink(filepath):
                        os.remove(filepath)
                        file_count += 1
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                print(f"Debug: All files removed. Total {file_count} were deleted.")

            os.makedirs(self.debug_dir, exist_ok=True)  # Recreate directory

        except Exception as e:
            print(f"Debug: Error while cleaning debug directory: {str(e)}")
            traceback.print_exc()