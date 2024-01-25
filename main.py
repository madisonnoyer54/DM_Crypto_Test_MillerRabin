import secrets
from sympy import symbols, Eq, solve

#random_bits = secrets.randbits(n)


# Question 3
def Decomp(n):
    # Décomposer n - 1 en 2^s * d
    d = n - 1
    s = 0 # Donc 2^s = 1

    # On divise par 2 
    while d % 2 == 0:
        s += 1
        d //= 2

    return s, d

# Test sur 10000 valeurs différentes
test_values = range(2, 10002)  # Commence à partir de 2 car la décomposition n'est pas définie pour n=1
results = []

for n in test_values:
    s, d = Decomp(n)
   # print(n-1, '=',2**s*d)
    if(n-1 != 2**s*d):
        print("Le teste à echoué")




