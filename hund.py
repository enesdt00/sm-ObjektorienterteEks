# først har jeg en klass, navnet sitt hund.
# Det er to parametere til konstruktør,men det tre innsants variabler inn i konstruktøren. 
class hund:
    def __init__(self,alder,vekt):
        self._alder=alder
        self._vekt=vekt
        self._mettHet=10
# Det er noen innsants metoder som skriver ut alder og vekt.
    def hent_alder(self):
        return self._alder
    def hent_vekt(self):
        return self._vekt
# Når denne metoden kalles,reduseres mettHet går ned med en tall. Avhenging av den reduseringen kan vekten går ned med en tall også.
    def spring(self):
        self._mettHet-=1
        if self._mettHet<5:
            self._vekt-=1
        else:
            self._vekt=self._vekt
        return self._mettHet, self._vekt
# Den metoden tar inn i en parameter. Den parameteren påvirker først mettHet.
    def spis(self,hentall):
        self._mettHet+=hentall
        if self._mettHet>7:
            self._vekt+=1
        else:
            self._vekt=self._vekt
        return self._mettHet,self._vekt

