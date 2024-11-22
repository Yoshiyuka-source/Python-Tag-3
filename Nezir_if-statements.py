def ageCheck(monthBirthday, monthCurrent, law, horrormovie):
    # Überprüfe, ob die Person in einem Land ist, in dem ab 18 die Volljährigkeit erreicht ist
    if law.lower() != "ja":
        print("Diese Funktion ist nur für Länder mit Volljährigkeit ab 18 Jahren geeignet.")
        return

    # Berechne die Anzahl an Monaten bis zum nächsten Geburtstag
    if monthCurrent < monthBirthday:
        monthsUntilBirthday = monthBirthday - monthCurrent
    elif monthCurrent > monthBirthday:
        monthsUntilBirthday = 12 - monthCurrent + monthBirthday
    else:
        monthsUntilBirthday = 0

    # Berechne das Alter nach dem nächsten Geburtstag
    ageAfterBirthday = 18

    # Überprüfe, ob die Person volljährig ist
    if monthsUntilBirthday == 0:
        print("Du bist heute Geburtstag!")
    elif monthsUntilBirthday > 0:
        print(f"Du hast in {monthsUntilBirthday} Monaten Geburtstag und wirst dann {ageAfterBirthday} Jahre alt.")
    else:
        print(f"Du bist bereits {ageAfterBirthday} Jahre alt.")

    
    if monthsUntilBirthday <= 0:
        horrormovieAnswer = horrormovie.lower()
        if horrormovieAnswer == "ja":
            print("Du kannst Horrorfilme ab 18 Jahren sehen.")
        else:
            print("Du kannst andere Filme sehen, die für dein Alter geeignet sind.")
    else:
        print(f"Du musst in {monthsUntilBirthday} Monaten wiederkommen, um den Rest der Umfrage zu beantworten.")


lawAnswer = input("Bist du in einem Land, in dem ab 18 die Volljährigkeit erreicht ist? (ja/nein): ")
monthBirthdayAnswer = int(input("In welchem Monat hast du Geburtstag? (1-12): "))
monthCurrentAnswer = int(input("Welcher Monat ist aktuell? (1-12): "))
horrormovieAnswer = input("Möchtest du gerne Horrorfilme ab 18 sehen? (ja/nein): ")
