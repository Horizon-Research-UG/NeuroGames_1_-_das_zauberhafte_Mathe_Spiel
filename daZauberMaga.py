# das zauberhafte Mathe Game 1
# neuroplastisches Game
# Mathe Upgrade laden

import time

# Globale Variablen für Punktestand, Runden und Timer
mana = 0
leben = 0
punkte = 0
runde = 0
start_zeit = None  # Speichert wann der Timer gestartet wurde

#############################################
# Timer Funktionen
#############################################

def timer_starten():
    """Startet den Timer beim ersten Mal"""
    global start_zeit
    if start_zeit is None:  # Nur beim ersten Mal starten
        start_zeit = time.time()
        print("⏱️  Timer gestartet!")
        time.sleep(3)

def vergangene_zeit_anzeigen():
    """Zeigt die vergangene Zeit seit Timer-Start an"""
    global start_zeit
    if start_zeit is not None:
        vergangen = time.time() - start_zeit
        minuten = int(vergangen // 60)
        sekunden = int(vergangen % 60)
        return f"⏱️  Zeit: {minuten:02d}:{sekunden:02d}"
    return "⏱️  Timer nicht gestartet"



#############################################



#############################################
# helden auswahl
# box packen
def wähle_deinen_Held():
    print("\n"*3)
    print("_____<Heldenauswahl>_____________________  ___________________________")
    hero = input("Wähle weise: Krieger, Magier, Schurke or x: ") # hero wird der input auf das gedruckte -> wähle...
    leben_setzen()
    return hero
# box packen

def leben_setzen():
    global leben
    leben = int(input("Setze deine Leben (z.B. 3): "))
    print("Leben gesetzt auf: " + str(leben))
    time.sleep(1)

def leben_anzeigen():
    print("Leben: " + str(leben))


### Held weiterleiten ###

# wenn inhalt der box addieren oder x ist
def held_weiterleiten(hero): # definiere Funktion wenn_held_ausgewählt mit Parameter hero
    if hero == "addieren" or hero == "x":
        print("Los gehts") # drucke Los gehts
        time.sleep(0.5) # warte 0.5 Sekunden
        print("Held weiterleiten") # drucke Held weiterleiten
        animation_1(1) # ani 1
        while True:
            zufallszahlen_bis() # rufe Funktion quest_1 auf
        
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

def zufallszahlen_bis():
    global leben, mana, punkte, runde, start_zeit  # Globale Variablen
    a = random.randint(0, mana)
    b = random.randint(0, mana)
    c = a + b
    if c <= mana:
        # Timer starten beim ersten Mal
        timer_starten()
        
        x = input(str(a) + " + " + str(b) + " = ")
        c = str(c)  # Ensure c is a string for comparison

        if str(x) == c:
            print("Richtig! ✓")
            punkte += 1
            print("Punkte: " + str(punkte))
            mana += 1
            print("Mana: " + str(mana)) # zeige aktuelles mana an
        else:
            print("Falsch! ✗ Die richtige Antwort war: " + str(c))
            leben -= 1
            leben_anzeigen()
            if leben <= 0:
                print("Game Over! Du hast keine Leben mehr.")
                print("Deine Gesamtpunkte: " + str(punkte) + " in Zeit: " + vergangene_zeit_anzeigen())
                print("___________________________  ___________________________")
                print("Ende ende 3")
                print("_______________________________")
                exit()  # Beende das Spiel  
        runde += 1
        print("Runde: " + str(runde))

    

        # Timer-Anzeige
        print(vergangene_zeit_anzeigen())
        print("-" * 40)  # Trennlinie
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
    mana = int(input("Start Mana: ")) # input für mana
    animation_1(2) # ani 2
    held_weiterleiten(x) # rufe Funktion wenn_held_ausgewählt mit Parameter hero auf



print("___________________________  ___________________________")
print("Ende ende 1")
print("Mana als Obergrenze des Ergebnisses wählen")
print(" Gesundheits Fluch bauen")





'''

mana = int(input("Start Mana: "))

try:
    while True:

'''