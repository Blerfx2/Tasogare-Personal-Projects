
git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

class Spell:
    def __init__(spell, comp1, comp2, comp3, comp4):
        spell.name = comp1
        spell.school = comp2
        spell.time = comp3
        spell.blurb = comp4

    def deets(spell):
        print(f"You want to know more about {spell.name}?\nWell it is in the school of {spell.school} and it takes about a {spell.time} to cast!\nHere is some more info if you are curious\n{spell.blurb}")

if __name__ == "__main__":
    test = Spell("eldritch blast", "evocation","reaction", "You think you need to know more punk?" )  
    test.deets()