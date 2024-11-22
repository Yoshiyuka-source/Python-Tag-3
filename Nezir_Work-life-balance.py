import time 
import webbrowser
import random

def main():
    print("Deine arbeit beginnt")

    work_and_pause()
    
def play_song():
    lieblingssongs = [
        "https://youtu.be/3XqqkrJENB4?si=lXOfj4nmkLuRPDYZ"
    ]
    webbrowser.open(lieblingssongs)

      
def work_and_pause():
    arbeitszeit = 8 * 60  # Gesamte Arbeitszeit in Minuten (8 Stunden)
    pause_dauer = 10      # Pausenzeit in Minuten
    lernintervall = 90    # Arbeitszeit zwischen Pausen in Minuten
    pause_counter = 0     # Anzahl der Pausen
    arbeitszeit_counter = 0  # Zeit, die tatsächlich gearbeitet wurde  

    while arbeitszeit > 0:
        print (f"Du hast noch, {arbeitszeit} minuten übrig.")
        
        arbeitszeit = min(lernintervall, arbeitszeit)
        for i in range(arbeitszeit):
            time.sleep(1)
            arbeitszeit_counter += 1
            arbeitszeit -= 1

        if arbeitszeit <= 0: 
            break
        
        print("\Endlich Pause, hier dein lieblingssong")
        
        play_song()
        
        for i in range(pause_dauer):
            time.sleep(1)
            arbeitszeit -= 1
            if arbeitszeit <= 0:
                break
            
        pause_counter += 1
        print(f"Pause vorbei. Du hast {pause_counter} pausen gemacht.")
        
        while True:
            warm_up = input("Lust auf warm-up? (ja/nein): ").strip().lower()
            if warm_up in ("ja", "nein"):
                break
            print("Ungültige Eingabe. Antworte mit 'ja' oder 'nein'.")
            
        if warm_up == "ja":
            zahlenraten()
                
    print("\Jooo Arbeit ist vorbei")
    print(f"Du hast {pause_counter} pausen gemacht und {arbeitszeit} minuten gearbeitet.")
        
def zahlenraten():
    geheimezahl = random.randint(1, 100)
    versuche = 6
    while versuche > 0:
        print(f"Du hast noch {versuche} Versuche übrig.")
        raten = input("Rate eine zahl zwischen 1 und 100: ")
        if raten.isdigit():
            raten = int(raten)
            if raten < geheimezahl:
                print("Zu niedrig, du Landratte!")
            elif raten > geheimezahl:
                print("Zu hoch!")
            else:
                print("Super gemacht jetzt haste den schatz")
                break
        else:
            print("Ungültig.")
                 
        versuche -= 1
    if versuche ==0:
        print("Game over!")
main()