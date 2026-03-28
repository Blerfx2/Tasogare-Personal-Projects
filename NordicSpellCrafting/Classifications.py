import pixie

angle_degrees = 45
angle_radians = angle_degrees * (3.14159 / 180)


"""TODO 1. Make the horizontal and diagonls of each function
        2. Figure out how to adjust for 9th level spells
        3. May have to change ctx fill rules
        """
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")

fill = pixie.Paint(pixie.SOLID_PAINT)
fill.color = pixie.parse_color("#FFFFFF")


def smallCurve(ctx, y, rotation=0):
# y should normally be the top of the segment
    if rotation == 3:
        smallCurve(ctx, y, 0)
        smallCurve(ctx, y, 1)
        smallCurve(ctx, y, 2)
    elif rotation == 2:
        y2 = 2000 - y
        path = pixie.parse_path(
        f"""
        M {y} 900
        A 100 100 90 0 1 {y} 1100
        M {y2} 900
        A 100 100 90 0 0 {y2} 1100
        """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
            y = 2000 - y
        path = pixie.parse_path(
        f"""
        M 900 {y}
        A 100 100 90 0 {rotation} 1100 {y}
        """
        )
        ctx.path_stroke(path)
        
def bigCurve(ctx, rotation = 0): # Stave only
    y = 200
    if rotation == 3:
        bigCurve(ctx,0)
        bigCurve(ctx,1)
        bigCurve(ctx,2)
    elif rotation == 2:
        y2 = 2000 - y
        path = pixie.parse_path(
            f"""
            M {y} 1150
            A 150 150 90 0 0 {y} 850
            M {y2} 1150
            A 150 150 90 0 1 {y2} 850
            """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
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
        ctx.path_stroke(path)

def staveRec(ctx, rotation=0): # Stave only
    y = 200
    if rotation == 0:
        y2 = y + 150
    else:
        y = 2000 - y
        y2 = y - 150
    ctx.stroke_segment(850, y, 850, y2)
    ctx.stroke_segment(840, y2, 1160, y2)
    ctx.stroke_segment(1150, y2, 1150, y)

def smallStaveRec(ctx, rotation=0): # Stave only
    if rotation == 3:
        smallStaveRec(ctx,0)
        smallStaveRec(ctx,1)
        smallStaveRec(ctx,2)
    elif rotation == 2:
        x = 200
        x2 = x + 125
        x3 = 2000 - x
        x4 = x3 - 125
        ctx.stroke_segment(x, 875, x2, 875)
        ctx.stroke_segment(x2, 865, x2, 1135)
        ctx.stroke_segment(x2, 1125, x, 1125)
        ctx.stroke_segment(x3, 875, x4, 875)
        ctx.stroke_segment(x4, 865, x4, 1135)
        ctx.stroke_segment(x4, 1125, x3, 1125)
    else:
        y = 200
        if rotation == 0:
            y2 = y + 125
        else:
            y = 2000 - y
            y2 = y - 125
        ctx.stroke_segment(875, y, 875, y2)
        ctx.stroke_segment(865, y2, 1135, y2)
        ctx.stroke_segment(1125, y2, 1125, y)

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
    if rotate == 3:
        line(ctx,pos,0)
        line(ctx,pos,1)
        line(ctx,pos,2)
    elif rotate == 1:
        ctx.stroke_segment(910, 2000-pos, 1090, 2000-pos)
    elif rotate == 2:
        ctx.stroke_segment(pos, 910, pos, 1090)
        ctx.stroke_segment(2000-pos, 910, 2000-pos, 1090)
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
    if rotation == 3:
        pointUp(ctx,y,0)
        pointUp(ctx,y,1)
        pointUp(ctx,y,2)
    elif rotation == 2:
        x = y
        x2 = x + 85
        x3 = 2000 - x
        x4 = x3 - 85
        ctx.stroke_segment(x2, 925, x,1006)
        ctx.stroke_segment(x, 994, x2, 1075)
        ctx.stroke_segment(x4, 925, x3,1006)
        ctx.stroke_segment(x3, 994, x4, 1075)
    else:
        if rotation == 0:
            y2 = y + 85
        else:
            y = 2000 - y
            y2 = y - 85
        ctx.stroke_segment(925, y2, 1006, y)
        ctx.stroke_segment(994, y, 1075, y2)

def pointDown(ctx, y, rotation=0):
# Pass in lower value. Usually is 10 more than base
    if rotation == 3:
        pointDown(ctx,y,0)
        pointDown(ctx,y,1)
        pointDown(ctx,y,2)
    elif rotation == 2:
        x = y
        x2 = x + 85
        x3 = 2000 - x
        x4 = x3 - 85
        ctx.stroke_segment(x, 925, x2,1006)
        ctx.stroke_segment(x2, 994, x, 1075)
        ctx.stroke_segment(x3, 925, x4,1006)
        ctx.stroke_segment(x4, 994, x3, 1075)
    else:
        if rotation == 0:
            y2 = y + 85
        else:
            y = 2000 - y
            y2 = y - 85
        ctx.stroke_segment(925, y, 1006, y2)
        ctx.stroke_segment(994, y2, 1075, y)

def curveDown(ctx, y, rotation=0):
# Usually y is 75 more than base
    if rotation == 3:
        curveDown(ctx, y, 0)
        curveDown(ctx, y, 1)
        curveDown(ctx, y, 2)
    elif rotation == 2:
        y2 = 2000 - y
        path = pixie.parse_path(
        f"""
        M {y} 925
        A 75 75 90 0 0 {y} 1075
        M {y2} 925
        A 75 75 90 0 1 {y2} 1075
        """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
            y = 2000 - y
            rotation = 0
        else:
            rotation = 1
        path = pixie.parse_path(
        f"""
        M 925 {y}
        A 75 75 90 0 {rotation} 1075 {y}
        """
        )
        ctx.path_stroke(path)

def curveUp(ctx, y, rotation=0):
# y should normally be the top of the segment
    if rotation == 3:
        curveUp(ctx, y, 0)
        curveUp(ctx, y, 1)
        curveUp(ctx, y, 2)
    elif rotation == 2:
        y2 = 2000 - y
        path = pixie.parse_path(
        f"""
        M {y} 925
        A 75 75 90 0 1 {y} 1075
        M {y2} 925
        A 75 75 90 0 0 {y2} 1075
        """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
            y = 2000 - y
        path = pixie.parse_path(
        f"""
        M 925 {y}
        A 75 75 90 0 {rotation} 1075 {y}
        """
        )
        ctx.path_stroke(path)

def lineCirc(ctx, y, rotation=0):
# y is usually 50 from base?
    if rotation == 3:
        lineCirc(ctx,y,0)
        lineCirc(ctx,y,1)
        lineCirc(ctx,y,2)
    elif rotation == 2:
        x = y
        x2 = 2000 - y

        path = pixie.parse_path(
        f"""
        M {x} 950
        A 50 50 90 0 1 {x} 1050
        A 50 50 90 0 1 {x} 950
        M {x2} 950
        A 50 50 90 0 1 {x2} 1050
        A 50 50 90 0 1 {x2} 950
        """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
            y = 2000 - y

        path = pixie.parse_path(
        f"""
        M 950 {y}
        A 50 50 90 0 1 1050 {y}
        A 50 50 90 0 1 950 {y}
        """
        )
        ctx.path_stroke(path)

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
    if rotation == 3:
         keyblade(ctx, y, 0)
         keyblade(ctx, y, 1)
         keyblade(ctx, y, 2)
    if rotation == 2:
        x = 1080
        y2 = y + 30
        x2 = 920
        y3 = 2000 - y
        y4 = y3 - 30
        ctx.stroke_segment(y, 1000, y, x2)
        ctx.stroke_segment(y2, 1000, y2, x2)
        ctx.stroke_segment(y3, 1000, y3, x)
        ctx.stroke_segment(y4, 1000, y4, x)
    else:
        if rotation == 0:
            x = 1080
            y2 = y + 30
        else:
            x = 920
            y = 2000 - y
            y2 = y - 30
        ctx.stroke_segment(1000, y, x, y)
        ctx.stroke_segment(1000, y2, x, y2)

def halfLine(ctx, y, rotation=0):
# Pass in lower value. Usually is 10 more than base
    if rotation == 3:
         halfLine(ctx, y, 0)
         halfLine(ctx, y, 1)
         halfLine(ctx, y, 2)
    if rotation == 2:
        x = 1080
        y2 = 2000 - y
        x2 = 920
        ctx.stroke_segment(y, 1000, y, x2)
        ctx.stroke_segment(y2, 1000, y2, x)
    else:
        if rotation == 0:
            x = 1080
            y2 = y + 30
        else:
            x = 920
            y = 2000 - y
        ctx.stroke_segment(1000, y, x, y)

def equals(ctx, y, rotation=0):
# Pass in lower value. Usually is 40 more than base
    if rotation == 0:
        y2 = y + 30
    else:
        y = 2000 - y
        y2 = y - 30
    ctx.stroke_segment(950, y, 1050, y)
    ctx.stroke_segment(950, y2, 1050, y2)

def flag(ctx, y, rotation=0):
    x = 1000
    if rotation == 1:
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
    ctx.path_stroke(path)

def diamond(ctx, y, rotation=0):
    x, x2, x3 = 1000, 950, 1050
    if rotation == 1:
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
    ctx.path_stroke(path)

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

def smallLineCirc(ctx, y, rotation=0):
# y is usually 40 from base
    if rotation == 3:
        smallLineCirc(ctx,y,0)
        smallLineCirc(ctx,y,1)
        smallLineCirc(ctx,y,2)
    elif rotation == 2:
        x = y
        x2 = 2000 - y

        path = pixie.parse_path(
        f"""
        M {x} 960
        A 30 30 90 0 1 {x} 1040
        A 30 30 90 0 1 {x} 960
        M {x2} 960
        A 30 30 90 0 1 {x2} 1040
        A 30 30 90 0 1 {x2} 960
        """
        )
        ctx.path_stroke(path)
    else:
        if rotation == 1:
            y = 2000 - y

        path = pixie.parse_path(
        f"""
        M 960 {y}
        A 30 30 90 0 1 1040 {y}
        A 30 30 90 0 1 960 {y}
        """
        )
        ctx.path_stroke(path)

def smallFillCirc(ctx, y, rotation=0):
# y is usually 40 from base
    if rotation == 3:
        smallFillCirc(ctx,y,0)
        smallFillCirc(ctx,y,1)
        smallFillCirc(ctx,y,2)
    elif rotation == 2:
        y2 = 2000 - y
        path = pixie.parse_path(
        f"""
        M {y} 965
        A 20 20 90 0 1 {y} 1035
        A 20 20 90 0 1 {y} 965
        M {y2} 965
        A 20 20 90 0 1 {y2} 1035
        A 20 20 90 0 1 {y2} 965
        """
        )
        ctx.path_fill(path)
        smallLineCirc(ctx,y,2)
    else:
        if rotation == 1:
            y = 2000 - y

        path = pixie.parse_path(
        f"""
        M 965 {y}
        A 20 20 90 0 1 1035 {y}
        A 20 20 90 0 1 965 {y}
        """
        )
        ctx.fill_style = fill
        ctx.path_fill(path)
        smallLineCirc(ctx,y)

def doubleDots(ctx, y, rotation=0):
# y is usually 100 from base
    if rotation == 1:
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
    ctx.path_fill(path)

def shieldedOrb(ctx, y, rotation=0):
# y is usually 50 from base
    if rotation == 1:
        y = 2000 - y
    path = pixie.parse_path(
    f"""
    M 945 {y}
    A 55 55 90 0 1 1055 {y}
    A 55 55 90 0 1 945 {y}
    """
    )

    ctx.path_fill(path)
    path = pixie.parse_path(
    """
    M 965 215
    A 50 50 90 1 0 1035 215
    """
    )
    ctx.path_stroke(path)
    path = pixie.parse_path(
    """
    M 980 255
    A 20 20 90 0 1 1020 255
    A 20 20 90 0 1 980 255

    """
    )
    ctx.path_fill(path)

def strSave(ctx, y):
    y2 = y + 50
    ctx.stroke_rect(900, y, 200, 200)
    ctx.stroke_rect(950, y2, 100, 100)

def dexSave(ctx, y):
    ctx.stroke_rect(900, y, 200, 200)

def conSave(ctx, y):
    ctx.fill_rect(900, y, 200, 200)
    ctx.stroke_rect(900, y, 200, 200)

def intSave(ctx, y):
    path = pixie.parse_path(
    f"""
    M 900 {y}
    A 100 100 90 0 1 1100 {y}
    A 100 100 90 0 1 900 {y}
    M 930 {y}
    A 65 65 90 0 1 1070 {y}
    A 65 65 90 0 1 930 {y}
    """
    )
    ctx.path_stroke(path)

def wisSave(ctx, y):
    path = pixie.parse_path(
    f"""
    M 900 {y}
    A 100 100 90 0 1 1100 {y}
    A 100 100 90 0 1 900 {y}
    """
    )
    ctx.path_stroke(path)

def chaSave(ctx, y):
    path = pixie.parse_path(
    f"""
    M 900 {y}
    A 100 100 90 0 1 1100 {y}
    A 100 100 90 0 1 900 {y}
    """
    )
    ctx.path_fill(path)
    ctx.path_stroke(path)

def hugeCirc(ctx):
    path = pixie.parse_path(
    """
    M 350 1000 
    A 650 650 90 0 1 1650 1000
    A 650 650 90 0 1 350 1000
    """
    )
    ctx.path_stroke(path)

def hugeDoubleCirc(ctx):
    path = pixie.parse_path(
    """
    M 350 1000 
    A 650 650 90 0 1 1650 1000
    A 650 650 90 0 1 350 1000
    M 400 1000 
    A 600 600 90 0 1 1600 1000
    A 600 600 90 0 1 400 1000
    """
    )
    ctx.path_stroke(path)

def hugeSquare(ctx):
    ctx.stroke_rect(500, 500, 1000, 1000)

def hugeDoubleSquare(ctx):
    ctx.stroke_rect(450, 450, 1100, 1100)
    ctx.stroke_rect(500, 500, 1000, 1000)

class Identity:
    def __init__(spell, name):
        spell.name = name
         

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
            if spell.name in ["Bludgeoning", "Piercing"]:
                functions.append(smallStaveRec)
                args.append([ctx])
                if spell.name == "Bludgeoning":
                    functions.append(lineCirc)
                    args.append([ctx,spell.y+50])
                elif spell.name == "Piercing":
                    functions.append(pointUp)
                    args.append([ctx,spell.y-10])
                elif spell.name == "Slashing":
                    pass
            elif spell.name == "Slashing":
                functions.append(staveRec)
                args.append([ctx])
            elif spell.name == "Force":
                functions.append(staveRec)
                args.append([ctx])
                functions.append(equals)
                args.append([ctx,spell.y+40])
            
            else:
                functions.append(bigCurve)
                args.append([ctx])
                if spell.name == "Fire":
                    functions.append(pointUp)
                    args.append([ctx,spell.y-5])
                elif spell.name == "Cold":
                    functions.append(line)
                    args.append([ctx, spell.y+60])
                elif spell.name == "Lightning":
                    functions.append(smallCurve)
                    args.append([ctx,spell.y])
                elif spell.name == "Thunder":
                    functions.append(curveDown)
                    args.append([ctx,spell.y+75])
                elif spell.name == "Acid":
                    functions.append(keyblade)
                    args.append([ctx,spell.y+10])
                elif spell.name == "Poison":
                    functions.append(halfArrowR)
                    args.append([ctx,spell.y+5])
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
        return functions, args
        
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
            functions.append(curveDown)
            args.append([ctx,spell.y])
        elif spell.name == "5 Feet":
            functions.append(halfLine)
            args.append([ctx,spell.y])
        elif spell.name == "10 Feet":
            functions.append(doubleDots)
            args.append([ctx,spell.y])
        elif spell.name == "30 Feet":
            pass
        elif spell.name == "60 Feet":
            functions.append(smallCurve)
            args.append([ctx, spell.y])
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
            functions.append(smallFillCirc)
            args.append([ctx, spell.y])

        return functions, args

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
            functions.append(curveUp)
            args.append([ctx, spell.y])
        elif spell.name == "1 Minute":
            functions.append(curveDown)
            args.append([ctx, spell.y+75])
        elif spell.name == "10 Minutes":
            functions.append(pointDown)
            args.append([ctx, spell.y])
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

        return functions, args

class Save(Identity):
    def __init__(spell, name, level):
            super().__init__(name)
            if level >= 1:
                spell.y = 900
            else:
                spell.y = 800
            spell.level = level


    def draw(spell, ctx):
        if spell.name == "None":
            return
        elif spell.name == "Dexterity":
            dexSave(ctx,spell.y)
        elif spell.name == "Constitution":
            conSave(ctx,spell.y)
        elif spell.name == "Wisdom":
            wisSave(ctx,spell.y+100)
        elif spell.name == "Strength":
            strSave(ctx,spell.y)
        elif spell.name == "Charisma":
            chaSave(ctx,spell.y+100)
        elif spell.name == "Intelligence":
            intSave(ctx,spell.y+100)

        if spell.level < 4:
            return
        elif spell.level < 6:
            hugeCirc(ctx)
        elif spell.level == 6:
            hugeDoubleCirc(ctx)
        elif spell.level < 9:
            hugeSquare(ctx)
        elif spell.level == 9:
            hugeDoubleSquare(ctx)
        
def collected(functions, args, rotations, ctx, image):
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
    if rotations == 3:
        ctx.translate(cx, cy)
        ctx.rotate(-angle_radians)
        ctx.translate(-cx, -cy)