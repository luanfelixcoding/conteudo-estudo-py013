"""
Você é um professor de matemática e está ensinando tipos de triângulos para a sua turma, 
e para aula ficar mais dinâmica você resolve criar um programa que verifica se os lados de um triângulo formam um triângulo válido.

Peça ao usuário para digitar o comprimento dos três lados de um triângulo. O programa deve verificar se os lados formam um triângulo válido e, em caso afirmativo, informar o tipo:

    Equilátero: todos os lados iguais

    Isósceles: dois lados iguais

    Escaleno: todos os lados diferentes

Se os lados não puderem formar um triângulo válido, o programa deve informar isso.

OUTPUT:
Digite o comprimento do lado 1: 3
Digite o comprimento do lado 2: 4
Digite o comprimento do lado 3: 5

O triângulo é escaleno.
"""

# Solicita ao usuário o comprimento dos lados do triângulo
l1 = float(input("Digite o comprimento do lado 1: "))
l2 = float(input("Digite o comprimento do lado 2: "))
l3 = float(input("Digite o comprimento do lado 3: "))

# Verifica se os lados formam um triângulo válido
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    # Verifica o tipo de triângulo
    if l1 == l2 == l3:
        print("\nO triângulo é equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("\nO triângulo é isósceles.")
    else:
        print("\nO triângulo é escaleno.")
else:
    print("Os lados informados não formam um triângulo válido.")
