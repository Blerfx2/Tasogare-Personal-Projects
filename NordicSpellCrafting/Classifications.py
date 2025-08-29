import pixie

angle_degrees = 45
angle_radians = angle_degrees * (3.14159 / 180)


"""TODO 1. Make each draw function do a for loop with a range. Modify all functions to account for all directions
        2 Might need to make a half rectangle function for things like 120 ft.
        3. For the Deception, Shapechanging, and Detection stave heads would need an if statement to change line length.
        4. Make the components for the spell components (i.e. lines, curves, semicircles, etc.)
        5. Figure out how you want to mush the data together
        """
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")

fill = pixie.Paint(pixie.SOLID_PAINT)
fill.color = pixie.parse_color("#FFFFFF")


def smallCurve(image, y, rotation=0):
# y should normally be the top of the segment
    if rotation in [1,3]:
        y = 2000 - y
    path = pixie.parse_path(
    f"""
    M 900 {y}
    A 100 100 90 0 {rotation} 1100 {y}
    """
    )
    image.stroke_path(path, paint, stroke_width=20)
        
def bigCurve(image, rotation = 0): # Stave only
    y = 200
    if rotation in [1,3]:
        y = 2000 - y
        rotation = 0
    else:
         rotation = 1
    path = pixie.parse_path(
        f"""
        M 1150 {y}
        A 150 150 90 0 {rotation} 850 {y}
        """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfRec(ctx, rotation=0): # Stave only
    y = 200
    if rotation == 0:
        y2 = y + 150
    else:
        y = 2000 - y
        y2 = y - 150
    ctx.stroke_segment(850, y, 850, y2)
    ctx.stroke_segment(840, y2, 1160, y2)
    ctx.stroke_segment(1150, y2, 1150, y)

def smallHalfRec(ctx, rotation=0): # Stave only?
    y = 200
    if rotation == 0:
        y2 = y + 125
    else:
        y = 2000 - y
        y2 = y - 125
    ctx.stroke_segment(850, y, 850, y2)
    ctx.stroke_segment(840, y2, 1160, y2)
    ctx.stroke_segment(1150, y2, 1150, y)

def mainLine(ctx, full=0):
    if full == 0:
        ctx.stroke_segment(1000, 200, 1000, 1000)
    elif full in [1,3]:
        ctx.stroke_segment(1000, 200, 1000, 1800)
    elif full in [2,4]:
        ctx.stroke_segment(200, 1000, 1800, 1000)
    elif full == 3:
# TODO Figure out how long diagonals need to be
        ctx.stroke_segment(1000, 200, 1000, 1000)
    
def line(ctx, pos=0, rotate=0):
# Unlike many other functions, this one only needs a 1 if it is a vertical line
# 60 past the top of the section
    if rotate in [1,3]:
        ctx.stroke_segment(910, 2000-pos, 1090, 2000-pos)
    if rotate == 2:
        ctx.stroke_segment(pos, 910, pos, 1090)
    else: 
        ctx.stroke_segment(910, pos, 1090, pos)

def sidewaysX(ctx, y, rotation=0):
# Pass in the lower value of y. Usually around 20 more than base
    if rotation == 0:
        y2 = y + 70
    else:
        y = 2000 - y
        y2 = y - 70
    ctx.stroke_segment(920, y, 1080, y2)
    ctx.stroke_segment(920, y2, 1080, y)

def pointUp(ctx, y, rotation=0):
# Pass in lower value. Usually is 5 less than base
    if rotation == 0:
        y2 = y + 85
    else:
         y = 2000 - y
         y2 = y - 85
    ctx.stroke_segment(925, y2, 1006, y)
    ctx.stroke_segment(994, y, 1075, y2)

def pointDown(ctx, y, rotation=0):
# Pass in lower value. Usually is 10 more than base
    if rotation == 0:
        y2 = y + 85
    else:
         y = 2000 - y
         y2 = y - 85
    ctx.stroke_segment(925, y, 1006, y2)
    ctx.stroke_segment(994, y2, 1075, y)

def curveDown(image, y, rotation=0):
# Usually y is 75 more than base
    if rotation in [1,3]:
        y = 2000 - y
        rotation = 0
    else:
        rotation = 1
    path = pixie.parse_path(
    f"""
    M 925 {y}
    A 75 75 90 0 1 1075 {y}
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

"TODO make a flag that accounts for moving on the x axis for all circles"

def lineCirc(image, y, rotation=0):
# y is usually 50 from base?
    if rotation in [1,3]:
        y = 2000 - y
    path = pixie.parse_path(
    f"""
    M 950 {y}
    A 50 50 90 0 1 1050 {y}
    A 50 50 90 0 1 950 {y}
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfArrowR(ctx, y, rotation=0):
# Pass in lower value. Usually is 5 more than base
    if rotation == 0:
        x, x2 = 1005, 1050
        y2 = y + 105
    else:
        x, x2 = 995, 950
        y = 2000 - y
        y2 = y - 105
    ctx.stroke_segment(x, y, x2, y2)

def keyblade(ctx, y, rotation=0):
# Pass in lower value. Usually is 10 more than base
    if rotation == 0:
        x = 1080
        y2 = y + 30
    else:
        x = 920
        y = 2000 - y
        y2 = y - 30
    ctx.stroke_segment(1000, y, x, y)
    ctx.stroke_segment(1000, y2, x, y2)

def equals(ctx, y, rotation=0):
# Pass in lower value. Usually is 40 more than base
    if rotation == 0:
        y2 = y + 30
    else:
        y = 2000 - y
        y2 = y - 30
    ctx.stroke_segment(925, y, 1075, y2)
    ctx.stroke_segment(925, y2, 1075, y)

def flag(image, y, rotation=0):
    x = 1000
    if rotation in [1,3]:
        y2, y3, x2 = y - 50, y - 100, 940
    else:
        y2, y3, x2 = y + 50, y + 100, 1060

    path = pixie.parse_path(
    f"""
    M {x} {y}
    L {x2} {y2}
    L {x} {y3}
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def diamond(image, y, rotation=0):
    x, x2, x3 = 1000, 950, 1050
    if rotation in [1,3]:
        y2, y3 = y - 50, y - 100
    else:
        y2, y3 = y + 50, y + 100
    path = pixie.parse_path(
    f"""
    M {x} {y}
    L {x3} {y2}
    L {x} {y3}
    L {x2} {y2}
    Z
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def antlers(ctx, rotation=0): # Stave only
    if rotation == 0:
        y, y2 = 200, y + 50
    else:
        y = 1800
        y2 = y - 50
    ctx.stroke_segment(890, y2, 1110, y2)
    ctx.stroke_segment(900, y2, 900, y)
    ctx.stroke_segment(945, y2, 945, y)
    ctx.stroke_segment(1055, y2, 1055, y)
    ctx.stroke_segment(1100, y2, 1100, y)

def smallLineCirc(image, y, rotation=0):
# y is usually 40 from base
    if rotation in [1,3]:
        y = 2000 - y

    path = pixie.parse_path(
    f"""
    M 960 {y}
    A 30 30 90 0 1 1040 {y}
    A 30 30 90 0 1 960 {y}
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def smallFillCirc(image, y, rotation=0):
# y is usually 40 from base
    if rotation in [1,3]:
        y = 2000 - y

    path = pixie.parse_path(
    f"""
    M 965 {y}
    A 20 20 90 0 1 1035 {y}
    A 20 20 90 0 1 965 {y}
    """
    )

    image.fill_path(path, fill)
    smallLineCirc(image)

def doubleDots(image, y, rotation=0):
# y is usually 100 from base
    if rotation in [1,3]:
        y = 2000 - y
    path = pixie.parse_path(
    f"""
    M 940 {y}
    A 10 10 90 0 1 960 {y}
    A 10 10 90 0 1 940 {y}
    M 1040 {y}
    A 10 10 90 0 1 1060 {y}
    A 10 10 90 0 1 1040 {y}
    """
    )
    image.fill_path(path, paint)

def shieldedOrb(image, y, rotation=0):
# y is usually 50 from base
    if rotation in [1,3]:
        y = 2000 - y
    path = pixie.parse_path(
    f"""
    M 945 {y}
    A 55 55 90 0 1 1055 {y}
    A 55 55 90 0 1 945 {y}
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

def strSave(ctx, y):
    y2 = y + 50
    ctx.stroke_rect(900, y, 200, 200)
    ctx.stroke_rect(950, y2, 100, 100)

class Identity:
    def __init__(spell, name):
        spell.name = name
    
    def collected(spell, functions, args, rotations, ctx, image):
        for rotation in range(0,rotations+1):
            if rotation == 3:
                cx, cy = image.width / 2, image.height / 2
                ctx.translate(cx, cy)
                ctx.rotate(angle_radians)
                ctx.translate(-cx, -cy)
                mainLine(ctx,1)
                mainLine(ctx,2)
            for func, arg in zip(functions, args):
                func(*arg, rotation)
            if rotation == 4:
                ctx.translate(cx, cy)
                ctx.rotate(-angle_radians)
                ctx.translate(-cx, -cy)
         

class School(Identity):
    def __init__(spell, name):
        super().__init__(name)
        spell.y = 200
        if "DMG" in spell.name:
            spell.damage = 1
            spell.name = spell.name.split(' ')[1]
        else:
            spell.damage = 0

    def draw(spell, ctx, image, rotation):
        functions = []
        args = []
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
            
            else:
                functions.append(bigCurve)
                args.append([image])
                if spell.name == "Fire":
                    pass
                elif spell.name == "Cold":
                    pass
                elif spell.name == "Lightning":
                    pass
                elif spell.name == "Thunder":
                    pass
                elif spell.name == "Acid":
                    functions.append(keyblade)
                    args.append([ctx,spell.y+10])
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
        super().collected(functions,args, rotation, ctx, image)
        
class Range(Identity):
    def __init__(spell, name):
          super().__init__(name)
          spell.y = 500

    def draw(spell, ctx, image, rotation):
        functions = []
        args = []
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
            functions.append(smallCurve)
            args.append([image, spell.y])
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
        super().collected(functions,args, rotation, ctx, image)

class Duration(Identity):
    def __init__(spell, name):
          super().__init__(name)
          spell.y = 700

    def draw(spell, ctx, image, rotation):
        functions = []
        args = []
        if spell.name == "Instant":
            functions.append(line)
            args.append([ctx,spell.y])
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
        super().collected(functions,args, rotation, ctx, image)

class Save(Identity):
    def __init__(spell, name, cantrip):
            super().__init__(name)
            if cantrip == 1:
                spell.y = 800
            else:
                spell.y = 900


    def draw(spell, ctx, image):
        functions = []
        args = []
        if spell.name == "None":
            return
        elif spell.name == "Dexterity":
            pass
        elif spell.name == "Constitution":
            pass
        elif spell.name == "Wisdom":
            pass
        elif spell.name == "Strength":
            strSave(ctx,spell.y)
        elif spell.name == "Charisma":
            pass
        elif spell.name == "Intelligence":
            pass
         




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
