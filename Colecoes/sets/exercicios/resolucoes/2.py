"""
Dadas duas frases, encontre as palavras em comum entre elas:
frase_1 = "Python é uma linguagem poderosa e fácil de aprender"
frase_2 = "Aprender Python é divertido e poderoso"

DICA: use .split() para separar as palavras

OUTPUT: 
{'python', 'aprender', 'e', 'é'}
"""

frase_1 = "Python é uma linguagem poderosa e fácil de aprender"
frase_2 = "Aprender Python é divertido e poderoso"

# Converte as frases em sets de palavras
palavras_1 = set(frase_1.lower().split())
palavras_2 = set(frase_2.lower().split())

# Encontra as palavras em comum
palavras_comum = palavras_1.intersection(palavras_2)
print(palavras_comum)

# Outra forma de fazer:
# palavras_comum = palavras_1 & palavras_2
# print(palavras_comum)
