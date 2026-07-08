from getpass import getpass
from random import randint


nombre_un = randint(1,10)
nombre_deux = input ("JOUEUR DEUX A VOTRE TOUR... DEVINEZ !!! ")
while True : 
    if nombre_deux < nombre_un :
        nombre_deux = input("TROP BAS, REESSAYEZ ")
    if nombre_deux > nombre_un:
        nombre_deux = input("TROP HAUT, REESSAYEZ")
    if nombre_deux == nombre_un :
        print ("FELICITATIONS...")
        break