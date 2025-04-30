"""
Você precisa dar 10.000 passos por dia. 
A cada entrada, o usuário informa quantos passos deu. 
Continue somando até chegar ou ultrapassar 10.000 e então exiba:
"Parabéns! Meta de passos atingida com X passos."

OUTPUT:
Quantos passos você deu agora? 5000
Quantos passos você deu agora? 3000
Quantos passos você deu agora? 2000

Parabéns! Meta de passos atingida com 10000 passos.
"""

# Inicializa as variáveis
total_passos = 0
meta = 10000

# Loop até atingir a meta
while total_passos < meta:
    passos = int(input("Quantos passos você deu agora? "))
    total_passos += passos

print(f"Parabéns! Meta de passos atingida com {total_passos} passos.")
