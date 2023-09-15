# først definerer jeg en klass, navnet sitt er motorsykkel. Det er to parametere til konstruktør, men det tre variabler inn i konstruktøren. 
# kilometerstand er lik '0' i begynnelsen.
class motorsykkel:
    def __init__(self,merke,registeringsnummer):
        self._merke=merke
        self._registeringsnummer=registeringsnummer
        self._kilometerstand=0
# Her definerer jeg noen hent metoder, så variablene kan skrives når hovedprogram kjøres.
    def hentMerke(self):
        return self._merke
    def hentRegnum(self):
        return self._registeringsnummer
# Her ber kjøer metoden en argument fra brukeren.Avhengig av den øker den kilometerstanden.
    def kjoer(self,km):
        self._kilometerstand+=km
    def hent_kilometerstand(self):
        return self._kilometerstand
    def skriv_ut(self):
        return self._merke,self._registeringsnummer,self._kilometerstand