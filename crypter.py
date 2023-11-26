message_clair= str(input('Entrer le message à crypter:'))
message_chiffre = ""
liste_alpha=[chr(i) for i in range(ord('A'), ord('Z')+1)]

for lettre in message_clair:
    if lettre.isalpha():
        decalage = 3 
        position_originale = liste_alpha.index(lettre.upper())
        nouvelle_position = (position_originale+decalage)%26
        lettre_chiffree = liste_alpha[nouvelle_position]
        message_chiffre += lettre_chiffree if lettre.isupper() else lettre_chiffree.lower()

    else:
        message_chiffre +=lettre
print('Votre message crypte est:' , message_chiffre)         