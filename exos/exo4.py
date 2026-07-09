notes_list = list()

while True : 
    notes_in = (input("Entrez vos notes séparées par une virgule"))
    notes_list = notes_in.split(',')
    break
print(notes_list)

print("Votre note la plus élevée est : ", (max[notes_list]),"/20")






























#input("""           ###NOTES###
 #   1- Entrer une nouvelle note
  #  2 - Consulter l'ensemble des notes
   # 3 - Connaitre la plus petite note
    #4 - Connaitre la plus grande note 
    #5 - Connaitre la moyenne des notes 
    #0 - quitter
      
    #-->:""")



