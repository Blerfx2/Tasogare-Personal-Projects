import random

class Species:
    def __init__(self):
        self.gender = random.choice(["Male","Female"])
        self.firstName = random.choice(self.nameLists[self.gender])
        self.lastName = random.choice(self.nameLists["Last"])
        self.fullName = self.firstName + " " + self.lastName

    def pickHair(self):
        hairLength = ["long", "short", "shoulder length"]
        hairColor = ["brown", "brunette", "blonde", "orange", "red", "strawberry blonde", "black"]
        hairType = ["straight", "curly", "wavy", "no", "braided", "coiled"]
        chosenHair = random.choice(hairType)
        if chosenHair != "no":
            return f"{random.choice(hairLength)}, {chosenHair}, {random.choice(hairColor)} hair,"
        else:
            return f"{chosenHair} hair,"
        
    def pickHorns(self):
        horns = ["curved", "chipped", "embroidered", "ram", "goat", "short", "sharp", "stubbed", "split", "merged", "crowned", "spiraled"]
        selected = random.choice(horns)
        if self.species == "Tiefling":
            return self.pickHair() + f" {selected} horns,"
        else:
            return f" {selected} horns,"
    
class Elf(Species):
    def __init__(self):
        self.nameLists = {
                "Male": ["Alorin", "Caeloy", "Daelin", "Ealor", "Faelin", "Galadriy", "Ilmarin", "Kaelor", "Laethin", 
            "Mirathor", "Naeloy", "Orisin", "Phaelin", "Quentor", "Raevin", "Saeloy", "Thaerin", "Ulmarin", 
            "Vaelor", "Wyndin", "Zelorin", "Amarin", "Briathor", "Cyrelin", "Drathor", "Ellorin", "Fenor", "Gealin", "Haelin", "Irathor"
            ],
                "Female": ["Aelindra", "Caelith", "Daelis", "Elowen", "Faelina", "Galadriel", "Ilmariel", "Kaelara", 
            "Laethwen", "Mirathiel", "Naelith", "Oriana", "Phaelina", "Quenthia", "Raevyn", "Saelina", 
            "Thaerwen", "Ulmariel", "Vaelora", "Wyndara", "Zelindra", "Amariel", "Brialeth", "Cyrelina", 
            "Draleth", "Ellorwen", "Fenorin", "Gealina", "Haelwen", "Irathiel"
            ],
                "Last": ["Silvious", "Tollic", "Magaris", "Ullavel", "Crosious", "Hallovel", "Dumaris", 
            "Numaris", "Bellovic", "Elenarel", "Yulel", "Usarious", "Alasaric", "Himmel", 
            "Tollevic", "Kosorious", "Nolious", "Glasic", "Nosorious", "Baseek", 
            "Conorious", "Calel", "Insivious", "Zoramic", "Volous", "Junipious", 
            "Jersious", "Garabel", "Nosorious", "Renolos"]}
        super().__init__()
        self.species = "Elf"
        self.skin = random.choice(["silvery", "coppery", "golden", "pale gray"])
        self.height = f"{random.randint(4,6)}'{random.randint(0,11)}\""
        self.hair = self.pickHair()

class Human(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Aiden", "Cian", "Eamon", "Gareth", "Kieran", "Niall", "Owen", "Seamus", "Tadhg", 
        "Brendan", "Connor", "Declan", "Liam", "Ronan", "Finn", "Ciaran", "Donal", 
        "Padraig", "Ruairi", "Cathal", "Cormac", "Diarmuid", "Eoghan", "Fergus", "Lorcan", 
        "Oisin", "Rory", "Tiernan", "Conall", "Daithi"
            ],
            "Female": [
        "Brigid", "Deirdre", "Fiona", "Grainne", "Maeve", "Nuala", "Rhiannon", "Siobhan", 
        "Una", "Aisling", "Eilish", "Sorcha", "Ciara", "Erin", "Bronagh", "Aoife", 
        "Caoimhe", "Niamh", "Roisin", "Orla", "Sinead", "Clodagh", "Mairead", "Saoirse", 
        "Brigit", "Moira", "Nessa", "Caitlin", "Aine", "Riona"
        ],
            "Last": [
        "Ailbhe", "Branagh", "Caomhan", "Dáire", "Eibhear", "Fiachra", "Goibniu", "Herne", 
        "Iorwerth", "Kai", "Loghain", "Mordha", "Niamhan", "Oisean", "Phelan", "Rhonwen", 
        "Scáthach", "Taranis", "Uilliam", "Vercingetorix", "Wynne", "Aldith", "Bevan", 
        "Cyrus", "Drustan", "Eogain", "Finnegan", "Gwydion", "Heremon", "Isolde", 
        "Kedric", "Lorcan", "Merrion", "Nuada", "Ossian"
            ]}
        
        super().__init__()
        self.species = "Human"
        self.skin = f"{random.choice(["pale ", "light ", "", "darker ", "tanned "])} {random.choice(["white", "brown", "dark"])}"
        self.height = f"{random.randint(4,6)}'{random.randint(0,11)}\""
        self.hair = self.pickHair()

class Dwarf(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Durin", "Thorin", "Balin", "Dwalin", "Ragnar", "Torin", "Bromir", "Gimrok", 
        "Dorak", "Thorak", "Brumir", "Gimli", "Durak", "Balthor", "Thrain", "Rogar", 
        "Borin", "Dorgrin", "Thorgar", "Bofur", "Bombur", "Dain", "Torgrim", "Rurik", 
        "Gorim", "Brakk", "Durok", "Thorek", "Rodrik", "Borak"
        ],
            "Female": [
        "Delga", "Tordis", "Borgny", "Dagmar", "Ragna", "Torunn", "Brynhild", "Gerdur", 
        "Drifa", "Thora", "Brunhild", "Gunnhild", "Dagny", "Bodil", "Thorunn", "Ragnhild", 
        "Borgrun", "Dagna", "Thordis", "Brynja", "Borghild", "Dalla", "Torvi", "Rangrid", 
        "Gudrun", "Brenna", "Dura", "Thorgerd", "Runa", "Brita"
        ],
            "Last": ["Guldock", "Timrock", "Masar", "Borite", "Garem", "Deravish", "Hamaram", 
        "Trobadar", "Bruvite", "Noravam", "Stovack", "Trozom", "Florgar", "Garavar", 
        "Smoldarock", "Vimite", "Crustite", "Inovock", "Tombovite", "Restarim", 
        "Yunuvock", "Emberite", "Vilock", "Runavite", "Groonish", "Bravite", 
        "Iodite", "Philosophom", "Terravite", "Gildar"]}
    
        super().__init__()
        self.species = "Dwarf"
        self.skin = f"{random.choice(["pale ", "light ", "", "darker ", "tanned "])} {random.choice(["white", "brown", "dark"])}"
        self.height = f"4'{random.randint(0,11)}\""
        self.hair = self.pickHair()

class Halfling(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Oliver", "William", "James", "Benjamin", "Lucas", "Henry", "Alexander", "Samuel", 
        "Daniel", "Jack", "Mason", "Ethan", "Noah", "Isaac", "Owen", "Thomas", "Charles", 
        "Matthew", "Joseph", "Andrew", "David", "Christopher", "Nathan", "Joshua", "Ryan", 
        "Brandon", "Kevin", "Tyler", "Justin", "Eric"
        ],
            "Female": [
        "Emma", "Sophia", "Charlotte", "Amelia", "Mia", "Evelyn", "Harper", "Abigail", 
        "Emily", "Lily", "Grace", "Chloe", "Zoe", "Violet", "Ruby", "Hannah", "Eleanor", 
        "Natalie", "Audrey", "Sophie", "Claire", "Lucy", "Stella", "Hazel", "Penelope", 
        "Nora", "Alice", "Piper", "Willow", "Ellie"
        ],
            "Last": [
        "Greenhill", "Riverbend", "Brightmeadow", "Stoneburrow", "Sweetriver", "Goldcliff", 
        "Merrybrook", "Underhill", "Goodbarrow", "Thornfield", "Sunnydale", "Rosecreek", 
        "Quickbrook", "Littlehill", "Roundmeadow", "Softriver", "Gentleburrow", "Proudcliff", 
        "Kindbrook", "Warmhollow", "Brightdale", "Clearriver", "Softmeadow", "Highcliff", 
        "Deepburrow", "Greenbrook", "Sunhill", "Clearmeadow", "Swiftriver", "Gentlehill"
        ]}
        
        super().__init__()
        self.species = random.choice(["Halfling", "Gnome"])
        self.skin = f"{random.choice(["pale ", "light ", "", "darker ", "tanned "])} {random.choice(["white", "brown", "dark"])}"
        self.height = f"3'{random.randint(0,11)}\""
        self.hair = self.pickHair()

class Tiefling(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Valor", "Justice", "Honor", "Courage", "Fury", "Zeal", "Pride", "Sorrow", 
        "Tempest", "Havoc", "Vengeance", "Strife", "Wrath", "Dread", "Torment", 
        "Chaos", "Ruin", "Malice", "Scorn", "Conquest", "Triumph", "Spite", "Defy", 
        "Rage", "Agony", "Doom", "Grit", "Rebel", "Prowess", "Fierce",
        "Durin", "Thorin", "Balin", "Ragnar", "Torin", "Gimli", "Thrain", "Dain",
        "Oliver", "William", "James", "Benjamin", "Lucas", "Henry", "Samuel",
        "Aiden", "Cian", "Eamon", "Kieran", "Niall", "Seamus", "Finn", "Ronan",
        "Bulgrush", "Torakesh", "Dakresh", "Goramesh", "Koresh", "Toresh",
        "Garem", "Koshin", "Salim", "Torin"
        ],
            "Female": [
        "Hope", "Mercy", "Faith", "Glory", "Virtue", "Peace", "Destiny", "Fortune", 
        "Grace", "Harmony", "Liberty", "Passion", "Serenity", "Truth", "Wisdom", 
        "Ambition", "Charity", "Delight", "Elation", "Fervor", "Jubilee", "Kindness", 
        "Loyalty", "Prudence", "Solace", "Bliss", "Joy", "Remedy", "Clarity", "Devotion",
        "Delga", "Tordis", "Borgny", "Ragna", "Torunn", "Brynhild", "Drifa", "Thora",
        "Emma", "Sophia", "Charlotte", "Amelia", "Mia", "Evelyn", "Harper",
        "Brigid", "Deirdre", "Fiona", "Grainne", "Maeve", "Nuala", "Siobhan", "Aisling",
        "Balasha", "Torasha", "Dakasha", "Gorasha", "Korasha", "Terasha",
        "Gara", "Kosha", "Sala", "Tora"
        ],
            "Last": ["Silvious", "Tollic", "Magaris", "Ullavel", "Crosious", "Hallovel", "Dumaris", 
    "Numaris", "Bellovic", "Elenarel", "Yulel", "Usarious", "Alasaric", "Himmel", 
    "Tollevic", "Kosorious", "Nolious", "Glasic", "Nosorious", "Baseek", "Conorious", 
    "Calel", "Insivious", "Zoramic", "Volous", "Junipious", "Jersious", "Garabel", 
    "Nosorious", "Renolos",
    "Guldock", "Timrock", "Masar", "Borite", "Garem", "Deravish", "Hamaram", 
    "Trobadar", "Bruvite", "Noravam", "Stovack", "Trozom", "Florgar", "Garavar", 
    "Smoldarock", "Vimite", "Crustite", "Inovock", "Tombovite", "Restarim", 
    "Yunuvock", "Emberite", "Vilock", "Runavite", "Groonish", "Bravite", "Iodite", 
    "Philosophom", "Terravite", "Gildar",
    "Greenhill", "Riverbend", "Brightmeadow", "Stoneburrow", "Sweetriver", "Goldcliff", 
    "Merrybrook", "Underhill", "Goodbarrow", "Thornfield", "Sunnydale", "Rosecreek", 
    "Quickbrook", "Littlehill", "Roundmeadow", "Softriver", "Gentleburrow", 
    "Proudcliff", "Kindbrook", "Warmhollow", "Brightdale", "Clearriver", 
    "Softmeadow", "Highcliff", "Deepburrow", "Greenbrook", "Sunhill", 
    "Clearmeadow", "Swiftriver", "Gentlehill",
    "Ailbhe", "Branagh", "Caomhan", "Dáire", "Eibhear", "Fiachra", "Goibniu", 
    "Herne", "Iorwerth", "Kai", "Loghain", "Mordha", "Niamhan", "Oisean", 
    "Phelan", "Rhonwen", "Scáthach", "Taranis", "Uilliam", "Vercingetorix", 
    "Wynne", "Aldith", "Bevan", "Cyrus", "Drustan", "Eogain", "Finnegan", 
    "Gwydion", "Heremon", "Isolde", "Kedric", "Lorcan", "Merrion", "Nuada", "Ossian",
    "the Fierce Warrior", "the Gentle Hunter", "the Wise Elder", "the Swift Runner", 
    "the Strong Shield", "the Brave Heart", "the True Voice", "the Iron Fist", 
    "the Kind Soul", "the Bold Leader", "the Sharp Eye", "the Thunder Strike", 
    "the Stone Guard", "the Wind Walker", "the Fire Keeper", "the Earth Shaker", 
    "the Sky Watcher", "the River Strider", "the Mountain Climber", 
    "the Forest Tracker", "the Night Stalker", "the Dawn Bringer", "the Storm Caller", 
    "the Peace Maker", "the War Chief", "the Spirit Guide", "the Blood Brother", 
    "the Bone Breaker", "the Shadow Walker", "the Light Bearer"]
        }
        self.species = "Tiefling"

        super().__init__()
        self.skin = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", 
        "black", "white", "gray", "cyan", "magenta", "lime", "navy", "olive",
        "teal", "maroon", "crimson", "indigo", "violet", "rainbow"])
        self.height = f"{random.randint(5,6)}'{random.randint(0,11)}\""
        self.hair = self.pickHorns()

class Bestial(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Bulgrush", "Torakesh", "Dakresh", "Goramesh", "Balorash", "Koresh", "Toresh", 
        "Dramash", "Garesh", "Brakosh", "Poresh", "Doramesh", "Karosh", "Balesh", "Goresh", 
        "Damesh", "Porash", "Koramesh", "Torush", "Barosh", "Gorash", "Talesh", "Berash", 
        "Dorash", "Gamesh", "Terosh", "Borash", "Karesh", "Polesh", "Togresh"
        ],
            "Female": [
        "Balasha", "Torasha", "Dakasha", "Gorasha", "Belasha", "Korasha", "Terasha", 
        "Drasha", "Garasha", "Brasha", "Porasha", "Dorasha", "Karasha", "Telasha", 
        "Balisha", "Golasha", "Damasha", "Polasha", "Kolasha", "Tolasha", "Barasha", 
        "Galasha", "Talasha", "Berasha", "Dolasha", "Gamasha", "Telasha", "Bolasha", 
        "Kelasha", "Pomasha"
        ],
            "Last": [
        "the Fierce Warrior", "the Gentle Hunter", "the Wise Elder", "the Swift Runner", 
        "the Strong Shield", "the Brave Heart", "the True Voice", "the Iron Fist", 
        "the Kind Soul", "the Bold Leader", "the Sharp Eye", "the Thunder Strike", 
        "the Stone Guard", "the Wind Walker", "the Fire Keeper", "the Earth Shaker", 
        "the Sky Watcher", "the River Strider", "the Mountain Climber", "the Forest Tracker", 
        "the Night Stalker", "the Dawn Bringer", "the Storm Caller", "the Peace Maker", 
        "the War Chief", "the Spirit Guide", "the Blood Brother", "the Bone Breaker", 
        "the Shadow Walker", "the Light Bearer"
            ]}
        
        super().__init__()
        self.species = random.choice(["Orc", "Aarakocra", "Bugbear", "Genasi", "Firbolg", "Gith", 
        "Goblin", "Harengon", "Kenku", "Kobold", "Minotaur", "Tabaxi", "Plasmoid", "Owlin", "Leonin", "Loxodon", "Tortle", "Grung"])
        self.skin = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "brown", 
        "black", "white", "gray", "cyan", "navy", "olive", "teal", "maroon", "crimson", "indigo", "violet", "gray"])
        self.height = f"{random.randint(5,7)}'{random.randint(0,11)}\""
        self.hair = self.pickHair()

class Lizardfolk(Species):
    def __init__(self):
        self.nameLists = {
            "Male": [
        "Garem", "Koshin", "Salim", "Torin", "Galen", "Kesim", "Sarim", "Tarem", 
        "Garim", "Kolem", "Sakem", "Torem", "Golin", "Kasim", "Sorim", "Tanem", 
        "Ganem", "Keshem", "Salum", "Tokim", "Garem", "Kosem", "Sarin", "Tolin", 
        "Gorim", "Kerim", "Salem", "Tanum", "Gamin", "Kosam"
        ],
            "Female": [
        "Gara", "Kosha", "Sala", "Tora", "Gale", "Kesa", "Sare", "Tara", "Gana", 
        "Kola", "Sake", "Tora", "Gola", "Kasa", "Sora", "Tana", "Gana", "Kesha", 
        "Sala", "Toka", "Gora", "Kosa", "Sara", "Tola", "Gale", "Kera", "Sana", 
        "Tone", "Gama", "Kase"
        ],
            "Last": ["the Fierce Warrior", "the Gentle Hunter", "the Wise Elder", "the Swift Runner", 
        "the Strong Shield", "the Brave Heart", "the True Voice", "the Iron Fist", 
        "the Kind Soul", "the Bold Leader", "the Sharp Eye", "the Thunder Strike", 
        "the Stone Guard", "the Wind Walker", "the Fire Keeper", "the Earth Shaker", 
        "the Sky Watcher", "the River Strider", "the Mountain Climber", "the Forest Tracker", 
        "the Night Stalker", "the Dawn Bringer", "the Storm Caller", "the Peace Maker", 
        "the War Chief", "the Spirit Guide", "the Blood Brother", "the Bone Breaker", 
        "the Shadow Walker", "the Light Bearer"]}
        self.species = "Lizardfolk"

        super().__init__()
        self.skin = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "brown", 
        "black", "white", "gray", "cyan", "navy", "olive", "teal", "maroon", "crimson", "indigo", "violet", "gray"])
        self.height = f"{random.randint(4,6)}'{random.randint(0,11)}\""
        self.hair = self.pickHorns()