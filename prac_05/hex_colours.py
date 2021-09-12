"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOUR_CODES = {"DarkSalmon": "#E9967A", "DarkKhaki": "#BDB76B",
                "Fuchsia": "#FF00FF", "SlateBlue": "#6A5ACD",
                "MediumSpringGreen": "#00FA9A", "MediumAquamarine": "#66CDAA",
                "MediumSlateBlue": "#7B68EE", "SandyBrown": "#F4A460",
                "SaddleBrown": "#8B4513", "AntiqueWhite": "#FAEBD7",
                "Tomato": "#FF6347", "DarkOrange": "#FF8C00", "HotPink": "#FF69B4",
                "Crimson": "#DC143C", "IndianRed": "#CD5C5C"}

colour = input("Enter a colour name: ")
while colour != "":
    print("The code for \"{}\" is {}".format(colour, COLOUR_CODES.get(colour)))
    colour = input("Enter a colour name: ")