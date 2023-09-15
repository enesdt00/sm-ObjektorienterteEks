from dato import dato
# først oppretter jeg en definasjon som har en objekt.
def hovedprogram():
    dato1=dato(15,8,2022)
# det kalles hent_aar metoden, så det kan skrives ut aar på terminalen
    print(dato1.hent_aar())
# Ved å kalle den metoden sjekkeDato, måler jeg først å se på  dagen min er lik en av disse registrerte dagene.
    if dato1.sjekkeDato(15):
        print("Loenningsdag!")
    if  dato1.sjekkeDato(1):
        print("Ny maaned,nye muligheter ")
   
    
    print(dato1.Skriv_Ut())
    
    
hovedprogram()
