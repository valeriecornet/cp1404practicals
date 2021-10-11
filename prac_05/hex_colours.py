"""Hexadecimal colour dictionary"""

HEX_COLOURS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "aquamarine1": "#7fffd4", "blue1": "#0000ff", "brown": "#a52a2a", "CadetBlue": "#5f9ea0", "chartreuse1": "#7fff00", "coral": "#ff7f50", "DarkOrchid": "#9932cc", "gold1": "#ffd700"}

hex_colour = input("Enter hexadecimal colour: ")

while hex_colour != "":
    if hex_colour in HEX_COLOURS:
        print("The code for colour {} is {}".format(hex_colour, HEX_COLOURS[hex_colour]))
    else:
        print("Invalid colour")
    hex_colour = input("Enter hexadecimal colour: ")
