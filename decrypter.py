message_chiffre= str(input('Entrer le message à décrypter:'))
message_dechiffre = ""
liste_alpha=[chr(i) for i in range(ord('A'), ord('Z')+1)]

for lettre in message_chiffre:
    if lettre.isalpha():
        decalage = 3 
        position_originale = liste_alpha.index(lettre.upper())
        nouvelle_position = (position_originale-decalage)%26
        lettre_dechiffree = liste_alpha[nouvelle_position]
        message_dechiffre += lettre_dechiffree if lettre.isupper() else lettre_dechiffree.lower()

    else:
        message_dechiffre +=lettre
print('Votre message décrypté est:' , message_dechiffre)
