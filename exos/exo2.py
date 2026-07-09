budget = 25
prix_steak = 13
prix_frites = 4
prix_salade = 5
prix_boisson = 2

while budget > 0 :
    
    choix_user = input("Bienvenue dans notre restaurant ! Voici la carte\n" \
"Steak - 13€\n"
"Frites - 4€\n"
"Salade - 5€\n"
"Boisson - 2€\n"
"Faites votre choix : ")
    message_retour = "Voici un %s , Bon appétit" %choix_user
    match choix_user:
        case "Steak":
            choix_user = "Steak"
            budget = budget - 13
            print(message_retour)
        case "Frites":
            choix_user = "Frites"
            budget = budget - 4
            print(message_retour)
        case "Salade":
            choix_user = "Salade"
            budget = budget - 5
            print(message_retour)
        case "Boisson":
            choix_user = "Boisson"
            budget = budget - 2
            print(message_retour)
    if budget <= 0 :
        print("Vous n'avez pas assez d'argent")
print ("Vous n'avez plus d'argent")

