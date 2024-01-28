import secrets
from sympy import symbols, Eq, solve
import random

#random_bits = secrets.randbits(n)


# Question 3
def Decomp(n):
    # Décomposer n - 1 en 2^s * d
    d = n - 1
    s = 0 # Donc 2^s = 1

    # On divise par 2 
    while d % 2 == 0:
        s += 1 # On compte combien de fois on divise d
        d //= 2 # On divise d

    return s, d

# Test de Decomp sur 10000 valeurs différentes
test_values = range(2, 10002)  # Commence à partir de 2 car la décomposition n'est pas définie pour n=1

for n in test_values:
    s, d = Decomp(n)
    if(n-1 != 2**s*d):
        print("Le teste à echoué : n - 1 = 2^s * d")

"""
Cette m´ethode rapide d’exponentiation modulaire est d´ecrite dans l’Annexe A. Il s’agit donc d’impl´e-
menter ici cette m´ethode sous la forme d’une fonction ExpMod() qui prend en entr´ee n, a et t et qui
renvoie en sortie at mod n.

Question 4. Impl´ementez la fonction ExpMod(). Testez-la sur 10000 valeurs diff´erentes.



"""

# Question 4 
def ExpMod(n, a, t):
    # Mettre t en binaire 
    t_binaire = bin(t)[2:]

    # Prendre la taille 
    r = len(t_binaire)

    # t = 1
    if t_binaire == '1':
        return a % n

    # t est pair
    elif t_binaire[-1] == '0':
        return ExpMod(n, (a**2) % n, t // 2)
      
    # t est impair
    else: 
        return (a * ExpMod(n, (a**2) % n, (int(t) - 1) // 2)) % n


# Test sur 10000 valeurs différentes
test_values = range(1, 10001) 
for z in test_values:
    a =  random.randint(1, 500)
    t =  random.randint(1, 500)
    n =  random.randint(1, 500)
    f = ExpMod(n,a,t)
    if(f != a**t % n):
        print("Le teste a échouer")
  


