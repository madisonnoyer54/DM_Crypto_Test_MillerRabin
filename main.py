import secrets
from sympy import symbols, Eq, solve
import random


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
test_valeur = range(2, 10002)  # Commence à partir de 2 car la décomposition n'est pas définie pour n=1
for n in test_valeur:
    s, d = Decomp(n)
    if(n-1 != 2**s*d):
        print("Le teste de la question 3 à echoué avec les valeur s = {s} d = {d}")



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
for z in range(10000) :
    a =  random.randint(1, 10000)
    t =  random.randint(1, 10000)
    n =  random.randint(1, 10000)
    f = ExpMod(n,a,t)
    if(f != a**t % n):
        print(f"Le teste de la question 4 a échouer sur les valeur a= {a} t = {t} et n = {n}")
  

# Question 5

def MillerRabin(n, cpt):
    for _ in range(cpt):
        stop = False
        # 1
        s, d = Decomp(n) 

        if d % 2 == 0:
            print(" d n'est pas impair")

        # 2
        a = random.randint(1, n-1)

        # 3
        resultat = ExpMod(n, a, d)
        if resultat == 1 or resultat == - 1:
            stop = True

        # 4
        i = 0
        while i < s or stop == False:
            resultat = ExpMod(n, a, d * 2**i)
            if resultat == - 1:
                stop = True
            elif resultat == 1:
                return 0
            i= i+1

        # 5 
        if(i == s and ExpMod(n, a, d * 2**i) != 1):
            return 0

    return 1

# 0 si composé 
# 1 si premier
print(MillerRabin(17, 20))