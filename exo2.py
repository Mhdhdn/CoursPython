choix_user = input("Bienvenue dans notre restaurant ! Voici la carte\n" \
"Steak - 13€\n"
"Frites - 4€\n"
"Salade - 5€\n"
"Boisson - 2€\n"
"Faites votre choix : ")

match choix_user:
    case "Steak":
        print("Voici un steak, 13€ s'il vous plaît")
    case "Frites":
        print("Voici des frites, 4€ s'il vous plaît")
    case "Steak":
        print("Voici une salade, 5€ s'il vous plaît")
    case "Steak":
        print("Voici une boisson, 2€ s'il vous plaît")

