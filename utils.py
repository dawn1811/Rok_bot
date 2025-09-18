from filepath.file_relative_paths import FilePaths

import cv2
import pytesseract as tess
import sys
import os
import inspect
import ctypes
import requests
import json
import traceback
import pyautogui  # For PC screen interactions

def _async_raise(tid, exctype):
    """Raises an exception in a thread."""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
    """Stops a thread."""
    _async_raise(thread.ident, SystemExit)


def resource_path(relative_path):
    """Gets the absolute path to a resource."""
    try:
        base_path = sys._MEIPASS  # For PyInstaller bundled apps
    except Exception:
        base_path = os.path.abspath(".")  # Regular execution
    return os.path.join(base_path, relative_path)


def build_command(program_path, *args):
    """Builds a command line execution string."""
    return [program_path, *args]


def img_to_string(pil_image):
    """Extracts text from an image using OCR."""
    tess.pytesseract.tesseract_cmd = resource_path(FilePaths.TESSERACT_EXE_PATH.value)
    try:
        result = tess.image_to_string(pil_image, lang="eng", config="--psm 6")
    except tess.pytesseract.TesseractError as e: # Handle potential Tesseract errors
        print(f"OCR Error: {e}")
        traceback.print_exc()
        return ""  # Return empty string on error

    return result.replace("\t", "").replace("\n", "").replace("\f", "")


def img_remove_background_and_enhance_word(cv_image, lower, upper):
    """Removes background and enhances text in an image."""
    hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    return cv2.bitwise_and(cv_image, cv_image, mask=mask) # Apply mask


def aircv_rectangle_to_box(rectangle):
    """Converts an aircv rectangle to a bounding box."""
    return rectangle[0][0], rectangle[0][1], rectangle[3][0], rectangle[3][1]


def bot_print(msg):
    """Prints a message to the console."""
    print(msg)



def get_last_info():
    """Retrieves the latest version information."""
    try:
        url = "https://raw.githubusercontent.com/yuceltoluyag/Rise-of-Kingdoms-Bot/main/docs/version.json"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes (e.g., 404)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching version info: {e}")
        return {}



def grab_screen(region=None):
    """Captures a screenshot of the specified region or the entire screen."""
    if region:
        x, y, width, height = region
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
    else:
        screenshot = pyautogui.screenshot()
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)  # Convert to BGR


def locate_image_on_screen(image_path, confidence=0.9):
    """Locates an image on the screen using template matching."""
    try:
        template = cv2.imread(resource_path(image_path), cv2.IMREAD_COLOR)  # load in color
        screenshot = grab_screen()
        match = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(match)

        if max_val >= confidence:
            h, w = template.shape[:2]
            x, y = max_loc
            center_x = x + w / 2
            center_y = y + h / 2
            return True, (center_x, center_y) # Return True and center coords
        return False, None # No Match

    except Exception as e:
        print(f"Error locating image: {e}")
        return False, None