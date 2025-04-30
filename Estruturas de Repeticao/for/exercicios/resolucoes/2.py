"""
Faça um programa que imprima somente 
os números pares entre 1 e 20 usando for.

OUTPUT:
Numeros pares entre 1 e 20:
2 4 6 8 10 12 14 16 18 20
"""

# Forma 1 de resolver
print("Numeros pares entre 1 e 20:")
for i in range(2, 21, 2):
    print(i, end=" ")

print("\n")

# Forma 2 de resolver
print("Numeros pares entre 1 e 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")

print()
