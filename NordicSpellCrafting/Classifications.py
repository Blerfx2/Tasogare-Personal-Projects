import pixie

"""TODO 1. In the spell class, make a function that takes the x and y values of each piece and does the correct calculation to rotate in the correct directions
        1.5 Might need to make a half rectangle function for things like 120 ft.
        2. Make a second function that does the same thing for diagonals
        3. For the Deception, Shapechanging, and Detection stave heads would need an if statement to change line length.
        4. Make the components for the spell components (i.e. lines, curves, semicircles, etc.)
        5. Figure out how you want to mush the data together
        """
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")

fill = pixie.Paint(pixie.SOLID_PAINT)
fill.color = pixie.parse_color("#FFFFFF")


def smallCurve(image, x, y, flip=0):
    path = pixie.parse_path(
    f"""
    M 900 200
    A 100 100 90 0 0 1100 200
    """
    )
    image.stroke_path(path, paint, stroke_width=20)
        
def bigCurve(image): # Stave only
    path = pixie.parse_path(
        """
        M 1150 200
        A 150 150 90 0 1 850 200
        """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfRec(ctx, flip=0): # Stave only
    ctx.stroke_segment(850, 200, 850, 350)
    ctx.stroke_segment(840, 350, 1160, 350)
    ctx.stroke_segment(1150, 350, 1150, 200)

def smallHalfRec(ctx, y, flip=0): # Stave only?
    ctx.stroke_segment(850, 200, 850, 325)
    ctx.stroke_segment(840, 325, 1160, 325)
    ctx.stroke_segment(1150, 325, 1150, 200)

def mainLine(ctx, x, y):
    ctx.stroke_segment(x, y, 1000, 1000)

def line(ctx, pos=0, rotate=0):
# Unlike many other functions, this one only needs a 1 if it is a vertical line
# 60 past the top of the section
    if rotate == 1:
        ctx.stroke_segment(pos, 910, pos, 1090)
    else: 
        ctx.stroke_segment(910, pos, 1090, pos)

def sidewaysX(ctx, x, y, flip=0):
    ctx.stroke_segment(920, 290, 1080, 220)
    ctx.stroke_segment(920, 220, 1080, 290)

def pointUp(ctx, x, y, flip=0):
    ctx.stroke_segment(925, 280, 1006, 195)
    ctx.stroke_segment(994, 195, 1075, 280)

def pointDown(ctx, x, y, flip=0):
    ctx.stroke_segment(925, 210, 1006, 295)
    ctx.stroke_segment(994, 295, 1075, 210)

def curveDown(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 925 275
    A 75 75 90 0 1 1075 275
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def lineCirc(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 950 250
    A 50 50 90 0 1 1050 250
    A 50 50 90 0 1 950 250
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfArrowR(ctx, x, y, flip=0):
    ctx.stroke_segment(1005, 205, 1050, 310)

def keyblade(ctx, x, y, flip=0):
    ctx.stroke_segment(1000, 210, 1080, 210)
    ctx.stroke_segment(1000, 240, 1080, 240)

def equals(ctx, x, y, flip=0):
    ctx.stroke_segment(925, 240, 1075, 240)
    ctx.stroke_segment(925, 270, 1075, 270)

def flag(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 1000 220
    L 1060 270
    L 1000 320
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def diamond(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 1000 200
    L 1050 250
    L 1000 300
    L 950 250
    Z
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def antlers(ctx, x, y, flip=0): # Stave only
    ctx.stroke_segment(890, 250, 1110, 250)
    ctx.stroke_segment(900, 250, 900, 200)
    ctx.stroke_segment(945, 250, 945, 200)
    ctx.stroke_segment(1055, 250, 1055, 200)
    ctx.stroke_segment(1100, 250, 1100, 200)

def smallLineCirc(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 960 240
    A 30 30 90 0 1 1040 240
    A 30 30 90 0 1 960 240
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def smallFillCirc(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 965 240
    A 20 20 90 0 1 1035 240
    A 20 20 90 0 1 965 240
    """
    )

    image.fill_path(path, fill)
    smallLineCirc(image)

def doubleDots(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 940 300
    A 10 10 90 0 1 960 300
    A 10 10 90 0 1 940 300
    M 1040 300
    A 10 10 90 0 1 1060 300
    A 10 10 90 0 1 1040 300
    """
    )
    image.fill_path(path, paint)

def shieldedOrb(image, x, y, flip=0):
    path = pixie.parse_path(
    """
    M 945 250
    A 55 55 90 0 1 1055 250
    A 55 55 90 0 1 945 250
    """
    )

    image.fill_path(path, fill)
    path = pixie.parse_path(
    """
    M 965 215
    A 50 50 90 1 0 1035 215
    """
    )
    image.stroke_path(path, paint, stroke_width=20)
    path = pixie.parse_path(
    """
    M 980 255
    A 20 20 90 0 1 1020 255
    A 20 20 90 0 1 980 255

    """
    )
    image.fill_path(path, paint)

def strSave(ctx, x, y):
    ctx.stroke_rect(900, 900, 200, 200)
    ctx.stroke_rect(950, 950, 100, 100)

class Identity:
    def __init__(spell, name):
        spell.name = name
        spell.x = 1000 # x and y are more like the center of where to put any symbol
        spell.y

class School(Identity):
    def __init__(spell, name):
        super().__init__(name)
        spell.y = 200
        if "DMG" in spell.name:
            spell.damage = 1
            spell.name = spell.name.split(' ')[1]
        else:
            spell.damage = 0

    def draw(spell, ctx, image):
        if spell.damage == 1:
            if spell.name in ["Bludgeoning", "Piercing", "Slashing"]:
                halfRec(ctx)
                if spell.name == "Bludgeoning":
                    pass
                elif spell.name == "Piercing":
                    pass
                elif spell.name == "Slashing":
                    pass
            elif spell.name == "Force":
                smallHalfRec(ctx)
                equals(ctx)
            
            elif spell.name == "Fire":
                pass
            elif spell.name == "Cold":
                pass
            elif spell.name == "Lightning":
                pass
            elif spell.name == "Thunder":
                pass
            elif spell.name == "Acid":
                pass
            elif spell.name == "Poison":
                pass
            elif spell.name == "Necrotic":
                pass
            elif spell.name == "Radiant":
                pass
            elif spell.name == "Psychic":
                pass
        elif spell.name == "Buff":
                pass
        elif spell.name == "Debuff":
                pass
        elif spell.name == "Negation":
                pass
        elif spell.name == "Healing":
                pass
        elif spell.name == "Warding":
                pass
        elif spell.name == "Summoning":
                pass
        elif spell.name == "Banishment":
                pass
        elif spell.name == "Creation":
                pass
        elif spell.name == "Exploration":
                pass
        elif spell.name == "Environment":
                pass
        elif spell.name == "Detection":
                pass
        elif spell.name == "Foreknowledge":
                pass
        elif spell.name == "Scrying":
                pass
        elif spell.name == "Deception":
                pass
        elif spell.name == "Social":
                pass
        elif spell.name == "Communication":
                pass
        elif spell.name == "Shapechanging":
                pass
        elif spell.name == "Movement":
                pass
        elif spell.name == "Teleportation":
                pass
        elif spell.name == "Control":
                pass
        elif spell.name == "Utility":
                pass
        
class Range(Identity):
    def __init__(spell, name):
          super().__init__(name)
          spell.y = 500

    def draw(spell, ctx, image):
        if spell.name == "Self":
            pass
        elif spell.name == "Touch":
            pass
        elif spell.name == "5 Feet":
            pass
        elif spell.name == "10 Feet":
            pass
        elif spell.name == "30 Feet":
            pass
        elif spell.name == "60 Feet":
            pass
        elif spell.name == "90 Feet":
            pass
        elif spell.name == "100 Feet":
            pass
        elif spell.name == "120 Feet":
            pass
        elif spell.name == "150 Feet":
            pass
        elif spell.name == "300 Feet":
            pass
        elif spell.name == "500 Feet":
            pass
        elif spell.name == "1 Mile":
            pass
        elif spell.name == "Sight":
            pass

class Duration(Identity):
    def __init__(spell, name):
          super().__init__(name)
          spell.y = 700

    def draw(spell, ctx, image):
        if spell.name == "Instant":
            pass
        elif spell.name == "1 Round":
            pass
        elif spell.name == "1 Minute":
            pass
        elif spell.name == "10 Minutes":
            pass
        elif spell.name == "1 Hour":
            pass
        elif spell.name == "8 Hours":
            pass
        elif spell.name == "10 Hours":
            pass
        elif spell.name == "24 Hours":
            pass
        elif spell.name == "7 Days":
            pass
        elif spell.name == "10 Days":
            pass
        elif spell.name in "Concentration 1 Min.":
            pass
        elif spell.name in "Concentration 10 Min.":
            pass
        elif spell.name in "Concentration 1 Hr.":
            pass
        elif spell.name in "Concentration 8 Hr.":
            pass
        elif spell.name in "Concentration 24 Hr.":
            pass
        elif spell.name == "30 Days":
            pass

class Save(Identity):
    def __init__(spell, name):
          super().__init__(name)

    def draw(spell, ctx, image):
        if spell.name == "None":
            return
        elif spell.name == "Dexterity":
            pass
        elif spell.name == "Constitution":
            pass
        elif spell.name == "Wisdom":
            pass
        elif spell.name == "Strength":
            pass
        elif spell.name == "Charisma":
            pass
        elif spell.name == "Intelligence":
            pass
         

def main():
    image = pixie.Image(2000,2000)
    image.fill(pixie.Color(1, 1, 1, 1))

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = 25
    mainLine(ctx, 1000, 200)


    ctx.line_width = 20



    image.write_file("trying.png")


    # Sideways

    # ctx.stroke_segment(1000, 1000, 1800, 1000)

    # spath = pixie.parse_path(
    #     """
    #     M 1800 900
    #     A 100 100 0 0 0 1800 1100
    #     M 1800 1150
    #     A 150 150 0 0 1 1800 850
    #     """
    # )
    # ctx.line_width = 20
    # ctx.stroke_segment(1500, 905, 1500, 1095)
    # ctx.stroke_segment(1300, 905, 1300, 1095)
    # image.stroke_path(spath, paint, stroke_width=20)



if __name__ == "__main__":
    main()