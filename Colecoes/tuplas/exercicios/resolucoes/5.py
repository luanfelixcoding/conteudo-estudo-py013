"""
Dada uma tupla com 10 números:
- o primeiro número,

- os últimos dois números,

- e todos os números do meio.

Tupla de exemplo
valores = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

OUTPUT:
primeiro = 10
meio = (20, 30, 40, 50, 60, 70, 80)
ultimos = (90, 100)
"""

valores = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

primeiro, *meio, ultimos_1, ultimos_2 = valores

print(f"primeiro = {primeiro}")
print(f"meio = {tuple(meio)}")
print(f"ultimos = ({ultimos_1}, {ultimos_2})")

"""# Outra forma de fazer:
primeiro = valores[0]
meio = valores[1:8]
ultimos = valores[8:10]

print(f"primeiro = {primeiro}")
print(f"meio = {meio}")
print(f"ultimos = {ultimos}")"""
