color_dict = {
    0: "black_gesso",
    1: "bright_red",
    2: "burnt_umber",
    3: "cadmium_yellow",
    4: "dark_sienna",
    5: "indian_red",
    6: "indian_yellow",
    7: "liquid_black",
    8: "liquid_clear",
    9: "midnight_black",
    10: "phthalo_blue",
    11: "phthalo_green",
    12: "prussian_blue",
    13: "sap_green",
    14: "titanium_white",
    15: "van_dyke_brown",
    16: "yellow_ochre",
    17: "alizarin_crimson"
}

subject_dict = {
    0: "barn",
    1: "beach",
    2: "boat",
    3: "bridge",
    4: "building",
    5: "bushes",
    6: "cabin",
    7: "cactus",
    8: "cirrus",
    9: "cliff",
    10: "clouds",
    11: "conifer",
    12: "cumulus",
    13: "deciduous",
    14: "dock",
    15: "farm",
    16: "fence",
    17: "fire",
    18: "flowers",
    19: "fog",
    20: "grass",
    21: "hills",
    22: "lake",
    23: "lakes",
    24: "lighthouse",
    25: "mill",
    26: "moon",
    27: "mountain",
    28: "mountains",
    29: "night",
    30: "ocean",
    31: "palm_trees",
    32: "path",
    33: "person",
    34: "portrait",
    35: "river",
    36: "rocks",
    37: "snow",
    38: "snowy_mountain",
    39: "structure",
    40: "sun",
    41: "tree",
    42: "trees",
    43: "waterfall",
    44: "waves",
    45: "windmill",
    46: "winter"
}

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


def find_value(dict, key):
    """ Returns value based on key in dictionary """
    if key in dict:
        return dict[key]
    return None
