"""
Uma estação meteorológica coleta temperaturas diárias. 
Você quer identificar apenas os dias com 
temperaturas anormais (acima de 35°C ou abaixo de 5°C)

# Desafio: use filter e lambda para encontrar somente as temperaturas anormais
# (acima de 35 ou abaixo de 5)

Lista de temperaturas:
temperaturas = [22, 4, 37, 19, 5, 42, 3]

OUTPUT:
[4, 37, 42, 3]
"""

# Lista de temperaturas
temperaturas = [22, 4, 37, 19, 5, 42, 3]

# Usando filter e lambda para encontrar temperaturas anormais
temperaturas_anormai = list(filter(lambda t: t > 35 or t < 5, temperaturas))
print(temperaturas_anormai)  # [4, 37, 42, 3]
