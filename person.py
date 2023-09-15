# her definerer jeg en klasse, navnet sitt er person som tar to parameter.
class person:
    def __init__(self,navn,alder):
        self._navn=navn
        self._alder=alder
        self._hobbyer=[]
# Første innsants metoden tar in i hobbyer.
    def leggTilHobby(self,hobbyer):
        self._hobbyer.append(hobbyer)
#  andre metoden skriver ut de hobbyene.
    def skrivHobbyer(self): 
        for i in range(len(self._hobbyer)):
             print(self._hobbyer[i], end=", ")
 # denne metoden kaller først den andre metoden (' skrivHobbyer'), og etterpå returnerer navn og alder 
    def skrivUt(self):
       self.skrivHobbyer() 
       return  self._navn,self._alder

