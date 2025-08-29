from Classifications import School, Range, Duration, Save, mainLine
import pixie

paint = pixie.Paint(pixie.SOLID_PAINT)
paint.color = pixie.parse_color("#000000")

fill = pixie.Paint(pixie.SOLID_PAINT)
fill.color = pixie.parse_color("#FFFFFF")

class Spell:
    def __init__(spell, name, tag, dist, dur, save, lvl):
        spell.name = name
        spell.school = School(tag)
        spell.range = Range(dist)
        spell.duration = Duration(dur)
        if lvl == 0:
            spell.save = Save(save, 1)
        else:
            spell.save = Save(save, 0)
        spell.level = int(lvl)
        spell.drawSpell()

    

    def drawSpell(spell):
        image = pixie.Image(2000,2000)
        image.fill(pixie.Color(1, 1, 1, 1))

        ctx = image.new_context()
        ctx.stroke_style = paint
        ctx.line_width = 25
        # TODO So this would probably be best to get thrown into a try except block
        if spell.level == 0:
            mainLine(ctx, 0)
            ctx.line_width = 20
            spell.school.draw(ctx,image,0)
            spell.range.draw(ctx,image,0)
            spell.duration.draw(ctx,image,0)
            spell.save.draw(ctx,image)

        else:
            mainLine(ctx, 1)
            if spell.level == 1:
                ctx.line_width = 20
                spell.school.draw(ctx,image,1)
                spell.range.draw(ctx,image,1)
                spell.duration.draw(ctx,image,1)
                spell.save.draw(ctx,image)
            elif spell.level in [2,4,7]:
                mainLine(ctx,2)
                ctx.line_width = 20
                spell.school.draw(ctx,image,2)
                spell.range.draw(ctx,image,2)
                spell.duration.draw(ctx,image,2)
                spell.save.draw(ctx,image)
            else:
                mainLine(ctx,2)
                ctx.line_width = 20
                spell.school.draw(ctx,image,4)
                spell.range.draw(ctx,image,4)
                spell.duration.draw(ctx,image,4)
                spell.save.draw(ctx,image)

        image.write_file(f"NordifiedSpells/{spell.name}.png")

        
        
if __name__ == "__main__":
    Spell('Acid Splash', 'DMG Acid', '60 Feet', 'Instant', 'Strength', 3)