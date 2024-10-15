# DM_Crypto_Test_MillerRabin

Ce projet utilise Python pour effectuer le test de Miller-Rabin et le visualiser sous forme de graphique. Il a été réalisé dans le cadre du cours d'Introduction à la Cryptographie en Master 1 Informatique. 

## Installation

1. Assurez-vous d'avoir Python installé sur votre système. Si ce n'est pas le cas, vous pouvez le télécharger sur [python.org](https://www.python.org/).

2. Clonez ce dépôt sur votre machine (si vous passez par GitHub) :

    ```bash
    git clone https://github.com/madisonnoyer54/DM_Crypto_Test_MillerRabin.git
    ```

3. Installez les dépendances en exécutant la commande suivante :

    ```bash
    make install
    ```

## Utilisation

1. Exécutez le script :

    ```bash
    make run
    ```

2. Le graphique s'ouvrira automatiquement à la fin de l'exécution du programme.

3. Dans notre programme, à la ligne 123 :

    ```python
    tailles_bits = [128, 256, 512, 1024, 2048, 4096]
    ```

    Ce sont les différentes valeurs de b. Pour un résultat plus rapide, je vous conseille de supprimer les 2 dernières valeurs (comme préconisé par notre enseignante Minnier).

## Contribution

Ce projet a été réalisé en binôme. Les deux participants sont NOYER Madison et FAEDO Théo.
