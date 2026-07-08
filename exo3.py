from getpass import getpass

nombre_un = getpass("JOUEUR UN ENTREZ UN NOMBRE SECRET") 
nombre_deux = input ("JOUEUR DEUX A VOTRE TOUR... DEVINEZ !!! ")
while True : 
    if nombre_deux < nombre_un :
        nombre_deux = input("TROP BAS, REESSAYEZ ")
    if nombre_deux > nombre_un:
        nombre_deux = input("TROP HAUT, REESSAYEZ")
    if nombre_deux == nombre_un :
        print ("FELICITATIONS...")
        break