def testwachtwoord(wachtwoord):
    if len(wachtwoord) < 8:
        print("Slecht wachtwoord")
        return
    if  hoofdletters and not str.isalpha(wachtwoord):
        print("Goed wachtwoord")
        return
    print("Redelijk wachtwoord")

wachtwoord = input ("Voer een wachtwoord in")
hoofdletters = [l for l in wachtwoord if l.isupper()]
testwachtwoord(wachtwoord);
