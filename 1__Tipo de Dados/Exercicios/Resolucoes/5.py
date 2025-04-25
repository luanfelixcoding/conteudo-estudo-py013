"""
Peça ao usuário para digitar três números flutuantes. 
Calcule a média e exiba o resultado como um número inteiro.

OUTPUT:
5.6
6.9
8.0

média: 6
"""

n1 = float(input("Digite o numero 1: "))
n2 = float(input("Digite o numero 2: "))
n3 = float(input("Digite o numero 3: "))

media = (n1 + n2 + n3) / 3

print(int(media))
