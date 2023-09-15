from motorsykkel import motorsykkel
# først oppretter jeg en definasjon som har tre objekter.
def hovedprogram():
    motorsykkel1=motorsykkel("Yamaha","92664 DXCMC")
    motorsykkel2=motorsykkel("BMW","26545 AXC")
    motorsykkel3=motorsykkel("Suzuki","95432 PKA")
# Her kaller jeg noen metoder som er villet i obligen
    print(motorsykkel1.skriv_ut())
    print(motorsykkel2.skriv_ut())
    print(motorsykkel3.skriv_ut())
    motorsykkel3.kjoer(10)
# Jeg definerer en betingelse ved å bruke assert. Ved å bruke assert her,vil jeg vurdere koden kjøres som det skal. 
    assert motorsykkel3.hent_kilometerstand()==10
    print(motorsykkel3.hentMerke(),"kilometerstand:",motorsykkel3.hent_kilometerstand())
   

hovedprogram() 
