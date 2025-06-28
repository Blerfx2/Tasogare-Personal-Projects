import pixie

"""TODO 1. In the spell class, make a function that takes the x and y values of each piece and does the correct calculation to rotate in the correct directions
        2. Make a second function that does the same thing for diagonals
        3. Make the components for the spell components (i.e. lines, curves, semicircles, etc.)
        4. Figure out how you want to mush the data together
        """
paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")


def smallCurve(image, x, y):
    path = pixie.parse_path(
    """
    M 900 200
    A 100 100 90 0 0 1100 200
    """
    )
    image.stroke_path(path, paint, stroke_width=20)
        
def bigCurve(image, x, y):
    path = pixie.parse_path(
        """
        M 1150 200
        A 150 150 90 0 1 850 200
        """
    )
    image.stroke_path(path, paint, stroke_width=20)

def mainLine(ctx, x, y):
    ctx.stroke_segment(x, y, 1000, 1000)

def line(ctx, x1, y1, x2, y2):
    ctx.stroke_segment(905, 500, 1095, 500)

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
    mainLine(ctx)
    bigCurve(image)


    ctx.line_width = 20
    ctx.stroke_segment(920, 290, 1080, 220)
    ctx.stroke_segment(920, 220, 1080, 300)



    image.write_file("NordicSpellCrafting/trying.png")


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