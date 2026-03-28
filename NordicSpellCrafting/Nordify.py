from Classifications import School, Range, Duration, Save, mainLine, collected
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
        spell.save = Save(save, int(lvl))
        spell.level = int(lvl)
        spell.drawSpell()

    

    def drawSpell(spell):
        image = pixie.Image(2000,2000)
        image.fill(pixie.Color(1, 1, 1, 1))

        ctx = image.new_context()
        ctx.stroke_style = paint
        ctx.fill_style = fill
        ctx.line_width = 25
        # TODO So this would probably be best to get thrown into a try except block
        if spell.level == 0:
            mainLine(ctx, 0)
            ctx.line_width = 20
            c1, c2 = spell.school.draw(ctx,image,0)
            c3, c4 = spell.range.draw(ctx,image,0)
            c5, c6 = spell.duration.draw(ctx,image,0)
            c1 += c3 + c5
            c2 += c4 + c6
            collected(c1, c2, 0, ctx, image)
            spell.save.draw(ctx)

        else:
            mainLine(ctx, 1)
            if spell.level == 1:
                ctx.line_width = 20
                c1, c2 = spell.school.draw(ctx,image,1)
                c3, c4 = spell.range.draw(ctx,image,1)
                c5, c6 = spell.duration.draw(ctx,image,1)
                c1 += c3 + c5
                c2 += c4 + c6
                collected(c1, c2, 1, ctx, image)
                spell.save.draw(ctx)
            elif spell.level in [2,4,7]:
                mainLine(ctx,2)
                ctx.line_width = 20
                c1, c2 = spell.school.draw(ctx,image,2)
                c3, c4 = spell.range.draw(ctx,image,2)
                c5, c6 = spell.duration.draw(ctx,image,2)
                c1 += c3 + c5
                c2 += c4 + c6
                collected(c1, c2, 2, ctx, image)
                spell.save.draw(ctx)
            elif spell.level == 9:
                mainLine(ctx,2)
                ctx.line_width = 20
                c1, c2 = spell.school.draw(ctx,image,3)
                c3, c4 = spell.range.draw(ctx,image,3)
                c5, c6 = spell.duration.draw(ctx,image,3)
                c1 += c3 + c5
                c2 += c4 + c6
                collected(c1, c2, 3, ctx, image)
                spell.save.draw(ctx)
            else:
                mainLine(ctx,2)
                ctx.line_width = 20
                c1, c2 = spell.school.draw(ctx,image,3)
                c3, c4 = spell.range.draw(ctx,image,3)
                c5, c6 = spell.duration.draw(ctx,image,3)
                c1 += c3 + c5
                c2 += c4 + c6
                collected(c1, c2, 3, ctx, image)
                spell.save.draw(ctx)

        image.write_file(f"NordifiedSpells/{spell.name}.png")
        #image.write_file(f"NordifiedSpells/{spell.level}/{spell.name}.png")

        
        
if __name__ == "__main__":
    Spell('Test', 'DMG Bludgeoning', '10 Feet', '1 Hour', 'Charisma', 6)