import random
import sys
from classes import Elf, Human, Dwarf, Halfling, Bestial, Tiefling, Lizardfolk

'''
These traits are borrowed from these two links:
https://www.dndspeak.com/2022/01/23/100-npc-personality-traits/
https://www.worldoflegon.com/personality-traits/
'''


good = [
    "Accessible", "Active", "Adaptable", "Admirable", "Adventurous", "Agreeable", "Alert", "Allocentric",
    "Amiable", "Anticipative", "Appreciative", "Articulate", "Aspiring", "Athletic", "Attractive", "Balanced",
    "Benevolent", "Brilliant", "Calm", "Capable", "Captivating", "Caring", "Challenging", "Charismatic",
    "Charming", "Cheerful", "Clean", "Clear-headed", "Clever", "Colorful", "Companionly", "Compassionate",
    "Conciliatory", "Confident", "Conscientious", "Considerate", "Constant", "Contemplative", "Cooperative",
    "Courageous", "Courteous", "Creative", "Cultured", "Curious", "Daring", "Debonair", "Decent", "Decisive",
    "Dedicated", "Deep", "Dignified", "Directed", "Disciplined", "Discreet", "Dramatic", "Dutiful", "Dynamic",
    "Earnest", "Ebullient", "Educated", "Efficient", "Elegant", "Eloquent", "Empathetic", "Energetic",
    "Enthusiastic", "Esthetic", "Exciting", "Extraordinary", "Fair", "Faithful", "Farsighted", "Felicific",
    "Firm", "Flexible", "Focused", "Forceful", "Forgiving", "Forthright", "Freethinking", "Friendly", "Fun-loving",
    "Gallant", "Generous", "Gentle", "Genuine", "Good-natured", "Gracious", "Hardworking", "Healthy", "Hearty",
    "Helpful", "Heroic", "High-minded", "Honest", "Honorable", "Humble", "Humorous", "Idealistic", "Imaginative",
    "Impressive", "Incisive", "Incorruptible", "Independent", "Individualistic", "Innovative", "Inoffensive",
    "Insightful", "Intelligent", "Intuitive", "Invulnerable", "Kind", "Knowledgeable", "Leaderly", "Leisurely",
    "Liberal", "Logical", "Lovable", "Loyal", "Lyrical", "Magnanimous", "Many-sided", "Masculine", "Mature",
    "Methodical", "Meticulous", "Moderate", "Modest", "Multi-leveled", "Neat", "Nonauthoritarian", "Objective",
    "Observant", "Open", "Optimistic", "Orderly", "Organized", "Original", "Painstaking", "Passionate", "Patient",
    "Patriotic", "Peaceful", "Perceptive", "Perfectionist", "Personable", "Persuasive", "Planful", "Playful",
    "Polished", "Popular", "Practical", "Precise", "Principled", "Profound", "Protean", "Protective",
    "Providential", "Prudent", "Punctual", "Purposeful", "Rational", "Realistic", "Reflective", "Relaxed",
    "Reliable", "Resourceful", "Respectful", "Responsible", "Responsive", "Reverential", "Romantic", "Rustic",
    "Sage", "Sane", "Scholarly", "Scrupulous", "Secure", "Selfless", "Self-critical", "Self-defacing",
    "Self-denying", "Self-reliant", "Self-sufficient", "Sensitive", "Sentimental", "Seraphic", "Serious",
    "Sharing", "Shrewd", "Simple", "Skillful", "Sober", "Sociable", "Solid", "Sophisticated", "Spontaneous",
    "Sporting", "Stable", "Steadfast", "Steady", "Stoic", "Strong", "Studious", "Suave", "Subtle", "Sweet",
    "Sympathetic", "Systematic", "Tasteful", "Teacherly", "Thorough", "Tidy", "Tolerant", "Tractable",
    "Trusting", "Understanding", "Undogmatic", "Unfoolable", "Upright", "Urbane", "Venturesome", "Vivacious",
    "Warm", "Well-bred", "Well-read", "Well-rounded", "Winning", "Wise", "Witty", "Youthful"
]

neutral = [
    "Absentminded", "Aggressive", "Ambitious", "Amusing", "Artful", "Ascetic", "Authoritarian", "Big-thinking",
    "Boyish", "Breezy", "Businesslike", "Busy", "Casual", "Cerebral", "Chummy", "Circumspect", "Competitive",
    "Complex", "Confidential", "Conservative", "Contradictory", "Crisp", "Cute", "Deceptive", "Determined",
    "Dominating", "Dreamy", "Driving", "Droll", "Dry", "Earthy", "Effeminate", "Emotional", "Enigmatic",
    "Experimental", "Familial", "Folksy", "Formal", "Freewheeling", "Frugal", "Glamorous", "Guileless",
    "High-spirited", "Hurried", "Hypnotic", "Iconoclastic", "Idiosyncratic", "Impassive", "Impersonal",
    "Impressionable", "Intense", "Invisible", "Irreligious", "Irreverent", "Maternal", "Mellow", "Modern",
    "Moralistic", "Mystical", "Neutral", "Noncommittal", "Noncompetitive", "Obedient", "Old-fashioned",
    "Ordinary", "Outspoken", "Paternalistic", "Physical", "Placid", "Political", "Predictable", "Preoccupied",
    "Private", "Progressive", "Proud", "Pure", "Questioning", "Quiet", "Religious", "Reserved", "Restrained",
    "Retiring", "Sarcastic", "Self-conscious", "Sensual", "Skeptical", "Smooth", "Soft", "Solemn", "Solitary",
    "Stern", "Stolid", "Strict", "Stylish", "Subjective", "Surprising", "Tough", "Unaggressive", "Unambitious",
    "Unceremonious", "Unchanging", "Undemanding", "Unfathomable", "Unhurried", "Uninhibited", "Unpredicatable",
    "Unsentimental", "Whimsical"
]

bad = [
    "Abrasive", "Abrupt", "Agonizing", "Aimless", "Airy", "Aloof", "Amoral", "Angry", "Anxious", "Apathetic",
    "Arbitrary", "Argumentative", "Arrogant", "Artificial", "Assertive", "Astigmatic", "Barbaric", "Bewildered",
    "Bizarre", "Bland", "Blunt", "Boisterous", "Brittle", "Brutal", "Calculating", "Callous", "Cantankerous",
    "Careless", "Cautious", "Charmless", "Childish", "Clumsy", "Coarse", "Cold", "Colorless", "Complacent",
    "Complaintive", "Compulsive", "Conceited", "Condemnatory", "Conformist", "Confused", "Contemptible",
    "Conventional", "Cowardly", "Crafty", "Crass", "Crazy", "Critical", "Crude", "Cruel", "Cynical", "Decadent",
    "Deceitful", "Delicate", "Demanding", "Dependent", "Desperate", "Destructive", "Devious", "Difficult",
    "Dirty", "Disconcerting", "Discontented", "Discouraging", "Discourteous", "Dishonest", "Disloyal",
    "Disobedient", "Disorderly", "Disorganized", "Disputatious", "Disrespectful", "Disruptive", "Dissolute",
    "Dissonant", "Distractible", "Disturbing", "Dogmatic", "Domineering", "Dull", "Easily Discouraged",
    "Egocentric", "Enervated", "Envious", "Erratic", "Escapist", "Excitable", "Expedient", "Extravagant",
    "Extreme", "Faithless", "Fanatical", "Fanciful", "Fatalistic", "Fawning", "Fearful", "Fickle", "Fiery",
    "Fixed", "Flamboyant", "Foolish", "Forgetful", "Fraudulent", "Frightening", "Frivolous", "Gloomy",
    "Graceless", "Grand", "Greedy", "Grim", "Gullible", "Hateful", "Haughty", "Hedonistic", "Hesitant",
    "Hidebound", "High-handed", "Hostile", "Ignorant", "Imitative", "Impatient", "Impractical", "Imprudent",
    "Impulsive", "Inconsiderate", "Incurious", "Indecisive", "Indulgent", "Inert", "Inhibited", "Insecure",
    "Insensitive", "Insincere", "Insulting", "Intolerant", "Irascible", "Irrational", "Irresponsible",
    "Irritable", "Lazy", "Libidinous", "Loquacious", "Malicious", "Mannered", "Mannerless", "Mawkish",
    "Mealymouthed", "Mechanical", "Meddlesome", "Melancholic", "Meretricious", "Messy", "Miserable", "Miserly",
    "Misguided", "Mistaken", "Money-minded", "Monstrous", "Moody", "Morbid", "Muddle-headed", "Naive",
    "Narcissistic", "Narrow", "Narrow-minded", "Natty", "Negativistic", "Neglectful", "Neurotic", "Nihilistic",
    "Obnoxious", "Obsessive", "Obvious", "Odd", "Offhand", "One-dimensional", "One-sided", "Opinionated",
    "Opportunistic", "Oppressed", "Outrageous", "Overimaginative", "Paranoid", "Passive", "Pedantic", "Perverse",
    "Petty", "Pharisaical", "Phlegmatic", "Plodding", "Pompous", "Possessive", "Power-hungry", "Predatory",
    "Prejudiced", "Presumptuous", "Pretentious", "Prim", "Procrastinating", "Profligate", "Provocative",
    "Pugnacious", "Puritanical", "Quirky", "Reactionary", "Reactive", "Regimental", "Regretful", "Repentant",
    "Repressed", "Resentful", "Ridiculous", "Rigid", "Ritualistic", "Rowdy", "Ruined", "Sadistic",
    "Sanctimonious", "Scheming", "Scornful", "Secretive", "Sedentary", "Selfish", "Self-indulgent", "Shallow",
    "Shortsighted", "Shy", "Silly", "Single-minded", "Sloppy", "Slow", "Sly", "Small-thinking", "Softheaded",
    "Sordid", "Steely", "Stiff", "Strong-willed", "Stupid", "Submissive", "Superficial", "Superstitious",
    "Suspicious", "Tactless", "Tasteless", "Tense", "Thievish", "Thoughtless", "Timid", "Transparent",
    "Treacherous", "Trendy", "Troublesome", "Unappreciative", "Uncaring", "Uncharitable", "Unconvincing",
    "Uncooperative", "Uncreative", "Uncritical", "Unctuous", "Undisciplined", "Unfriendly", "Ungrateful",
    "Unhealthy", "Unimaginative", "Unimpressive", "Unlovable", "Unpolished", "Unprincipled", "Unrealistic",
    "Unreflective", "Unreliable", "Unrestrained", "Unself-critical", "Unstable", "Vacuous", "Vague", "Venal",
    "Venomous", "Vindictive", "Vulnerable", "Weak", "Weak-willed", "Well-meaning", "Willful", "Wishful", "Zany"
]

quirks = [
    "This person's pockets are filled with a seemingly infinite supply of sunflower seeds. They discreetly spit the hulls into their hand and toss them when they think no one's watching.",
    "This person also dreams of being an adventurer, but their parents, spouse, drinking buddies, etc. keep talking them out of it. They are constantly sneaking peeks at your armor and weaponry, trying to hide their jealousy.",
    "This person is very religious. One of the daily prayers is coming up, and they really want this conversation to end so they can make their way to the temple.",
    "This person occasionally sneaks sips from a leather-wrapped hip flask. If they like the player, they'll offer them a nip. It's the vilest bathtub moonshine imaginable.",
    "This person smacks their lips way, way, way too often.",
    "This person starts laughing out of nowhere. When questioned, they say that they just remembered a joke about a freshly plucked harpy that isn't suitable for polite company.",
    "This person is a sailor on shore leave. They're trying to pack in as much drinking, gambling, and general chicanery as possible before their crew sets sail.",
    "This person loves to garden. Their fingernails are always caked in dirt, and they occasionally have bits of twigs stuck in their hair.",
    "This person has a beloved dog that follows them everywhere. The dog likes snuffling for treats in strangers' pockets.",
    "The person writes pulpy stories on the side. They're always jotting down notes on a little slate tablet, and will do nearly anything to witness something grim, gritty, or grisly.",
    "This person just moved into town from a distant land, and everyone thinks they don't know the local language. In reality, they just don't like chatting.",
    "This person was born in a distant town. Their wagon broke down while passing through town, and they decided to just live there instead of fixing it. The wagon is still there, with a single broken axle.",
    "This person has lived alone for years, meditating on the purpose of the multiverse. They came back once they found it.",
    "This person is absolutely obsessed with foraging. They can identify every local plant, know exactly where to find it, and can cook it to perfection.",
    "This person has a strange accent and refuses to tell the party where they picked it up.",
    "This person has read every book in town, but never traveled beyond its borders. They think they're ready for anything.",
    "This person is known across the region for their honesty. Gamblers regularly come into town just so the person can deal with their high-stakes games.",
    "This person has a shed on the edge of their property, where they tinker late into the night.",
    "This person has an uncanny ability to predict the weather. They often guide the conversation towards temperatures and cloud movements.",
    "This person's jerky recipe is the pride of the town. They're always willing to buy or trade for fresh meat from the party's adventures.",
    "This person looks severe and talks in a sneering voice, but is actually kind-hearted and generous.",
    "This person has nine children, with another on the way. They'd do nearly anything for a night of peace and quiet.",
    "This person has good taste. They quickly pick out the little flourishes in the party's equipment and sincerely compliment subtle details.",
    "This person has OCD and is constantly trying to organize things.",
    "This person has no sense of direction and will always go the wrong way.",
    "This person is fixated on having the newest cutting edge gadgets, many of which don't work as advertised.",
    "This person never seems to be paying attention but can recite back anything said to him/her/them word-for-word.",
    "This person has a lifelong bird watching list and will drop everything to see a bird not on the list.",
    "This person Whenever someone changes the topic from what they were talking about, they say, 'Uh huh. Anyway...' before returning to what they were saying.",
    "This person peppers their speech with words from other languages.",
    "This person habitually whistles a tune, a sort of personal theme song.",
    "This person has been learning a new instrument / writing on their next song, and insists on having the PCs listen to what they've been working on.",
    "This person prefers if they're the only one holding any sharp tool / weapon in the room, and will insist on handling anything that requires a knife themselves.",
    "This person has a bit of satyr blood in them, so when speaking they have a goat-like stu-u-u-tter.",
    "This person is overly secretive of their books / folders, even if they're of no high importance, like their diary.",
    "This person never swears.",
    "This person swears every other sentence.",
    "This person assumes the worst out of any situation presented to them, even something as nice as a picnic could have disastrous effects in their eyes.",
    "This person goes starkly silent around anyone they find remotely attractive.",
    "This person talks relentlessly to fill the awkward silence, even if they would like to shut up, around anyone they find remotely attractive.",
    "This person constantly reminisces about the golden ages or the 'good old days', even if the period they're alluding to wasn't that great.",
    "This person is scared of gore and faints at the sight of blood.",
    "This person needs to wear a certain piece of jewelry or clothing in order to feel comfortable or safe.",
    "This person comments on things they observe in others out loud. Even observations most would keep to themselves.",
    "This person loves gossiping and any piece of juicy info, or just has a constant curiosity in the goings on of others.",
    "This person has a tendency to spill secrets, theirs and others', though they don't mean to.",
    "This person melts and coos at the sight of any remotely 'cute' animal, from cats to dogs to fluffy and lethal owlbears.",
    "This person has selective mutism. As a result, they have a few different ways of communicating non-verbally whenever they need to.",
    "This person loves to hear themself talk, and always finds a way to insert their personal stories into a conversation.",
    "This person loves listening to people talking about their interest, and even if they're not particularly interested in the object of discussion, will ask follow-up questions.",
    "This person has an unhealthy obsession for tea, drinking an unacceptable amount every day.",
    "This person is literate, and considers grammar vital for one's success. They will correct and be annoyed by PCs if they're not speaking properly.",
    "This person often loses their train of thought and tends to quickly jump from one topic to the next.",
    "This person tells inappropriate jokes at the WORST times.",
    "This person has an interesting story for every occasion. Sometimes, these stories tend to drag on for way too long.",
    "This person cannot stand the ocean, or any body of water. They are DEATHLY afraid of the open sea.",
    "This person is very religious and typically likes to adorn their clothing with symbols of their God/Goddess.",
    "This person wants everyone to think they are an intellectual. They sometimes use big words to sound smart, but they don't always know what they mean.",
    "This person is very jumpy, and can easily be frightened by loud noises or someone walking up behind them.",
    "This person sounds sweet but is very passive-aggressive and judgmental, bless their heart.",
    "This person keeps food in their pockets to feed wildlife.",
    "This person has a hobby that they are very happy to tell you about if you show even the slightest hint of interest.",
    "This person is on a diet and is very envious of anyone around them eating delicious food or drink.",
    "This person is never idle; they can't just sit and do nothing. They're usually busy doing something: reading a book, whittling, gathering flowers, etc.",
    "This person is paranoid, by pretty much anything and anyone. There is always a conspiracy brewing somewhere that involves them.",
    "This person is patient —too patient for their own good.",
    "This person is a neat freak, they love to clean. When someone meets them, they're usually seen with a broom or a cloth, cleaning something or another.",
    "This person loves to ponder the big questions: who are we and why are we here?",
    "This person loves to cook and will always offer food to her guests, even if they decline her offer.",
    "This person is fascinated by phrenology, and desperately wants to measure the heads of every creature she meets.",
    "The person is gruff and taciturn except when talking to kids because they remind him of his own kids.",
    "The person can't handle their alcohol. The person also loves to indulge.",
    "The person can't stand being wrong and will try to destroy every reasoning that could show them this. If proven wrong, the person will sulk for days on end.",
    "The person is always doing something with their hands out of nervousness: braiding hair, thrumming fingers on the table, picking at the hem of their shirt.",
    "The person is an unabashed flirt but will freeze up if approached first.",
    "The person does not believe in magic and will not believe in magic even if someone invokes Tiamat in front of them.",
    "This person seems tired and talks and walks slowly and kind of in a slumber.",
    "This person tries to give the PC advice in the form of sayings from his home country. Sometimes they fit, sometimes they don't.",
    "This person tends to daydream. Sometimes he seems far off and is not listening. Even when he seems to listen closely, he asks to repeat the last part.",
    "This person dislikes violence, but understands that some problems can't be solved any other way. He may ask for the PCs to come up with a non-violent solution.",
    "This person distrusts everyone and everything and is pleasantly surprised when something happens just as promised or discussed.",
    "The person is on a quest to find rare and elusive potion making ingredients. They regularly turn up with new injuries.",
    "This person doesn't believe in elves.",
    "They, the person, have been mandated by a nature goddess to find and categorize every type of mushroom. They categorize them very badly, and should not be trusted to make meals.",
    "The person is a ten thousand year old dragon in disguise, just havin' a right giggle at causing all sorts of trouble.",
    "The person is always trying to trip on magic mushrooms and they try to hide the fact.",
    "This person has an intense distrust for the city guard.",
    "This person is fidgety and frequently looks at the sky or ceiling to check for monsters.",
    "This person sees any new piece of information as a potential deception.",
    "This person is quick to get into fights in order to test their own strength.",
    "This person is not content unless they are the most extravagantly dressed person in the room.",
    "This person is incredibly helpful, whether you want them to be or not.",
    "This person often speaks in riddles or rhymes and making sense of it all can be quite challenging.",
    "This person follows rules to the letter even when it inconveniences them and everyone around them.",
    "This person speaks to everyone in a calm but condescending voice almost as if they were speaking to a child.",
    "This person treats their tools/vehicle with more love and affection than their own family.",
    "This person gives everyone a nickname and refuses to learn their real names.",
    "This person is always carrying food on a stick, and if asked, will highly recommend the dubious stall they got it from.",
    "This person insists on carrying things too heavy for them, or taking care of delicate objects they invariably break, or watching over valuables they will definitely lose.",
    "This person sleeps all day and stays up all night."
]

speciesList = [[Elf, Human, Dwarf, Halfling, Tiefling],[Bestial, Lizardfolk, Tiefling],[Elf, Human, Dwarf, Halfling, Tiefling, Bestial, Lizardfolk, Tiefling]]

def main(quantity, category, filename):
    with open(filename, "w") as file:
        alignments = {"Good": good, "Neutral": neutral, "Bad": bad}
        for num in range(quantity):
            npc = NPC(num+1, category)
            npc.personality.append(random.choice(alignments["Good"]))
            npc.personality.append(random.choice(alignments["Neutral"]))
            npc.personality.append(random.choice(alignments["Bad"]))
            while len(npc.personality) < 4:
                rando = random.choice(alignments[random.choice(list(alignments.keys()))])
                if not rando in npc.personality:
                    npc.personality.append(rando)
            npc.quirk = random.choice(quirks)
            print(npc)
            print("-"*80)
            file.write(str(npc))
            file.write("-"*80 + "\n")



class NPC:
    def __init__(self, number, speciesCategory):
        self.id = number
        self.species = random.choice(speciesList[speciesCategory])()
        self.personality = []
        self.quirk = ""
        self.description = []

    def __str__(self):
        return(f'''NPC: {self.id}
Name: {self.species.fullName}
They are a {self.species.gender.lower()} {self.species.species.lower()} who is a {self.personality[0].lower()}, {self.personality[1].lower()}, {self.personality[2].lower()}, and {self.personality[3].lower()} person with 
{self.species.hair} and a {self.species.skin} complexion.
{self.quirk}
''')
    




if __name__ == '__main__':
    num = 0
    category = 3
    file = ""
    while num == 0 or category > 2 or ".txt" not in file:
        num = int(input("How many NPCs would you like to make?\n"))
        category = int(input("Which category would you like to use?\n1 = Court\n2 = Alliance\n3 = All\n")) - 1
        file = input("Please type a file name, followed by .txt, to save this information to.\nTHIS WILL OVERWRITE THE FILE IF IT ALREADY EXISTS!\n")
        if not isinstance(num,int) or num <= 0:
            print("Why'd you start this program if you didn't want to make someone?")
        elif not isinstance(category, int) or 2 < category < 0:
            print("When asked about which category, please type 1, 2, or 3")
        elif not isinstance(file, str) or ".txt" not in file:
            print("please put in a valid file name followed by .txt")

    main(num, category, file)