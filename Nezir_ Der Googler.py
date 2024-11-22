import webbrowser

print("Schreib suche")

while True:
    eingabe = input ("")
    if eingabe == "suche":
        webbrowser.open("http://www.google.com/")
    
    else:
        print("schreib suche jetzt sofort")