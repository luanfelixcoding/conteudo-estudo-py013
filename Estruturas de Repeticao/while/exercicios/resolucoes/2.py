"""
Você está em um ponto esperando o ônibus nº 517. 
Cada vez que passa um ônibus, você digita o número dele. 
Continue até que apareça o 517, então imprima:
"Ônibus 517 chegou! Embarcando..."

OUTPUT:
Qual o número do ônibus que passou? 123
Não é o ônibus certo...

Qual o número do ônibus que passou? 456
Não é o ônibus certo...

Qual o número do ônibus que passou? 517
Ônibus 517 chegou! Embarcando...
"""

# Inicializa a variável do ônibus
onibus = 0

# Loop até que o ônibus 517 chegue
# O loop continua enquanto o número do ônibus não for 517
while onibus != 517:
    onibus = int(input("\nQual o número do ônibus que passou? "))
    if onibus != 517:
        print("Não é o ônibus certo...")

print("Ônibus 517 chegou! Embarcando...")
