from getpass import getpass

nombre_un = int(getpass("JOUEUR UN ENTREZ UN NOMBRE SECRET")) 

if not (nombre_un >= 0 and nombre_un <= 100) : 
    print("NOMBRE NON COMPRIS ENTRE 0 ET 100 TRICHEUR")
else : 
    while True : 

        nombre_deux = input ("JOUEUR DEUX A VOTRE TOUR... DEVINEZ !!! ")

        if nombre_deux < nombre_un :
            nombre_deux = input("TROP BAS, REESSAYEZ ")
        if nombre_deux > nombre_un:
            nombre_deux = input("TROP HAUT, REESSAYEZ")
        else : print ("FELICITATIONS...")
        break