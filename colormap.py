from itertools import product

MAJOR_COLORS = ["White", "Red", "Black", "Yellow", "Violet"]
MINOR_COLORS = ["Blue", "Orange", "Green", "Brown", "Slate"]

color_map_dict = dict(enumerate(product(MAJOR_COLORS, MINOR_COLORS), start=1))


def color_pair_to_string(major_color, minor_color):
    return f"{major_color} {minor_color}"


def get_color_from_pair_number(pair_number):
    return color_map_dict.get(pair_number, None)


def get_pair_number_from_color(major_color, minor_color):
    for key in color_map_dict.keys():
        if color_map_dict[key] == (major_color, minor_color):
            return key
    return None
