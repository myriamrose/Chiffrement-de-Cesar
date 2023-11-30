# Chiffrement-de-Cesar
CHIFFREMENT DE CESAR

Ce code permet de chiffrer et de déchiffrer des messages en utilisant un chiffrement par décalage.

Principe du chiffrement par décalage
Le chiffrement par décalage est un chiffrement par substitution simple. Il consiste à remplacer chaque lettre du message clair par une autre lettre décalée d’un certain nombre de positions dans l’alphabet.

Utilisation du code
Pour utiliser le code, vous devez d’abord entrer le message que vous souhaitez chiffrer ou déchiffrer. Le code est déjà implémenté avec le décalage(3).
Le code affichera le message chiffré ou déchiffré.

**Exemples**

**Chiffrement**
Message_clair = “Bonjour tout le monde !”
Decalage = 3

message_clair= str(input('Entrer le message à crypter:'))
print('Votre message crypte est:' , message_chiffre) 


**Sortie**
Message clair : Bonjour tout le monde !
Message chiffré : Erqmrxu wrxw oh prqgh !

**Déchiffrement**

Message_chiffre = “Erqmrxu wrxw oh prqgh !”
Decalage = 3

message_chiffre= str(input('Entrer le message à décrypter:'))
print('Votre message décrypté est:' , message_chiffre)

**Sortie**

```
Message chiffré : Erqmrxu wrxw oh prqgh !
Message clair: Bonjour tout le monde !
```

**Explication**

Dans l’exemple ci-dessus, le message clair est “Bonjour tout le monde !”. Le décalage est de 3.

Pour chiffrer le message, chaque lettre est remplacée par la lettre décalée de 3 positions dans l’alphabet. Par exemple, la lettre “B” est remplacée par la lettre “D”.

Le message chiffré est donc “Erqmrxu wrxw oh prqgh !”.

Pour déchiffrer le message, chaque lettre est remplacée par la lettre décalée de 3 positions dans l’alphabet inverse. Par exemple, la lettre “D” est remplacée par la lettre “B”.

Le message clair est donc “Bonjour tout le monde !”.
