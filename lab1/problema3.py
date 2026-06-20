sample = ["a", 90, 8, "X55", "1z", 102, "asdf", 65, 10, "word", "567", 567]

auxiliar = sample[::-1]

print(auxiliar)

numere_doar = [x for x in sample if isinstance(x, int)]

print(numere_doar)

def generate_circulant_matrix(n):
    base = list(range(1, n + 1))
    
    matrix = [base[-i:] + base[:-i] for i in range(n)]
    
    return matrix

print(sample)


n=int(input("baga n pentru matrice"))
m=generate_circulant_matrix(n)

for row in m:
    print (row)
