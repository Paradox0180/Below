import os
import sys
import random
import time


# clear screen function
def clear_screen():
    os.system('clear')

def fake_loading():
    if anesthetized == True:
        print("")
        print("Research 0%", end="\r")
        time.sleep(0.5)
        print("Research 25%", end="\r")
        time.sleep(0.5)
        print("Research 50%", end="\r")
        time.sleep(0.5)
        print("Research 75%", end="\r")
        time.sleep(0.5)
        print("Research 100%", end="\r")
        time.sleep(1)
        print("Research complete, added to reports. Please send your reports by entering the report command")
        print("")

def dispose_entity():
    entity = "none"
    rarity = "none"
    dosage = "none"

# important variables
terminal = "run"
in_shop = False
points = 50
entity = "none"
rarity = "none"
anesthetized = False
dosage = "none"
chance = [1, 2]
equipment = "basic equipment"
common_reports = 0
uncommon_reports = 0
mythical_reports = 0
cursed_reports = 0
unknown_reports = 0

clear_screen()

# welcome massege
print("""Welcom to Volt Spark Terminal V 1.0
For a list of commands type "help".  """)
print("------------------------------------")
print("""You got an E-Mail, type "mail" to open""")
print("")

# terminal while loop
while terminal != "quit":
    command  = input(">>  ")
    if entity == "none":
        anesthetized = False

    if command == "mail":
        print("""
From: Micheal
Subject: New Job
Greetings, new worker
Welcome to your new job in this submarine. Let me tell you the basics, your job here is to research the newly found
entities in oceania, everything will be managed from this terminal right here. Start by capturing
entities from the ocean and anesthetize them correctly before doing reserach or they will attack
you, after researching on them and sending your reports to the Higher Ups you will
be rewarded with reserach points that you can buy more items with from the shop that increase
your income. every entity has there own rarity and anesthesia dose so check those by typing index
on the terminal.

Micheal
""")
    elif command == "exit":
        terminal = "quit"
    elif command == "help":
        print("""
Available Commands:
  help          - Show this help menu
  index         - View the entity index
  capture       - Capture an entity (e.g., 'capture Common')
  anesthetize   - Anesthetize the captured entity (e.g., 'anesthetize 10 7 5')
  research      - Conduct research (e.g., 'research basic')
  shop          - View and purchase items from the shop
  status        - Check your points, captured entity, and available research types
  report        - Send your research report to headquarters
  exit          - Exit the game
  clear         - Clears the screen of the terminal
  dispose       - Removes current entity
Please type all commands in lower case.
""")
    elif command == "index":
        print("""
A- Drenched Kracken:
An entity Descnding from the kracken species. it is much more smaller from the classic Kracken
Class: Common
Anesthesia Dosage: 10 7 2

B- Siren Shark:
First instance found in ground zero, oceania. it uses its built in high pitched  sirens to disorient prey which
require much more concentrated amount of anesthesia to disable its sirens due to there dangerous pitch.
Class: Common
Anesthesia dosage: 17 20 11

C- Spectral Serpent:
Found in the more deep parts of oceania, it spectates its prey intimdating it.
Class: UnCommon
Anesthesia Dosage: 5 8 13

D- Harp Wraith:
Description of this entity is classified.
Class: UnCommon
Anesthesia Dosage: 4 21 0

E- Crystal Stalker:
Concentrated at crystal reefs, oceania. it is higly valuable due to its crystal heart, capturing it gives you
a 50% chance to get bonus points.
Class: Mythical
Anesthesia Dosage: 3 7 2


F- Drowned Whale:
Whales who enter void zone, oceania get drowned by unknown forces even if they are sea creatures who live
in water. after drowing they experiance a zombification like procsses and turn to the Drowned whale.
Class: Mythical
Anesthesia Dosage: 15 20 5

G- Abyss Leviathan:
A Levuathen worm like creature that lurks in the abyss of void zone. capablities are unknown.
Class: Cursed
Anesthesia Dosage: 16 8 0

H- Shadow Phantom:
Description on this entity is highly Classified
Class: UnKnown
Anesthesia Dosage: 34 24 16

Payment upon researching:
Common: 50
UnCommon: 100
Mythical: 200
Cursed: 350
UnKnown: 750

Price upon capturing:
Common: 10
UnCommon: 25
Mythical: 50
Cursed: 100
UnKown: 250


You need specific research equipment for each entity class
""")
    elif command == "larry":
        points += 1000000
        print("\nYou got an additional 1 million points, how did you find this cheat code?\n")
    elif command == "clear":
        clear_screen()
    elif command == "status":
        print("\nPoints>> " + (str(points)))
        print("Entity>> " + entity)
        print("Class of entity>> " + rarity)
        print("Anesthetized>> " + (str(anesthetized)))
        print("Current equipment>> " + equipment)
        print("Common reports>> " + (str(common_reports)))
        print("Uncommon reports>> " + (str(uncommon_reports)))
        print("Mythical reports>> " + (str(mythical_reports)))
        print("Cursed reports>> " + (str(cursed_reports)))
        print("Unknown reports>> " + (str(unknown_reports)))
        print("")
    elif command == "capture common" and points >= 10:
        points -= 10
        rc1 = random.choice(chance)
        if rc1 == 1:
            anesthetized = False
            dosage = "10 7 2"
            entity = "drenched kracken"
            rarity = "common"
            print("\nCaptured Entity>> " + entity, "\n")
        elif rc1 == 2:
            anesthetized = False
            dosage = "17 20 11"
            entity = "siren shark"
            rarity = "common"
            print("Captured Entity>> " + entity)
    elif command == "capture uncommon" and points >= 25:
        points -= 25
        rc2 = random.choice(chance)
        if rc2 == 1:
            anesthetized = False
            dosage = "5 8 13"
            entity = "spectral serpent"
            rarity = "uncommon"
            print("\nCaptured Entity>> " + entity, "\n")
        elif rc2 == 2:
            anesthetized = False
            dosage = "4 21 0"
            entity = "harp wraith"
            rarity = "uncommon"
            print("\nCaptured Entity>> " + entity, "\n")
    elif command == "capture mythical" and points >= 50:
        points -= 50
        rc4 = random.choice(chance)
        if rc4 == 1:
            bp = random.choice(chance)
            if bp == 1:
                points += 50
                print("\nYou got 50 bonus points from crystal stalker's crystal heart :D")
            anesthetized = False
            dosage = "3 7 2"
            entity = "crystal stalker"
            rarity = "mythical"
            print("\nCaptured Entity>> " + entity, "\n")
        elif rc4 == 2:
            anesthetized = False
            dosage = "15 20 5"
            entity = "drowned whale"
            rarity = "mythical"
            print("\nCaptured Entity>> " + entity, "\n")
    elif command == "capture cursed" and points >= 100:
        anesthetized = False
        points -= 100
        dosage = "16 8 0"
        entity = "abyss leviathan"
        rarity = "cursed"
        print("\nCaptured Entity>> " + entity, "\n")
    elif command == "capture unknown" and points >= 250:
        anesthetized = False
        points -= 250
        dosage = "34 24 16"
        entity = "shadow leviathan"
        rarity = "unknown"
        print("\nCaptured Entity>> " + entity, "\n")
    elif command == "capture":
        print("""
You got to specify what class you want to capture. For Example:
capture common
capture mythical
capture unknown
to read about classes enter index
""")
    elif command.startswith("anesthetize"):
        entered_dosage = command[12:].strip()
        if entered_dosage == dosage:
            if anesthetized == True:
                print("\nEntity is already anesthetized\n")
            else:
                anesthetized = True
                print("\nSuccessfully anesthetized " + entity, "\n")
        else:
            if anesthetized == True:
                print("\nEntity is already anesthetized\n")
            else:
                terminal = "quit"
    elif command == "research":
        if anesthetized == False:
            terminal = "quit"
        if entity == "none":
            print("\nNo entity captured\n")
        elif rarity == "common":
            entity = "none"
            rarity = "none"
            dosage = "none"
            fake_loading()
            common_reports += 1
        elif rarity == "uncommon":
            if equipment != "basic equipment":
                entity = "none"
                rarity = "none"
                dosage = "none"
                fake_loading()
                uncommon_reports += 1
            else:
                print("\nupgrade equipment from the shop to research uncommon entities\n")
        elif rarity == "mythical":
            if equipment != "basic equipment" and equipment != "advanced equipment":
                entity = "none"
                rarity = "none"
                dosage = "none"
                fake_loading()
                mythical_reports += 1
            else:
                print("\nupgrade equipment from the shop to research mythical entities\n")
        elif rarity == "cursed":
            if equipment != "basic equipment" and equipment != "advanced equipment" and equipment != "specialized equipment":
                entity = "none"
                rarity = "none"
                dosage = "none"
                fake_loading()
                cursed_reports += 1
            else:
                print("\nupgrade equipment from the shop to research cursed entities\n")
        elif rarity == "unknown":
            if equipment != "basic equipment" and equipment != "advanced equipment" and equipment != "specialized equipment" and equipment != "prototype equipment":
                entity = "none"
                rarity = "none"
                dosage = "none"
                fake_loading()
                unknown_reports += 1
            else:
                print("\nupgrade equipment from the shop to research unknown entities\n")
    elif command == "report":
        print("\nSending reports...\n", end = "\r")
        points = points + (common_reports * 50)
        points = points + (uncommon_reports * 100)
        points = points + (mythical_reports * 200)
        points = points + (cursed_reports * 350)
        points = points + (unknown_reports * 750)
        time.sleep(1)
        print("\nSent all reports\n")
        common_reports = 0
        uncommon_reports = 0
        mythical_reports = 0
        cursed_reports = 0
        unknown_reports = 0
    elif command == "shop":
        print("""
Shop items:
1- advanced equipment       -Makes research on uncommon entities possiple.
Price: 200

2- specialized equipment    -Makes research on mythical entities possiple.
Price:1000

3- prototype equipment      -Makes research on cursed entities possiple.
Price: 2500

4 classified equipment      -Makes research on unknown entities possiple.
Price: 5000

Enter "buy [item]" to buy anything from the shop.
Enter "quit" to exit the shop.
""")
        in_shop = True
        while in_shop == True:
            shop_input = input("Shop Menu>>  ")
            if shop_input == "quit":
                in_shop = False
            elif shop_input == "buy advanced equipment":
                if points >= 200:
                    points -= 200
                    equipment = "advanced equipment"
                    print("\nSuccesfully bought " + equipment, "\n")
                else:
                    print("\nNot enough research points\n")
                    print("\nCurrent points>> " + (str(points)), "\n")
            elif shop_input == "buy specialized equipment":
                if points >= 1000:
                    points -= 1000
                    equipment = "specialized equipment"
                    print("\nSuccesfully bought " + equipment, "\n")
                else:
                    print("Not enough research points")
                    print("\nCurrent points>> " + (str(points)), "\n")
            elif shop_input == "buy prototype equipment":
                if points >= 2500:
                    points -= 2500
                    equipment = "prototype equipment"
                    print("\nSuccesfully bought " + equipment, "\n")
                else:
                    print("\nNot enough research points\n")
                    print("\nCurrent points>> " + (str(points)), "\n")
            elif shop_input == "buy classified equipment":
                if points >= 5000:
                    points -= 5000
                    equipment = "classified equipment"
                    print("\nSuccesfully bought " + equipment, "\n")
                else:
                    print("\nNot enough research points\n")
                    print("\nCurrent points>> " + (str(points)), "\n")
    elif command == "dispose":
        print("\nDisposing entity...\n", end = "\r")
        dispose_entity()
        time.sleep(2)
        print("\nDisposed entity\n")
    else:
        print("""
Invalid command or not enough points XD
""")

dead_menu = True

print("")
print("You ded?")
print("Reason of death>> idk why u ded lol")
print("Score AKA Points>> " + (str(points)))
print("")

while dead_menu == True:
    dead_input = input("\nRetry? (y/n)  \n")
    if dead_input == "y":
        clear_screen()
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        dead_menu = False
