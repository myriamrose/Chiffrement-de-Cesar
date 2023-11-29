def grille(cle , lettre_debut= None):
# Convertir la cle en majuscules et supprimer les doublons
    cle_formate =[]
    for char in cle:
        if char in cle.upper() and char not in cle_formate:
          cle_formate.append(char)

    for char in cle.upper():
        if char not in cle and char not in cle_formate:
          cle_formate.append(char)
    cle_formate ="".join(cle_formate)
    
# Creer l'alphabet sans la cle
    alphabet ="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    alphabet ="".join(filter(lambda x: x not in cle, alphabet))

# Concatener la cle et l'alphabet pour former la grille
   
    alphabet_grille = cle_formate + alphabet

# Creer la grille de polybe
    grille_polybe = [list(alphabet_grille[i:i+5])for i in range(0,25,5)]

    if lettre_debut is not None:
     for i in range(5):
        for j in range(5):
           if grille_polybe[i][j]==lettre_debut:
              grille_polybe[0][0]== grille_polybe[i][j]
              grille_polybe[i][j]==lettre_debut
    return grille_polybe

def position_lettre(lettre, grille_polybe):
    lettre = lettre.replace("J","I")
    for i in range(5):
        for j in range(5):
            if grille_polybe[i][j]==lettre:
                return i, j
    return None

choix = int(input("Tapez 1 pour crypter et 2 pour décrypter : "))

if choix == 1:

 def chiffrement_polybe(message, grille_polybe):
    message_chiffree=" "
    for lettre in message.upper():
        if lettre.isalpha() :
            position = position_lettre(lettre, grille_polybe)
            if position:
                message_chiffree += str(position[0] + 1) + str(position[1] + 1)
        else:
            message_chiffree += lettre
    return message_chiffree

 choix = int(input("Tapez 1 pour crypter avec un mot clé et 2 pour choisir la lettre de début de la grille de Polybe : "))
 if choix == 1:
   cle = str(input('Entrer la cle du chiffrement de polybe:'))
   message = str(input('Entrer le message a crypter:')) 
   print("Message chiffre: ", chiffrement_polybe(message, grille(cle)))
 elif choix == 2:  
    lettre_debut = str(input('Entrer la lettre de début de la grille:'))
    message = str(input('Entrer le message a crypter:'))
    print("Message chiffre: ", chiffrement_polybe(message, grille(lettre_debut)))
 



elif choix == 2:
 def dechiffrement_polybe(message_chiffre, grille_polybe):
    message_dechiffree=""
    positions = [int(paire) for paire in message_chiffre if paire.isdigit()]
    for i in range(0, len(positions), 2):
        if i+1 < len(positions):
            ligne, colonne= positions[i] - 1, positions[i+1]-1
            if 0 <= ligne < 5 and 0 <= colonne < 5:
                message_dechiffree += grille_polybe[ligne][colonne]+''
            else:
                message_dechiffree += ''
        else:
            message_dechiffree += ''
    return message_dechiffree
 
 choix = int(input("Tapez 1 pour décrypter avec un mot clé et 2 pour choisir la lettre de début de la grille de Polybe : "))
 if choix == 1:
   cle = str(input('Entrer la cle du chiffrement de polybe:'))
   message = str(input('Entrer le message a décrypter:'))
   print("Message déchiffré: ", dechiffrement_polybe(message, grille(cle)))

 elif choix == 2:  
    lettre_debut = str(input('Entrer la lettre de début de la grille:'))
    message = str(input('Entrer le message a décrypter:')) 
    print("Message déchiffré: ", dechiffrement_polybe(message, grille(lettre_debut)))



   
