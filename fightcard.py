import sys
from PIL import Image, ImageOps, ImageDraw, ImageFont

class FightCard():
    def __init__(self, facts, image, username, race, mmr, title):
        self.facts = facts
        self.image = image
        self.username = username
        self.race = race
        self.mmr = mmr
        self.title = title

class CreateCard():
    def __init__(self):
        self.fightcard = None

    def get_inputs(self):
        username = input("Please enter the username: ")
        race = input("Please enter the race: ")
        mmr = input("Please enter the mmr: ")
        num_facts = self.get_num_facts()
        facts = []
        for x in range(num_facts):
            fact = input(f"Please enter fact {x}: ")
            facts.append(fact)
        title = input("Please enter a title for the player. Keep empty if you do not want titles: ")
        if title != "":
            title += " "
        image = input("Please enter the image path. Note that this should ideally be 40x40 otherwise it will be squished: ")
        self.fightcard = FightCard(facts, image, username, race, mmr, title)

    def create_card(self):
        img = Image.new(mode="RGB", size=(350, 200), color=(255,255,255))
        logo = Image.open(self.fightcard.image)
        size = (100, 100)
        logo = logo.resize(size)
        img.paste(logo, box=None)
        draw = ImageDraw.Draw(img)
        draw.text((120, 20),self.fightcard.title + self.fightcard.username,(0,0,0))
        draw.text((120, 40),self.fightcard.race + " : " + self.fightcard.mmr,(0,0,0))
        for i in range(len(self.fightcard.facts)):
            draw.text((10, 110 + (i * 15)),self.fightcard.facts[i],(0,0,0))
        img = ImageOps.expand(img, border=5, fill='black')
        img.show()

    def get_num_facts(self):
        num_facts = input("Please enter the number of facts: ")
        while not num_facts.isnumeric() or int(num_facts) < 0 or int(num_facts) > 6:
            num_facts = input("Invalid input, please enter a number between 1 and 6: ")
        return int(num_facts)

if __name__ == '__main__':
    # either ask questions or load from file
    args = sys.argv
    if len(args) != 2:
        print("Invalid args passed in. Please use \"python fightcard.py help\" to see valid options")
        exit()
    if args[1] == "help":
        print("\"python fightcard.py type\" - to manually enter all required information")
        print("\"python fightcard.py read\" - to read all information from a csv file")
    elif args[1] == "type":
        createCard = CreateCard()
        createCard.get_inputs()
        createCard.create_card()
    elif args[1] == "read":
        print("blah")
    else:
        print("Invalid args passed in. Please use \"python fightcard.py help\" to see valid options")
    # ask for player race
    # ask for 

