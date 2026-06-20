from collections import Counter

with open("text.txt", "r") as f:
    continut = f.read()

text_curat = "".join(char.lower() if char.isalnum() or char.isspace() else " " for char in continut)
cuvinte = text_curat.split()

frecventa ={}
for cuvant in cuvinte:
    frecventa[cuvant]= frecventa.get(cuvant,0)+1

#print(frecventa)

numarator = Counter(cuvinte)
top_5 = numarator.most_common(5)

for cuvant, numar in top_5:
        print(f"{cuvant}: {numar}")
