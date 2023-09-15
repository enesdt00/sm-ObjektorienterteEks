#  først må jeg importere den klassen 'person' som vanlig.
from person import person
# her er det en hovedprogram som ber to variabler fra brukeren.
# De variablene brukes in i den objekten slik info1.
def hovedprogram():
    navn1=input("Skriv et navn:")
    alder1=input("skriv en alder:")
    info1=person(navn1,alder1)
 # jeg oppreter en while-løkken på den måten kan brukeren kalle metoden så mye han vil. 
    i=0
    while i!=1:
        loekken=input("Trykk 'p' for å forsette å legge ny hobby, trykk 's' for å slutte programmet:")
        if loekken=='p' or loekken=='P':
            hobby1=input("Skriv ei hobby:")
            info1.leggTilHobby(hobby1)
        elif loekken=='s' or loekken=='S':
            i=1
        else:
            print("udefinert karakter")
    
    print(info1.skrivUt())
hovedprogram()
