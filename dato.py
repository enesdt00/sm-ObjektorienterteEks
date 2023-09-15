# først har jeg en klass, navnet sitt dato.
# Det er tre parametere til konstruktør slik ny_dag,ny_maaned,ny_aar.
class dato:
    def __init__(self,ny_dag,ny_maaned,ny_aar):
        self._dag=ny_dag
        self._maaned=ny_maaned
        self._aar=ny_aar
        # her er det en instansmetoden som skriver ut ny_aar parameteren.
    def hent_aar(self):
        return self._aar
        # Her definerer jeg en variabel som er i en tekststring, og definerer en list som er tomt i begynnelse og tar in i alle parameterene  som en elementer.
    def Skriv_Ut(self):
        tekstStreng=str(self._dag)+" "+str(self._maaned)+" "+str(self._aar)
        print(tekstStreng)
        tekstList=[]
        for i in tekstStreng.split(" "):
            tekstList.append(i)
# Til slutt retunerer de elementene.
        return tekstList[0]+"."+tekstList[1]+"."+tekstList[2]
#  en metod som tar in  i en ny parameter. I den metoden sammelignes de to variabler ny_dag og nydag.
    def sjekkeDato(self,nyDag):
        if self._dag==nyDag:
           return True
        else:
           return False
    def sekkeDato1(self,nydag):
        print("sadasda")
    



        
        
        
    