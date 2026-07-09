mon_texte = "je suis texte"

nb_caractère_mon_texte = len(mon_texte)
mon_texte_maj = mon_texte.upper()
mon_texte_min = mon_texte.lower()

for lettre in mon_texte:
    print (lettre)

septieme_lettre = mon_texte[6] #on commence a compter à 0 et on compte les espaces

print(septieme_lettre)

#determiner consonne voyelle 

lettre_input_maj = input("saisir une lettre").upper()

if lettre_input_maj in "AEIOUY":
    print(f"La lettre {lettre_input_maj} est une voyelle") 
else :
    print(f"La lettre {lettre_input_maj} est une consonne")

print(f"est ce que le nombre 10 est supérieur à 7 ? {10<7}")

resultat_ternaire = "OUI" if 10>7 else "NON" 

print(f"Est-ce que le nombre 10 est supérieur à 7 ? {'OUI' if 10>7 else 'NON'}") 

de_la_lettre_2_a_5 = mon_texte[1:4]
a_partir_de_la_5e_lettre = mon_texte[4:]
jusqua_la_6e_lettre = mon_texte[:5]

prenom_input_user = input("entrez votre prenom")
prenom_formate = prenom_input_user[0].upper() + prenom_input_user[1:].lower()

fruits_txt = "pomme,abricot,banane,mangue,kiwi"

print(f"texte brut : {fruits_txt}")

ensemble_fruit = fruits_txt.split(',')

for fruit in ensemble_fruit:
    print(fruit)

from math import pi
nombre_a_virgule = pi

print(f"Valeur de pi : {pi:.4f}")

print("""### MENU ### 
1. sanwich
2. Cocabienfrais
3. Tasty crousty""")