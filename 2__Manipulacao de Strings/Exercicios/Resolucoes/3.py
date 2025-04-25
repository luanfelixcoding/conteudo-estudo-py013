"""
Dado o nome do usuário, imprima ele de trás para frente.

OUTPUT: 
Ligeirinho
ohniriegiL
"""

# Pegando nome do usuario
nome: str = input("Digite o seu nome: ")

# Mostrando o seu nome ao contrario
print(f"Seu nome ao contrario é: {nome[::-1]}")
