import secrets
import random
import matplotlib.pyplot as plt


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
for _ in range(10000):
    n =  random.randint(2, 100000)
    s, d = Decomp(n)
    if(n-1 != 2**s*d):
        print(f"Le teste de la question 3 à echoué avec les valeur n={n} s = {s} d = {d}")



# Question 4 
# Avec python on ne peux pas faire de la recursion sur des grand nombre sens faire tout planter, donc voici une version adapter.
def ExpMod(n, a, t):
    result = 1
    a = a % n  

    # Mettre t en binaire 
    t_binaire = bin(t)[2:]  

    # Prendre la taille 
    r = len(t_binaire)

    for i in range(r):
        if t_binaire[r - i - 1] == '1':
            result = (result * a) % n
        a = (a * a) % n

    return result

# Test de ExpMod sur 10000 valeurs différentes
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

        # verifie que d impair 
        if d % 2 == 0:
            print(" d n'est pas impair")

        # 2
        a = random.randint(1, n-1)

        # 3
        resultat = ExpMod(n, a, d)
        if resultat == 1 or resultat == - 1:
            stop = True # On peut rien dire et on arret 

        # 4
        i = 0
        while i < s and stop == False:
            resultat = ExpMod(n, a, d * 2**i)
            if resultat == -1:
                stop = True # On peut rien dire et on arret 
            elif resultat == 1:
                return 0 # conclure n est composer 
            i= i+1

        # 5 
        if(i == s and ExpMod(n, a, d * 2**i) != 1 and stop == False):
            return 0 # conclure que n composer 


    return 1




# Question 6
n1 = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF"
n1 = int(n1, 16)
print("n1 (768 bits) =", MillerRabin(n1, 20))

n2 = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEC4FFFFDAF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000002D9AB"
n2 = int(n2, 16)
print("n2 (768 bits) =", MillerRabin(n2, 20))

n3 = "FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF"
n3 = int(n3, 16)
print("n3 (1024 bits) =", MillerRabin(n3, 20))


# Question 7
def Eval(b, cpt):
    compteur = 0
    n = secrets.randbits(b)
    while MillerRabin(n, cpt) == 0 :
        compteur = compteur + 1
        n = secrets.randbits(b)
     
    return compteur



# Question 8
tailles_bits = [128, 256, 512, 1024, 2048, 4096]
moyennes = []

for taille in tailles_bits:
    compteurs = []
    for _ in range(100):
        compteurs.append(Eval(taille, 20))
    moyenne_compteur = sum(compteurs) / 100
    moyennes.append(moyenne_compteur)


# Graphe
plt.plot(tailles_bits, moyennes, marker='o')
plt.xlabel('Taille en bits du nombre')
plt.ylabel('Moyenne du nombre de répétitions')
plt.title('Moyenne du nombre de répétitions en fonction de la taille du nombre')
plt.grid(True)
plt.show()