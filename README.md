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

CHIFFREMENT AFFINE

**Description**

Ce code permet de crypter ou de décrypter un message en utilisant un chiffrement à décalage. Le chiffrement à décalage est un type de chiffrement simple qui consiste à remplacer chaque lettre du message clair par une autre lettre décalée d’un certain nombre de positions dans l’alphabet.

**Utilisation**

Pour utiliser ce code, vous devez d’abord saisir le choix que vous souhaitez effectuer :


Tapez 1 pour crypter et 2 pour décrypter :

Si vous choisissez de crypter un message, vous devez ensuite saisir le message clair et les clés de chiffrement. Les clés de chiffrement sont deux nombres entiers. La première clé de chiffrement, ‘cle1’, représente le nombre de positions à décaler vers l’avant. La seconde clé de chiffrement, ‘cle2’, représente un décalage supplémentaire qui peut être appliqué à la fin du processus de cryptage ou de décryptage.

```
Entrer le message à crypter :
Entrer la première clé de chiffrement (il doit être premier avec 26) :
Entrer la seconde clé de chiffrement :
```
Le message crypté est ensuite affiché à l’écran.

Si vous choisissez de décrypter un message, vous devez ensuite saisir le message crypté et la première clé de chiffrement.

```
Entrer le message à décrypter :
Entrer la première clé de chiffrement (il doit être premier avec 26) :
Entrer la seconde clé de chiffrement :
```

Le message décrypté est ensuite affiché à l’écran.

**Exemples**

**Cryptage**

```
Tapez 1 pour crypter et 2 pour décrypter :
1
Entrer le message à crypter :
Bonjour
Entrer la première clé de chiffrement (il doit être premier avec 26) :
3
Entrer la seconde clé de chiffrement :
5
Votre message crypté est :
ivsgvne 

**Déchiffrement**

```
Tapez 1 pour crypter et 2 pour décrypter :
2
Entrer le message à décrypter :
ivsgvne 
Entrer la première clé de chiffrement (il doit être premier avec 26) :
3
Entrer la seconde clé de chiffrement :
5
Votre message décrypté est :
Bonjour
```

**Fonctionnement**

Le code fonctionne comme suit :

1. La fonction ‘math.gcd()’est utilisée pour vérifier que la première clé de chiffrement est premier avec 26. Un nombre premier est un nombre qui n’a que deux diviseurs : 1 et lui-même. Si la première clé de chiffrement n’est pas premier avec 26, l’utilisateur est prié d’entrer une nouvelle valeur valeur jusqu’à ce que le clé soit premier avec 26
2. Si la première clé de chiffrement est premier avec 26, alors le message clair est crypté en remplaçant chaque lettre par une autre lettre décalée d’un certain nombre de positions dans l’alphabet.
3. La fonction ‘pow()’est utilisée pour calculer l’inverse de la première clé de chiffrement. L’inverse d’un nombre est un autre nombre qui, multiplié par le premier nombre, donne 1. L’inverse de la première clé de chiffrement est utilisé pour décrypter le message.
4. Si le choix de l’utilisateur est 2, alors le message crypté est déchiffré en remplaçant chaque lettre par une autre lettre décalée d’un certain nombre de positions dans l’alphabet, en utilisant l’inverse de la première clé de chiffrement.

CHIFFREMENT POLYBE

Ce code permet de chiffrer et déchiffrer des messages à l’aide du chiffrement de Polybe.

* Fonctionnement

Le chiffrement de Polybe est un chiffrement par substitution monoalphabétique. Il fonctionne en remplaçant chaque lettre du message par une autre lettre, selon une grille de Polybe.

La grille de Polybe est une grille de 5 x 5, avec les lettres de l’alphabet disposées de manière aléatoire.

*Utilisation

Pour chiffrer un message, il suffit de suivre les étapes suivantes :

1. Entrez la clé du chiffrement de Polybe ou la lettre de début
2. Entrez le message à chiffrer.
3. Lancez le programme.

Le programme affichera le message chiffré.

Pour déchiffrer un message, il suffit de suivre les étapes suivantes :

1. Entrez la clé du chiffrement de Polybe ou la lettre de début
2. Entrez le message à déchiffrer.
3. Lancez le programme.

Le programme affichera le message déchiffré.

## Options

Le programme offre deux options de chiffrement :

* Chiffrement avec clé : Le message est chiffré en utilisant la clé fournie.
* Chiffrement avec lettre de début : Le message est chiffré en utilisant une lettre de début fournie.

## Exemples

Voici quelques exemples d’utilisation du programme :


# Chiffrement avec clé

Cle = “SECRET”
Message  clair = “Bonjour!”
 Message chiffré:
22444334445514
# Chiffrement avec lettre de début
Lettre_debut = “B”
Message  clair= “Bonjour!”
 Message chiffré :
 11353425355143
```
Déchiffrement avec clé
Message chiffré :
22444334445514
Message  clair = “Bonjour!”
Déchiffrement avec letter de début
Message chiffré :
 11353425355143
Message clair = “Bonjour!”





```








