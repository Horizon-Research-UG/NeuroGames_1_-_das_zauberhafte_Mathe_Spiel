# das zauberhafte Mathe Game 1
# neuroplastisches Game
# Mathe Upgrade laden

import time
#############################################



#############################################
# helden auswahl
# box packen
def wähle_deinen_Held():
    print("\n"*3)
    print("_____<Heldenauswahl>_____________________  ___________________________")
    hero = input("Wähle weise: Krieger, Magier, Schurke or x: ") # hero wird der input auf das gedruckte -> wähle...
    return hero
# box packen




### Held weiterleiten ###

# wenn inhalt der box addieren oder x ist
def held_weiterleiten(hero): # definiere Funktion wenn_held_ausgewählt mit Parameter hero
    if hero == "addieren" or hero == "x":
        print("Los gehts") # drucke Los gehts

        time.sleep(0.5) # warte 0.5 Sekunden

        print("Held weiterleiten") # drucke Held weiterleiten
        animation_1(1) # ani 1
        while True:
            zufallszahlen_bis_9() # rufe Funktion quest_1 auf
        
#sonst
    else: # sonst
        print("Ende 2") # drucke Ende 2
### Ende Held weiterleiten ###





#############################################
# Quests
#############################################

# Quest 1 - addieren 1
def addieren_1():
    print(str(a) + " + " + str(b) + " = z")
    input("x = ")
    if x == z:
        print("Richtig")
    else:
        print("Falsch")



#zufallszahlen bis 9
## anfordern an die Quest
## stelle rechenaufgaben aus zu summanden (a & b)
## a + b = c
## c soll max 9 sein
import random
def zufallszahlen_bis_9():
    a = random.randint(1, 3)
    b = random.randint(1, 3)
    c = a + b
    if c < 9:
        x = input(str(a) + " + " + str(b) + " = ")
        c = str(c)  # Ensure c is a string for comparison

        if str(x) == c:
            print("Richtig")
        else:
            print("Falsch")
    else:
        print("Zu groß: " + str(c))
# ende erste Quest bauen - addieren 1




#############################################
# animationen
#############################################

def import_time_terminal_gui(): # Anfangs animation
    print("Lade...")
    print('"import "')
    time.sleep(0.3)
    print('"import time "')
    time.sleep(0.3)
    print('"import time geladen"')
    time.sleep(0.3)
# ende Anfangs animation

# ani 1 - start animation
def animation_1(n):
    for i in range(n):
        print(".")
        time.sleep(0.2) # warte 0.2 Sekunden
        print("..")
        time.sleep(0.2) # warte 0.2 Sekunden
        print("...")
        time.sleep(0.2) # warte 0.2 Sekunden
# ani 1 - ende animation
#############################################


#############################################################
### Hauptprogramm ###
#############################################################


# ani 1
import_time_terminal_gui() # rufe Funktion import_time_terminal_gui auf


while True: # solange wahr
    x = wähle_deinen_Held() # rufe Funktion wähle_deinen_Held auf
    animation_1(2) # ani 2
    held_weiterleiten(x) # rufe Funktion wenn_held_ausgewählt mit Parameter hero auf



print("___________________________  ___________________________")
print("Ende ende 1")
print(" Gesundheits fluch bauen")





'''

mana = int(input("Start Mana: "))

try:
    while True:

'''