"""
Você foi contratado pela NASA para criar um contador regressivo para o lançamento de um foguete.

Peça ao usuário para informar o tempo em segundos que falta para o lançamento do foguete.
O programa deve exibir a contagem regressiva de 10 em 10 segundos,
até chegar a 0, e exibir a mensagem "Lançamento!".
O seu programa deve verificar se o tempo é maior que 0.
Caso contrário, exiba a mensagem "O tempo deve ser maior que 0!".

DESAFIO: Se quiser deixar mais realista, que tal usar uma funcao chamada time.sleep()?
A função time.sleep() faz o programa "dormir" por um determinado número de segundos.
Isso pode ser útil para simular a contagem regressiva.
No começo do seu código escreva: import time
Para usar a função, você deve escrever time.sleep(10) para fazer o programa esperar 10 segundos.

OUTPUT:
Digite o tempo em segundos: 30

30 segundos restantes
20 segundos restantes
10 segundos restantes
Lançamento!
"""
import time

# Solicita ao usuário o tempo em segundos
tempo = int(input("Digite o tempo em segundos: "))

if tempo >= 0:
    # Loop para a contagem regressiva
    for i in range(tempo, 0, -10):
        print(f"{i} segundos restantes")
        time.sleep(10)  # Espera 10 segundos entre as mensagens
    print("Lançamento!")
else:
    print("O tempo deve ser maior que 0!")
