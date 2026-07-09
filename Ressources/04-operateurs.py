#OPERATEURS ARYTMETIQUES = OPERATIONS MATHEMATIQUES
nombre_un = 5
nombre_deux = 10

la_somme = 5 + 10 
la_somme_variables = nombre_un + nombre_deux

la_difference = nombre_deux - nombre_un

#print("ABC " * 20)

#OPERATEURS DE COMPARAISONS 

egalite = 10 == 11 #false

difference = 10 != 11 #True

superiorite = 10 > 5 #True

superiorite_ou_egalite = 10 >= 5 #True

inferiorite = 10 < 5 #False

inferiorite_ou_egalite = 5 <= 10 #True

#OPERATEURS LOGIQUES

possede_carte_bibliotheque = True
argent = 25
age = int(input("Quel âge avez vous ?")) #INT TRANSFORME LA CHAINE DE CARACTERES ENTREES DANS L'INPUT EN CHIFFRE AFIN DETRE TRAITEE COMME TEL

acces_bibliotheque = age >= 12 and possede_carte_bibliotheque

acces_avec_paiement_possible_2_euros = argent >= 2 or possede_carte_bibliotheque

est_mineur = not(age >= 18)
