from enum import Enum
from filepath.constants import *


class StrImagePosition(Enum):
    WINDOWS_TITLE = (161, 13, 322, 50)


class FilePaths(Enum):
    TEST_SRC_FOLDER_PATH = "test_screen_caps\\"
    TEST_CURR_SCREEN_CAP_PATH = "test_screen_caps\\current_cap.png"
    TESSERACT_EXE_PATH = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    TESSDATA_CHI_SIM_PATH = (
        "C:\\Program Files\\Tesseract-OCR\\tessdata\\chi_sim.traineddata"
    )
    SAVE_FOLDER_PATH = "save\\"


class BuffsImageAndProps(Enum):
    ENHANCED_GATHER_BLUE = [
        "templates\\buffs\\enhanced_gathering_blue.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        BOOSTS,
    ]
    ENHANCED_GATHER_PURPLE = [
        "templates\\buffs\\enhanced_gathering_purple.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        BOOSTS,
    ]


class ItemsImageAndProps(Enum):
    ENHANCED_GATHER_BLUE = [
        "templates\\items\\enhanced_gathering_blue.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        BOOSTS,
    ]
    ENHANCED_GATHER_PURPLE = [
        "templates\\items\\enhanced_gathering_blue.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        BOOSTS,
    ]


class ImagePathAndProps(Enum):
    MAP_BUTTON_IMG_PATH = [
        "templates\\map_button.png",
        (1920, 1080),
        (1697, 883, 1801, 977),
        0.98,
        25,
        HOME,
    ]
    HOME_BUTTON_IMG_PATH = [
        "templates\\home_button.png",
        (1920, 1080),
        (1697, 883, 1801, 977),
        0.98,
        25,
        MAP,
    ]
    GREEN_HOME_BUTTON_IMG_PATH = [
        "templates\\green_home_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        GREEN_HOME,
    ]
    WINDOW_IMG_PATH = [
        "templates\\window.png",
        (1920, 1080),
        (1396, 222, 1436, 250),
        0.70,
        25,
        WINDOW,
    ]
    WINDOW_TITLE_MARK_IMG_PATH = [
        "templates\\window_title_mark.png",
        (1920, 1080),
        (632, 214, 685, 256),
        0.70,
        25,
        WINDOW_TITLE,
    ]
    BUILDING_TITLE_MARK_IMG_PATH = [
        "templates\\building_title_left.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        BUILDING_TITLE,
    ]
    BUILDING_INFO_BUTTON_IMG_PATH = [
        "templates\\building_info_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        BUILDING_INFO,
    ]
    QUEST_CLAIM_BUTTON_IMAGE_PATH = [
        "templates\\quests_claim_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        CLAIM_BUTTON,
    ]
    BARRACKS_BUTTON_IMAGE_PATH = [
        "templates\\barracks_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        BARRACKS_BUTTON,
    ]
    ARCHER_RANGE_BUTTON_IMAGE_PATH = [
        "templates\\archery_range_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ARCHER_RANGE_BUTTON,
    ]
    STABLE_BUTTON_IMAGE_PATH = [
        "templates\\stable_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        STABLE_BUTTON,
    ]
    SIEGE_WORKSHOP_BUTTON_IMAGE_PATH = [
        "templates\\siege_workshop_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SIEGE_WORKSHOP_BUTTON,
    ]
    TRAINING_UPGRADE_BUTTON_IMAGE_PATH = [
        "templates\\training_upgrade_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        TRAINING_UPGRADE_BUTTON,
    ]
    TRAIN_BUTTON_IMAGE_PATH = [
        "templates\\train_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        TRAIN_BUTTON,
    ]
    UPGRADE_BUTTON_IMAGE_PATH = [
        "templates\\upgrade_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        UPGRADE_BUTTON,
    ]
    SPEED_UP_BUTTON_IMAGE_PATH = [
        "templates\\speed_up_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SPEED_UP,
    ]
    DECREASING_BUTTON_IMAGE_PATH = [
        "templates\\decreasing_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        DECREASING,
    ]
    INCREASING_BUTTON_IMAGE_PATH = [
        "templates\\increasing_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        INCREASING,
    ]
    LOCK_BUTTON_IMAGE_PATH = [
        "templates\\lock_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        LOCK,
    ]
    RESOURCE_SEARCH_BUTTON_IMAGE_PATH = [
        "templates\\resource_search_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        RESOURCE_SEARCH,
    ]
    RESOURCE_GATHER_BUTTON_IMAGE_PATH = [
        "templates\\resource_gather_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        RESOURCE_GATHER,
    ]
    NEW_TROOPS_BUTTON_IMAGE_PATH = [
        "templates\\new_troops_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        NEW_TROOPS,
    ]
    TROOPS_MATCH_BUTTON_IMAGE_PATH = [
        "templates\\troops_match_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        TROOPS_MATCH,
    ]
    VERIFICATION_CHEST_BUTTON_IMAGE_PATH = [
        "templates\\verification_chest_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VERIFICATION_CHEST,
    ]
    VERIFICATION_VERIFY_BUTTON_IMAGE_PATH = [
        "templates\\verification_verify_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VERIFICATION_VERIFY,
    ]
    VERIFICATION_CLOSE_REFRESH_OK_BUTTON_IMAGE_PATH = [
        "templates\\verification_close_refresh_ok_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VERIFICATION_CLOSE_REFRESH_OK,
    ]
    GIFTS_CLAIM_BUTTON_IMAGE_PATH = [
        "templates\\alliance_gifts_claim_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        GIFTS_CLAIM,
    ]
    TECH_RECOMMEND_IMAGE_PATH = [
        "templates\\alliance_tech_recommend.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        TECH_RECOMMEND,
    ]
    TECH_DONATE_BUTTON_IMAGE_PATH = [
        "templates\\alliance_tech_donate.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        TECH_DONATE,
    ]
    MATERIALS_PRODUCTION_BUTTON_IMAGE_PATH = [
        "templates\\materials_production_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        MATERIALS_PRODUCTION,
    ]
    TAVERN_BUTTON_BUTTON_IMAGE_PATH = [
        "templates\\tavern_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        TAVERN_BUTTON,
    ]
    CHEST_OPEN_BUTTON_IMAGE_PATH = [
        "templates\\chest_open_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        CHEST_OPEN,
    ]
    CHEST_CONFIRM_BUTTON_IMAGE_PATH = [
        "templates\\chest_confirm_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        CHEST_CONFIRM,
    ]
    ATTACK_BUTTON_POS_IMAGE_PATH = [
        "templates\\attack_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ATTACK_BUTTON,
    ]
    HOLD_POS_CHECKED_IMAGE_PATH = [
        "templates\\hold_posistion_checked.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        HOLD_POS_CHECKED,
    ]
    HOLD_POS_UNCHECK_IMAGE_PATH = [
        "templates\\hold_position_unchecked.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        HOLD_POS_UNCHECK,
    ]
    UNSELECT_BLUE_ONE_SAVE_BUTTON_IMAGE_PATH = [
        "templates\\unselect_save_blue_one.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.95,
        25,
        UNSELECT_BLUE_ONE,
    ]
    SELECTED_BLUE_ONE_SAVE_BUTTON_IMAGE_PATH = [
        "templates\\selected_save_blue_one.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.95,
        25,
        SELECTED_BLUE_ONE,
    ]
    SAVE_SWITCH_BUTTON_IMAGE_PATH = [
        "templates\\switch_save.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SAVE_SWITCH,
    ]
    VICTORY_MAIL_IMAGE_PATH = [
        "templates\\victory_mail.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VICTORY_MAIL,
    ]
    DEFEAT_MAIL_IMAGE_PATH = [
        "templates\\defeat_mail.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        DEFEAT_MAIL,
    ]
    RETURN_BUTTON_IMAGE_PATH = [
        "templates\\return_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        RETURN_BUTTON,
    ]
    HOLD_ICON_IMAGE_PATH = [
        "templates\\hold_icon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        HOLD_ICON,
    ]
    HOLD_ICON_SMALL_IMAGE_PATH = [
        "templates\\hold_icon_small.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        HOLD_ICON_SMALL,
    ]
    MARCH_BAR_IMAGE_PATH = [
        "templates\\march_bar.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        MARCH_BAR,
    ]
    HEAL_ICON_IMAGE_PATH = [
        "templates\\heal_icon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        HEAL_ICON,
    ]
    DAILY_AP_CLAIM_BUTTON_IMAGE_PATH = [
        "templates\\daily_ap_claim.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        DAILY_AP_CLAIM,
    ]
    USE_AP_BUTTON_IMAGE_PATH = [
        "templates\\use_ap.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        USE_AP,
    ]
    SCOUT_BUTTON_IMAGE_PATH = [
        "templates\\scout_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SCOUT_BUTTON,
    ]
    SCOUT_EXPLORE_BUTTON_IMAGE_PATH = [
        "templates\\explore_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        EXPLORE_BUTTON,
    ]
    SCOUT_EXPLORE2_BUTTON_IMAGE_PATH = [
        "templates\\explore_button2.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        EXPLORE_BUTTON2,
    ]
    SCOUT_EXPLORE3_BUTTON_IMAGE_PATH = [
        "templates\\explore_button3.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        EXPLORE_BUTTON3,
    ]
    SCOUT_SEND_BUTTON_IMAGE_PATH = [
        "templates\\scout_send_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        SEND_BUTTON,
    ]
    MAIL_EXPLORATION_REPORT_IMAGE_PATH = [
        "templates\\mail_exploration_report.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        MAIL_EXPLORATION_REPORT,
    ]
    MAIL_SCOUT_BUTTON_IMAGE_PATH = [
        "templates\\mail_scout_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        MAIL_SCOUT_BUTTON,
    ]
    INVESTIGATE_BUTTON_IMAGE_PATH = [
        "templates\\investigate_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        INVESTIGATE_BUTTON,
    ]
    GREAT_BUTTON_IMAGE_PATH = [
        "templates\\great_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        GREAT_BUTTON,
    ]
    SCOUT_IDLE_ICON_IMAGE_PATH = [
        "templates\\scout_idle_icon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        IDLE_ICON,
    ]
    SCOUT_ZZ_ICON_IMAGE_PATH = [
        "templates\\scout_zz_icon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        ZZ_ICON,
    ]
    MERCHANT_ICON_IMAGE_PATH = [
        "templates\\merchant_icon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        MERCHANT_ICON,
    ]
    MERCHANT_FREE_BTN_IMAGE_PATH = [
        "templates\\merchant_free_btn.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        MERCHANT_FREE_BTN,
    ]
    MERCHANT_BUY_WITH_WOOD_IMAGE_PATH = [
        "templates\\merchant_buy_with_wood.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        MERCHANT_BUY_WITH_WOOD,
    ]
    MERCHANT_BUY_WITH_FOOD_IMAGE_PATH = [
        "templates\\merchant_buy_with_food.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        MERCHANT_BUY_WITH_FOOD,
    ]
    HAS_MATCH_QUERY_IMAGE_PATH = [
        "templates\\has_match_query.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.80,
        25,
        HAS_MATCH_QUERY,
    ]
    VERIFICATION_VERIFY_TITLE_IMAGE_PATH = [
        "templates\\verification_verify_title.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VERIFICATION_VERIFY_TITLE,
    ]
    SUNSET_CANYON_IMAGE_PATH = [
        "templates\\sunset_canyon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SUNSET_CANYON_BTN,
    ]
    SUNSET_CANYON_OK_IMAGE_PATH = [
        "templates\\sunset_canyon_ok.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SUNSET_CANYON_OK_BTN,
    ]
    LOST_CANYON_IMAGE_PATH = [
        "templates\\lost_canyon.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SUNSET_CANYON_BTN,
    ]
    LOST_CANYON_OK_IMAGE_PATH = [
        "templates\\lost_canyon_ok.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        LOST_CANYON_OK_BTN,
    ]
    SKIP_BATTLE_CHECKED_IMAGE_PATH = [
        "templates\\skip_battle_checked.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        SKIP_BATTLE_CHECKED,
    ]
    ITEM_VIP1_IMAGE_PATH = [
        "templates\\items\\resources\\vip1.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_VIP1,
    ]
    ITEM_VIP2_IMAGE_PATH = [
        "templates\\items\\resources\\vip2.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_VIP2,
    ]
    ITEM_GEMS1_IMAGE_PATH = [
        "templates\\items\\resources\\gems1.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_GEMS1,
    ]
    ITEM_GEMS2_IMAGE_PATH = [
        "templates\\items\\resources\\gems2.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_GEMS2,
    ]
    ITEM_GEMS3_IMAGE_PATH = [
        "templates\\items\\resources\\gems3.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_GEMS3,
    ]
    ITEM_RESOURCE_PACK1_IMAGE_PATH = [
        "templates\\items\\resources\\resource_pack1.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_RESOURCE_PACK1,
    ]
    ITEM_EXCESS_RESOURCE_PROMPT_YES_IMAGE_PATH = [
        "templates\\items\\resources\\excess_resource_prompt_yes.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_EXCESS_RESOURCE_PROMPT_YES,
    ]
    ITEM_EXCESS_RESOURCE_PROMPT_NO_IMAGE_PATH = [
        "templates\\items\\resources\\excess_resource_prompt_no.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        ITEM_EXCESS_RESOURCE_PROMPT_NO,
    ]
    ALL_ARMIES_BUSY_IMAGE_PATH1 = [
        "templates\\AllArmiesBusy1.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        "ALL_ARMIES_BUSY1",
    ]
    ALL_ARMIES_BUSY_IMAGE_PATH2 = [
        "templates\\AllArmiesBusy2.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        "ALL_ARMIES_BUSY2",
    ]
    # Mağara görselleri
    CAVE_IMAGE_PATH = [
        "templates\\cave.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        "CAVE",
    ]
    CAVE2_IMAGE_PATH = [
        "templates\\cave2.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        "CAVE2",
    ]
    # Köy görseli
    VILLAGE_IMAGE_PATH = [
        "templates\\village.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        "VILLAGE",
    ]


class GuiCheckImagePathAndProps(Enum):
    VERIFICATION_VERIFY_BUTTON_IMAGE_PATH = [
        "templates\\verification_verify_button.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.90,
        25,
        VERIFICATION_VERIFY,
    ]
    MAP_BUTTON_IMG_PATH = [
        "templates\\map_button_0.png",
        (1920, 1080),
        (10, 602, 113, 709),
        0.98,
        25,
        HOME,
    ]
    HOME_BUTTON_IMG_PATH = [
        "templates\\home_button_0.png",
        (1920, 1080),
        (10, 602, 113, 709),
        0.98,
        25,
        MAP,
    ]
    WINDOW_IMG_PATH = [
        "templates\\window.png",
        (1920, 1080),
        (0, 0, 0, 0),
        0.70,
        25,
        WINDOW,
    ]


GuiCheckImagePathAndPropsOrdered = [
    # GuiCheckImagePathAndProps.VERIFICATION_CLOSE_REFRESH_OK_BUTTON_IMAGE_PATH,
    GuiCheckImagePathAndProps.VERIFICATION_VERIFY_BUTTON_IMAGE_PATH,
    GuiCheckImagePathAndProps.MAP_BUTTON_IMG_PATH,
    GuiCheckImagePathAndProps.HOME_BUTTON_IMG_PATH,
    GuiCheckImagePathAndProps.WINDOW_IMG_PATH,
]

ALL_ARMIES_BUSY_IMAGE_PATH1 = [
    "templates\\AllArmiesBusy1.png",
    (1920, 1080),
    (0, 0, 0, 0),
    0.70,
    25,
    "ALL_ARMIES_BUSY1",
]

ALL_ARMIES_BUSY_IMAGE_PATH2 = [
    "templates\\AllArmiesBusy2.png",
    (1920, 1080),
    (0, 0, 0, 0),
    0.70,
    25,
    "ALL_ARMIES_BUSY2",
]
