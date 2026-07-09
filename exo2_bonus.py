menu = {
    "1": ("Coca Cola", 1.00),
    "2": ("Burger", 6.00),
    "3": ("Tacos", 7.00),
    "4": ("Milkshake", 4.00),
    "5": ("Steak", 13.00),
    "6": ("Pomme", 0.50)
}



budget = float(input("Quel est votre budget ? "))
commande = []
total = 0.0

while True: 
    print("\n### MENU ###")
    elements = menu.items()

    for menu_nb, (nom_produit, prix) in elements:
        print(f"{menu_nb}. {nom_produit} [Prix : €{prix:.2f}]")
    print(f"\nIl vous reste actuellement € {budget} ")
    print(f"Total actuel de la commande: € {total} ")

    choix_user = input("Que voulez vous aujourd'hui ?")

    if choix_user == "0":
        break
    
    if choix_user not in menu:
        print("CHOIX INVALIDE")
        continue

    nom_produit, prix_produit = menu[choix_user]

    if total + prix_produit > budget : 
        print("BUDGET DEPASSE, CHOIX IMPOSSIBLE")
        continue

    commande.append(nom_produit)
    total += prix_produit
    budget = budget - prix_produit
    print(f"Le produit '{nom_produit} a bien été à la commande")

print("### COMMANDE ###")
for produit in commande: 
    print(f"-{produit}")
print (f"{total:.2f}")
print (f"Budget restant : €{budget - total}")

