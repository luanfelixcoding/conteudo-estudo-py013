"""
Você está juntando moedas em um cofrinho. 
A cada vez, o usuário digita o valor da moeda (ex: 0.50, 1.00). 
O programa deve somar até atingir ou passar de R$5,00 e então mostrar:
"Meta atingida: R$X no cofrinho!"

OBS: A meta atingida deve ser exibida com duas casas decimais.

OUTPUT:
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 0.50
Digite o valor da moeda (ex: 0.50): R$ 1.00
Digite o valor da moeda (ex: 0.50): R$ 1.00

Meta atingida: R$5.00 no cofrinho!
"""

# Inicializa as variáveis
total = 0.0
meta = 5.0

# Loop até atingir a meta
while total < meta:
    moeda = float(input("Digite o valor da moeda (ex: 0.50): R$ "))
    total += moeda

print(f"Meta atingida: R${total:.2f} no cofrinho!")
