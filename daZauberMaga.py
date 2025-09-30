# das zauberhafte Mathe Game 1
# neuroplastisches Game
# Mathe Upgrade laden

# box packen
def wähle_deinen_Held():
    hero = input("Wähle weise: Krieger, Magier, Schurke or x: ") # hero wird der input auf das gedruckte -> wähle...
    return hero

# erste Quest bauen - addieren 1
## anfordern an die Quest
## stelle rechenaufgaben aus zu summanden (a & b)
## a + b = c
## c soll max 9 sein
def quest_1():
    a = 1
    b = 2
    c = a + b
    if c > 9:
        c = 9
    return c


# wenn inhalt der box addieren oder x ist

def auswahl_und_game():
    if hero == "addieren" or hero == "x":

        try: # versuche diesen Weg
            print("Willkommen im zauberhaften Mathe Game 1") # drucken Willkommen...
        except Exception as e: # außer es gibt einen Fehler
            print(f"Ein Fehler ist aufgetreten: {e}") # drucken den Fehler
        finally: # egal was passiert
            print("Danke fürs Spielen!") # drucken fürs Spielen
    else: # sonst
        print("Ende")
        wähle_deinen_Held() # rufe die Funktion wähle_deinen_Held auf

while True:
    hero = wähle_deinen_Held()
    auswahl_und_game()
'''

mana = int(input("Start Mana: "))

try:
    while True:

'''