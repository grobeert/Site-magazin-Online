import random

s = input("Introdu un mesaj: ")

# 1. Afișare inversă
print(s[::-1])

# 2. Afișare litere aleatorii (mici/MARI)
print("Litere amestecate: ", end="")
for litera in s:
    if random.randint(1, 2) == 1:
        print(litera.lower(), end="")
    else:
        print(litera.upper(), end="")
print("\n") 

n = 17
rezultat = ""

for litera in s:
    if litera.isalpha(): 
        if litera.isupper(): 
            baza = ord('A') 
        else: 
            baza = ord('a')
        cod_nou = (ord(litera) - baza + n) % 26 + baza
        rezultat += chr(cod_nou)
    else:
        rezultat += litera
print(rezultat)