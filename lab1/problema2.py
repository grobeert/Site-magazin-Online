s = int(input("Introdu un numar: "))

while s!=0:
    print(s%10,end="")
    s=s//10

#print(s)
import random


def is_prime(n):

    if n < 2: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    
    # Verificăm divizorii până la rădăcina pătrată a lui n
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def generate_prime(k):

    minim = 10**(k-1)
    maxim = (10**k) - 1
    
    while True:
        # Generăm un număr aleatoriu în intervalul corect
        numar = random.randint(minim, maxim)
        
        # Optimizare: numerele pare nu sunt prime (în afară de 2)
        if numar % 2 != 0 and is_prime(numar):
            return numar

# Testăm pentru 15 cifre
print("Generăm un număr prim de 15 cifre...")
rezultat = generate_prime(15)
print(f"Numărul generat: {rezultat}")