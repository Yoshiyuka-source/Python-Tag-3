import time

fragen = [
    "Wie gehts dir",
    "Wie war dein tag so",
    "Wie alt bist du",
    "Was machst du",
    "Wie groß bist du",
    "Was deine lieblingsfarbe",
    "Was ist deine lieblings tier",
    "Was magst du eher PC/Laptop",
    "Magst du Sommer oder Winter",
    "Bist du ein frühaufsteher oder spätaufsteher"

]

i = 0
while i < 10:
    print("Frage:", fragen[i])
    print("Du hast noch 30 sekunden.")

    sekunden = 30
    while sekunden > 0:
        print("Noch", sekunden, "Sekunden", end="\r")
        time.sleep(1)
        sekunden -= 1

    antwort = input("\nJetzt antworte: ")
    i += 1
