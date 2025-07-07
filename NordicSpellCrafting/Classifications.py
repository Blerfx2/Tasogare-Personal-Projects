import pixie

"""TODO 1. In the spell class, make a function that takes the x and y values of each piece and does the correct calculation to rotate in the correct directions
        2. Make a second function that does the same thing for diagonals
        3. For the Deception, Shapechanging, and Detection stave heads would need an if statement to change line length.
        4. Make the components for the spell components (i.e. lines, curves, semicircles, etc.)
        5. Figure out how you want to mush the data together
        """
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")

fill = pixie.Paint(pixie.SOLID_PAINT)
fill.color = pixie.parse_color("#FFFFFF")


def smallCurve(image, x=0, y=0):
    path = pixie.parse_path(
    """
    M 900 200
    A 100 100 90 0 0 1100 200
    """
    )
    image.stroke_path(path, paint, stroke_width=20)
        
def bigCurve(image): # This is only used in the top most section of the initial rune
    path = pixie.parse_path(
        """
        M 1150 200
        A 150 150 90 0 1 850 200
        """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfRec(ctx):
    ctx.stroke_segment(850, 200, 850, 350)
    ctx.stroke_segment(840, 350, 1160, 350)
    ctx.stroke_segment(1150, 350, 1150, 200)

def smallHalfRec(ctx):
    ctx.stroke_segment(850, 200, 850, 325)
    ctx.stroke_segment(840, 325, 1160, 325)
    ctx.stroke_segment(1150, 325, 1150, 200)

def mainLine(ctx, x=0, y=0):
    ctx.stroke_segment(x, y, 1000, 1000)

def line(ctx, x1=0, y1=0, x2=0, y2=0):
    ctx.stroke_segment(910, 260, 1090, 260)

def sidewaysX(ctx, x=0, y=0):
    ctx.stroke_segment(920, 290, 1080, 220)
    ctx.stroke_segment(920, 220, 1080, 290)

def pointUp(ctx):
    ctx.stroke_segment(925, 280, 1006, 195)
    ctx.stroke_segment(994, 195, 1075, 280)

def pointDown(ctx):
    ctx.stroke_segment(925, 210, 1006, 295)
    ctx.stroke_segment(994, 295, 1075, 210)

def curveDown(image):
    path = pixie.parse_path(
    """
    M 925 275
    A 75 75 90 0 1 1075 275
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def lineCirc(image):
    path = pixie.parse_path(
    """
    M 950 250
    A 50 50 90 0 1 1050 250
    A 50 50 90 0 1 950 250
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def halfArrowR(ctx):
    ctx.stroke_segment(1005, 205, 1050, 310)

def keyblade(ctx):
    ctx.stroke_segment(1000, 210, 1080, 210)
    ctx.stroke_segment(1000, 240, 1080, 240)

def equals(ctx):
    ctx.stroke_segment(925, 240, 1075, 240)
    ctx.stroke_segment(925, 270, 1075, 270)

def flag(image):
    path = pixie.parse_path(
    """
    M 1000 220
    L 1060 270
    L 1000 320
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def diamond(image):
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

def antlers(ctx):
    ctx.stroke_segment(890, 250, 1110, 250)
    ctx.stroke_segment(900, 250, 900, 200)
    ctx.stroke_segment(945, 250, 945, 200)
    ctx.stroke_segment(1055, 250, 1055, 200)
    ctx.stroke_segment(1100, 250, 1100, 200)

def smallLineCirc(image):
    path = pixie.parse_path(
    """
    M 960 240
    A 30 30 90 0 1 1040 240
    A 30 30 90 0 1 960 240
    """
    )
    image.stroke_path(path, paint, stroke_width=20)

def smallFillCirc(image):
    path = pixie.parse_path(
    """
    M 965 240
    A 20 20 90 0 1 1035 240
    A 20 20 90 0 1 965 240
    """
    )

    image.fill_path(path, fill)
    smallLineCirc(image)

def doubleDots(image):
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

def shieldedOrb(image):
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

def strSave(ctx):
    ctx.stroke_rect(900, 900, 200, 200)
    ctx.stroke_rect(950, 950, 100, 100)

class Identity:
    def __init__(spell, name):
        spell.name = name
        spell.damage = 0
        spell.x = 1000 # x and y are more like the center of where to put any symbol
        spell.y = 275



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