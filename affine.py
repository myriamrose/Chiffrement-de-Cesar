import math

choix = int(input("Tapez 1 pour crypter et 2 pour décrypter : "))

if choix == 1:
    message_clair = str(input('Entrer le message à crypter:'))
    cle1 = int(input('Entrer la première clé de chiffrement(il doit être premier avec 26):'))
    while math.gcd(cle1, 26) != 1:
      print(cle1, 'doit etre premier avec 26')
      cle1 = int(input('Entrer la première clé de chiffrement(il doit être premier avec 26):'))
      
    cle2 = int(input('Entrer la seconde clé de chiffrement:'))
    message_chiffre = ""
    liste_alpha=[chr(i) for i in range(ord('A'), ord('Z')+1)]

    for lettre in message_clair:
         if lettre.isalpha():
          x = liste_alpha.index(lettre.upper())
          nouvelle_position = (cle1 * x + cle2) % 26
          lettre_chiffree = liste_alpha[nouvelle_position]
          message_chiffre += lettre_chiffree if lettre.isupper() else lettre_chiffree.lower()
         else:
           message_chiffre += lettre
    print('Votre message crypté est:' , message_chiffre)
    
elif choix == 2:
    message_chiffre = str(input('Entrer le message à décrypter:'))
    cle1 = int(input('Entrer la première clé de chiffrement(il doit être premier avec 26):'))
    while math.gcd(cle1, 26) != 1:
     print(cle1, 'doit etre premier avec 26')
     cle1 = int(input('Entrer la première clé de chiffrement(il doit être premier avec 26):'))

    cle2 = int(input('Entrer la seconde clé de chiffrement:'))
    message_dechiffre = ""
    liste_alpha=[chr(i) for i in range(ord('A'), ord('Z')+1)]
    a_inv = pow(cle1, -1, 26)

    for lettre in message_chiffre:
       if lettre.isalpha():
        y = liste_alpha.index(lettre.upper())
        ancienne_position = (a_inv * (y-cle2)) % 26
        lettre_dechiffree = liste_alpha[ancienne_position]
        message_dechiffre += lettre_dechiffree if lettre.isupper() else lettre_dechiffree.lower()
       else:
         message_dechiffre += lettre
    print('Votre message décrypté est:' , message_dechiffre)
    
else:
   print("Choix erroné!!!")





    

       
       













