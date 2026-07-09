from getpass import getpass
from random import randint


nombre_un = randint(1,100)
nombre_deux = int(input ("JOUEUR DEUX A VOTRE TOUR... DEVINEZ !!! "))
while True : 
    if nombre_deux < nombre_un :
        nombre_deux = int(input("TROP BAS, REESSAYEZ "))
    elif nombre_deux > nombre_un:
        nombre_deux = int(input("TROP HAUT, REESSAYEZ"))
    elif nombre_deux == nombre_un :
        print ("FELICITATIONS...")
        break