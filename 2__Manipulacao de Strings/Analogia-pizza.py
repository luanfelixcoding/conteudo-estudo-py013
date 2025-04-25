print("Bem-Vindo a Pizzaria do Python!")
print("Hoje vamos saborear as pizzas de strings ...")

# Pizza Inteira (string completa)
pizza = "calabresa+mussarela+portuguesa"

"""
Index do fatiamento da string

c a l a b r e s a + m  u  s  s  a  r  e  l  a  +  p  o  r  t  u  g  u  e  s  a
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 
"""

print(f"\nPizza Completa: {pizza}")

print("\nVamos fatiar a PIZZA! Cada sabor tem o seu pedaço: ")

# Pegando pedaços (fatiando strings)
fatia_1 = pizza[0:9]     # calabresa
fatia_2 = pizza[10:19]   # mussarela
fatia_3 = pizza[20:30]   # portuguesa


print(f"Fatia 1 (posição 0 a 8): {fatia_1}")
print(f"Fatia 2 (posição 10 a 19): {fatia_2}")
print(f"Fatia 3 (posição 20 a 30): {fatia_3}")

# Pegar os últimos caracteres
print("\nSó quer um pedacinho? Que tal os últimos 6 caracteres da pizza:")
print(pizza[-6:])  # Exemplo de fatiamento negativo


# Juntando Sabores
print("\nVamos misturar sabores para criar uma nova pizza!")
pizza_mista = fatia_1 + "+" + fatia_3
print(f"Nova Pizza Mista: {pizza_mista}")


# Pegando um pedaço com mais fome
print("\nUma pessoa com fome pega 3 pedaços de uma vez:")
grande_fatia = pizza[0:30]
print(f"Grande Fatia: {grande_fatia}")

print("\nManipular strings é como saborear uma pizza — você escolhe os pedaços e pode até criar novos sabores!")
