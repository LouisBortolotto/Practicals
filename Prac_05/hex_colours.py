
HEX_COLOURS = {"BLUE": "#0000ff", "AZURE": "#f0ffff", "CHOCOLATE": "#d2691e", "ORANGE": "#ff8c00",
               "VIOLET": "#9400d3", "GRAY": "#bebebe", "GOLD": "#ffd700", "RED": "#ff3030", "GREEN": "#a2cd5a"}

colour = input("Enter colour: ").upper()
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour")
    colour = input("Enter colour: ").upper()
