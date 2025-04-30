"""
Peça ao usuário para digitar um número inteiro positivo N. 
Use um laço for para somar todos os números de 1 até N e mostre o resultado final.
OBS: Seu programa deve verificar se o número é positivo.
Caso o número seja negativo, exiba a mensagem: "Número inválido!".

OUTPUT:
Digite um número inteiro: 10
Soma dos números de 1 a 10: 55

Digite um número inteiro: -10
Número inválido!
"""

n = int(input("Digite um número inteiro: "))
soma = 0

if n > 0:
    for i in range(n + 1):
        soma += i
    print(f"Soma dos números de 1 a {n}: {soma}")
else:
    print("Número inválido!")
