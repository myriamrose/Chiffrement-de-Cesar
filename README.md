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