"""
Peça ao usuário digitar um número e o programa
deve mostrar na tela se o número é par ou ímpar.
Caso o número seja par, exiba a mensagem: "O número é par!".
Caso o número seja ímpar, exiba a mensagem: "O número é ímpar!".

OUTPUT:
Digite um número: 5
O número é ímpar!

Digite um número: 4
O número é par!
"""

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número é par!")
else:
    print("O número é ímpar!")
