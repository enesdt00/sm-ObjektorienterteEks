from hund import hund
# først oppretter jeg en definasjon som har en objekt.
def hovedprogram():
    hund1=hund(3,13)
    teller1=0
# Her bruker jeg en while-løkken. Jeg vet at det ikke er nødvendig,men jeg vil ikke kalle spring.metode fra linje til linje.
# Så spring metoden kalles 5 ganger i den løkken.
    while teller1<=4:
        hund1.spring()
        teller1+=1
    
    print("vekten til hund er:",hund1.hent_vekt())
    hund1.spring()
    print("vekten til hund er:",hund1.hent_vekt())
# Samme som før lager jeg en annen løkken. Så spis.metoden skal kalles 5 ganger. Etterpå skal det vises endringen av vekten.
    teller2=0
    while teller2<=4:
         hund1.spis(2)
         teller2+=1
    print("vekten til hund er:",hund1.hent_vekt())
    hund1.spis(2)
    print("vekten til hund er:",hund1.hent_vekt())

hovedprogram()

    