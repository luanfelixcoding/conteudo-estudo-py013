"""
Crie um menu de operações matemáticas (soma, subtração, multiplicação e divisão).

O usuário deve escolher a operação desejada e informar os dois números inteiros.
O programa deve realizar a operação escolhida e exibir o resultado.
Caso não há a opção escolhida mostre uma mensagem de erro para o usuário.

OUTPUT:

Escolha a operação desejada:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
Digite o número 1: 10
Digite o número 2: 5
Resultado da soma: 15
"""

# Criação do Menu
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Solicita ao usuário a operação desejada
operacao = int(input("Escolha a operação desejada (1/2/3/4): "))

# Solicita ao usuário os números
n1 = int(input("Digite o número 1: "))
n2 = int(input("Digite o número 2: "))

# Realiza a operação escolhida
if operacao == 1:
    resultado = n1 + n2
    print(f"Resultado da soma: {resultado}")

elif operacao == 2:
    resultado = n1 - n2
    print(f"Resultado da subtração: {resultado}")

elif operacao == 3:
    resultado = n1 * n2
    print(f"Resultado da multiplicação: {resultado}")

elif operacao == 4:
    if n2 != 0:
        resultado = n1 / n2
        print(f"Resultado da divisão: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Operação inválida. Por favor, escolha uma operação válida.")
