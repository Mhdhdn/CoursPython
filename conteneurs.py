mon_nombre = 123
mes_nbs = [1, 2, 3, 4, 5]
mes_mots = ["pense", "croyaisque", "ilaledroit"]
mes_nb_virg = [1.23, 2.44, 56.6]
mes_booleens = [True, False, True, False]
mes_elements = ["pensing", 1, True, 2.33]

mon_deuxieme_nb = mes_nbs[1]
print(mon_deuxieme_nb)

mes_nb_du_2_au_4 = mes_nbs[1:3]
print(mes_nb_du_2_au_4)

la_date = "DD/MM/YYYY"
la_date_ensemble = la_date.split('/')
print(la_date_ensemble)
jour, moi, annee = la_date_ensemble

print(jour) #DD

#pour ajouter des choses a une liste : append (un a la fois)

liste_vide = [] #ou list()

liste_vide.append ("jepense")
print(liste_vide)

liste_vide.extend(["zozomapampa", 1234, True]) #EXTEND AJOUTE PLUSIEURS A LA FOIS

print(liste_vide)

liste_vide.pop() #par defaut retire le dernier element, POP prend en compte que les int
liste_vide.pop(0) #retire le premier element 
liste_vide.remove("zozomapampa") #retire zozo de la liste

print(liste_vide)

liste_vide.insert(1, "ilaledroit?") #insert ajoute un element à la position selectionnée, ici 2e
print(liste_vide)

liste_vide.count("jepense") #compte le nb de jepense dans la liste

len(liste_vide) #donne la longueur de la liste

#Utilisation range

mes_nb_de_1a10 = [range(11)]



##autres types de contenants 

## TUPLE () - liste non modifiable

## SET {} - Liste ne permettant pas les dupliques, permet de faire des comparaisons (venn diagram), permet de connaitres le nombres d'options diff(exemple connaitre le nombre de pomme, banane etc sans difficulté)

## DICTIONNAIRE - associer une clé à un element 

carnet_dadresse = {"Elliot": "5 rue jean jaures", 
    "John": "Rue de la criss",
    "Andrew": "45 place de G"
 }

#pour trouver l'adresse 

print(f"Adresse d'Elliot : {carnet_dadresse["Elliot"]}")

carnet_dadresse["Lola"] = "11 avenue du 14 Juillet" #ceci crée une clé (Lola) et lui attribue une adresse

print(f"L'adresse de Lola est : {carnet_dadresse['Lola']}")

new_person = input("entrer le nom")
carnet_dadresse[new_person] = input("entrez l'adresse")
for adresse in carnet_dadresse
