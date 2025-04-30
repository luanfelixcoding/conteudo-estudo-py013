"""
Escreva um programa que, dado um número N, imprima uma escada de asteriscos com N degraus.
O número de degraus deve ser lido do usuário.

OUTPUT:
Digite o número de degraus: 4
*
**
***
****
"""

# Solicita ao usuário o número de degraus
n = int(input("Digite o número de degraus: "))

for i in range(1, n+1):
    # Imprime a escada de asteriscos
    print("*" * i)
