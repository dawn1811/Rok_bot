from gui.creator import (
    checkbox_fn_creator,
    train_fn_creator,
    write_bot_config,
    entry_int_fn_creator,
)

from tkinter import StringVar, OptionMenu, Frame, Label, Entry, N, W
import webbrowser


# ───────────────────────────────────────────
#  Helper used by many <entry> widgets
# ───────────────────────────────────────────
def integer_entry_validate_cmd_creator(app, attr_name, def_value=0):
    """Validate that entry only contains an integer and sync to bot_config."""
    def validate_cmd(value, action_type):
        # action_type == "1"  → insertion / modification
        if action_type == "1":
            if not value.isdigit() or (len(value) > 1 and value[0] == "0"):
                return False
        setattr(app.bot_config, attr_name, int(value or def_value))
        # ——— PC-native: use a fixed prefix instead of device.save_file_prefix
        write_bot_config(app.bot_config, prefix="pc_bot")
        return True
    return validate_cmd


# ───────────────────────────────────────────
#  Checkbox / Entry creators (unchanged)
# ───────────────────────────────────────────
restart_checkbox          = checkbox_fn_creator("enableStop", "Auto Restart Game")
restart_do_round          = entry_int_fn_creator("stopDoRound", "Execute at every", "round")

break_do_round            = entry_int_fn_creator("breakDoRound", "Execute at every", "round")
terminate_checkbox        = checkbox_fn_creator("terminate", "Terminate when break")
break_checkbox            = checkbox_fn_creator("enableBreak", "Take break at every end of round")

mystery_merchant_checkbox = checkbox_fn_creator("enableMysteryMerchant",
                                                "Use resource buy item in Mystery Merchant")


# ── dropdown to pick break time ───────────────────────────────────────────
def time_drop_down(app, parent):
    value    = f"{int(app.bot_config.breakTime / 60)} Minute"
    options  = [f"{m} Minute" for m in (1,2,3,4,5,10,15,20,25,30,40,50,60)]
    variable = StringVar(value=value)

    def cmd(selected):
        app.bot_config.breakTime = int(selected.replace(" Minute", "")) * 60
        write_bot_config(app.bot_config, prefix="pc_bot")

    return OptionMenu(parent, variable, *options, command=cmd), variable


# ── in-city settings ──────────────────────────────────────────────────────
collecting_checkbox       = checkbox_fn_creator("enableCollecting",
                                                "Collect resources / help alliance")

produce_material          = checkbox_fn_creator("enableMaterialProduce", "Produce material")
material_do_round         = entry_int_fn_creator("materialDoRound", "Execute at every", "round")

open_free_chest_in_tavern = checkbox_fn_creator("enableTavern", "Open free chest in tavern")

training                  = checkbox_fn_creator("enableTraining", "Auto train/upgrade troops")
train_barracks            = train_fn_creator("Barracks:",       "trainBarracksTrainingLevel",
                                             "trainBarracksUpgradeLevel")
train_archery_range       = train_fn_creator("Archery:",        "trainArcheryRangeTrainingLevel",
                                             "trainArcheryRangeUpgradeLevel")
train_stable              = train_fn_creator("Stable:",         "trainStableTrainingLevel",
                                             "trainStableUpgradeLevel")
train_siege               = train_fn_creator("Siege:",          "trainSiegeWorkshopTrainingLevel",
                                             "trainSiegeWorkshopUpgradeLevel")

daily_vip_point_and_chest = checkbox_fn_creator("enableVipClaimChest",
                                                "Claim daily VIP point & chest")
vip_do_round              = entry_int_fn_creator("vipDoRound", "Execute at every", "round")

claim_quest_checkbox      = checkbox_fn_creator("claimQuests", "Claim quests / objectives")
quest_do_round            = entry_int_fn_creator("questDoRound", "Execute at every", "round")

alliance_action_checkbox  = checkbox_fn_creator("allianceAction",
                                                "Alliance gifts / donations / helps")
alliance_do_round         = entry_int_fn_creator("allianceDoRound", "Execute at every", "round")

# ── outside-city / barbarians / gather settings ──────────────────────────
attack_barbarians_checkbox    = checkbox_fn_creator("attackBarbarians", "Attack Barbarians")
hold_position_checkbox        = checkbox_fn_creator("holdPosition", "Hold Position After Attack")
heal_troops_checkbox          = checkbox_fn_creator("healTroopsBeforeAttack", "Heal troops before attack")
use_daily_ap_checkbox         = checkbox_fn_creator("useDailyAPRecovery", "Use Daily AP Recovery")
use_normal_ap_checkbox        = checkbox_fn_creator("useNormalAPRecovery", "Use Normal AP Recovery")
barbarians_base_level_entry   = entry_int_fn_creator("barbariansBaseLevel", "Base Level (normal/KvK):")
barbarians_min_level_entry    = entry_int_fn_creator("barbariansMinLevel", "Min attack Level:")
barbarians_max_level_entry    = entry_int_fn_creator("barbariansMaxLevel", "Max attack Level:")
number_of_attack_entry        = entry_int_fn_creator("numberOfAttack", "Number of Attack:")
timeout_entry                 = entry_int_fn_creator("timeout", "Timeout (sec):")

gather_resource_checkbox      = checkbox_fn_creator("gatherResource", "Gather resource")
gather_gem_checkbox           = checkbox_fn_creator("gatherGem", "Gather Gem")
gather_gem_distance           = entry_int_fn_creator("gatherGemDistance", "Gem distance")
gather_gem_signal             = checkbox_fn_creator("gatherGemSignal", "No signal? (skip)")
resource_no_secondery_commander = checkbox_fn_creator(
                                    "gatherResourceNoSecondaryCommander", "No secondary commander")
use_gathering_boosts          = checkbox_fn_creator("useGatheringBoosts", "Use gathering boosts")
hold_one_query_space_checkbox = checkbox_fn_creator("holdOneQuerySpace", "Reserve 1 march slot")

enable_scout_checkbox         = checkbox_fn_creator("enableScout", "Enable explore")
enable_investigation_checkbox = checkbox_fn_creator("enableInvestigation", "Investigate Cave / Village")

enable_sunset_canyon_checkbox = checkbox_fn_creator("enableSunsetCanyon", "Enable Sunset Canyon")
enable_lost_canyon_checkbox   = checkbox_fn_creator("enableLostCanyon",   "Enable Lost Canyon")

use_items                     = checkbox_fn_creator("useItems", "Use Items")
use_items_vip                 = checkbox_fn_creator("useItemsVip", "Use VIP Points")
use_items_gems                = checkbox_fn_creator("useItemsGems", "Use Gem Items")
use_items_daily_rss           = checkbox_fn_creator("useItemsDailyRss", "Use 5× Lv1 RSS Packs (daily)")

# ── gather-resource ratio widget ─────────────────────────────────────────
def resource_ratio(app, parent):
    labels      = ["Food:", "Wood:", "Stone:", "Gold:"]
    attr_names  = ["gatherResourceRatioFood", "gatherResourceRatioWood",
                   "gatherResourceRatioStone", "gatherResourceRatioGold"]

    frame = Frame(parent)
    Label(frame, text="Type:").grid( row=0, column=0, sticky=N+W, padx=(0,5) )
    Label(frame, text="Ratio:").grid(row=1, column=0, sticky=N+W, padx=(0,5))

    for col, (lbl, attr) in enumerate(zip(labels, attr_names)):
        sv = StringVar(value=str(getattr(app.bot_config, attr)))

        def make_validator(attr_name):
            return integer_entry_validate_cmd_creator(app, attr_name, def_value=0)

        entry = Entry(frame, textvariable=sv, width=10, validate="key",
                      validatecommand=(frame.register(make_validator(attr)), "%P", "%d"))
        Label(frame, text=lbl).grid(row=0, column=col+1, sticky=N+W, padx=5)
        entry.grid(row=1, column=col+1, sticky=N+W, padx=5)
    return frame, None


# ───────────────────────────────────────────
#  Master list consumed by SettingFrame
# ───────────────────────────────────────────
bot_config_title_fns = [
    [break_checkbox,                    [break_do_round, terminate_checkbox, time_drop_down]],
    [mystery_merchant_checkbox,         []],
    [open_free_chest_in_tavern,         []],
    [collecting_checkbox,               []],
    [produce_material,                  [material_do_round]],
    [daily_vip_point_and_chest,         [vip_do_round]],
    [claim_quest_checkbox,              [quest_do_round]],
    [alliance_action_checkbox,          [alliance_do_round]],
    [training,                          [train_barracks, train_archery_range,
                                         train_stable, train_siege]],
    [attack_barbarians_checkbox,        [hold_position_checkbox, heal_troops_checkbox,
                                         use_daily_ap_checkbox, use_normal_ap_checkbox,
                                         barbarians_base_level_entry, barbarians_min_level_entry,
                                         barbarians_max_level_entry, number_of_attack_entry,
                                         timeout_entry]],
    [gather_resource_checkbox,          [use_gathering_boosts, hold_one_query_space_checkbox,
                                         resource_ratio, resource_no_secondery_commander]],
    [enable_scout_checkbox,             [enable_investigation_checkbox]],
    [gather_gem_checkbox,               [gather_gem_distance, gather_gem_signal]],
    [enable_sunset_canyon_checkbox,     []],
    [enable_lost_canyon_checkbox,       []],
    [use_items,                         [use_items_vip, use_items_gems, use_items_daily_rss]],
]


# ───────────────────────────────────────────
#  Simple hyperlink callback
# ───────────────────────────────────────────
def callback(url: str):
    webbrowser.open_new(url)
