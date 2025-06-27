import pixie

"""TODO 1. In the spell class, make a function that takes the x and y values of each piece and does the correct calculation to rotate in the correct directions
        2. Make a second function that does the same thing for diagonals
        3. Make the components for the spell components (i.e. lines, curves, semicircles, etc.)
        4. Figure out how you want to mush the data together
        """

class Type:
    def __init__(spell):
        pass



def main():
    image = pixie.Image(2000,2000)
    image.fill(pixie.Color(75, 5, 5, 1))

    paint = pixie.Paint(pixie.SOLID_PAINT)
    paint.color = pixie.parse_color("#000000")

    ctx = image.new_context()
    ctx.stroke_style = paint
    ctx.line_width = 25

    ctx.stroke_segment(1000, 200, 1000, 1000)

    spath = pixie.parse_path(
        """
        M 900 200
        A 100 100 90 0 0 1100 200
        M 1150 200
        A 150 150 90 0 1 850 200
        """
    )
    ctx.line_width = 20
    ctx.stroke_segment(905, 500, 1095, 500)
    ctx.stroke_segment(905, 700, 1095, 700)
    ctx.stroke_rect(900, 900, 200, 200)
    ctx.stroke_rect(950, 950, 100, 100)

    image.stroke_path(spath, paint, stroke_width=20)

    # Sideways

    ctx.stroke_segment(1000, 1000, 1800, 1000)

    spath = pixie.parse_path(
        """
        M 1800 900
        A 100 100 0 0 0 1800 1100
        M 1800 1150
        A 150 150 0 0 1 1800 850
        """
    )
    ctx.line_width = 20
    ctx.stroke_segment(1500, 905, 1500, 1095)
    ctx.stroke_segment(1300, 905, 1300, 1095)
    image.stroke_path(spath, paint, stroke_width=20)
    # cimage = image.copy()
    # cimage.flip_vertical()
    # cimage = cimage.sub_image(0,1000,2000,1000)
    # image.draw(cimage)
    image.write_file("trying.png")


if __name__ == "__main__":
    main()