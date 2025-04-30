"""
Como você gosta de trabalhar com números, você se tornou Dr. Estranho e agora você é um super-herói que tem o poder de fazer cálculos matemáticos incríveis!
Você decidiu criar um programa que calcula a soma de todos os números inteiros de 1 a 100.
O programa deve exibir a soma total.

DESAFIO: caso que você queira complicar as coisas, tente mostrar o número de interações realizadas no loop FOR.

OUTPUT normal:
Soma total: 5050

OUTPUT com DESAFIO:
Soma total: 5050
Número de iterações: 100
"""
# Inicializa as variáveis
soma, interacoes = 0, 0

# Loop para calcular a soma de 1 a 100
for i in range(1, 101):
    soma += i
    interacoes += 1

print(f"Soma total: {soma}")
print(f"Número de iterações: {interacoes}")
