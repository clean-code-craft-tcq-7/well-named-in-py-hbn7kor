from colormap import color_map_dict


def md_heading():
    headerArray = ["| Pair number | Major Color | Minor Color |", "| --- | --- | --- |"]
    return "\n".join(headerArray)


def csv_heading():
    return "Pair number,Major Color,Minor Color"


def md_format_line(number, major_color, minor_color):
    return "| {} | {} | {} |".format(number, major_color, minor_color)


def csv_format_line(number, major_color, minor_color):
    return "{},{},{}".format(number, major_color, minor_color)


def print_reference_manual(heading_formatter, line_formatter):
    print(heading_formatter())
    for key in color_map_dict.keys():
        major_color, minor_color = color_map_dict[key]
        print(line_formatter(key, major_color, minor_color))
