print("Parte 1")
# Parte 1
for i in range(5):
    print(i, end=" ")

print("\n" + "="*20)
print("Parte 2")

# Parte 2
for i in range(5, -1, -1):
    print(i, end=" ")

print("\n" + "="*20)
print("Parte 3")

# Parte 3
for i in range(10):
    print(i)
    # Lembre do conteudo de Estrutura de Controle
    if i == 5:
        break
    print("Continuando o loop...")
print("Loop finalizado.")

print("="*20)
print("Parte 4")

# Parte 4
for i in range(0, 10, 2):
    print(i, end=" ")

print("\n" + "="*20)
print("Parte 5")

# Parte 5
# Lembre do conteudo de Manipulação de Strings
string = "Python"
for letra in string:
    print(letra, end="-")

print("\n" + "="*20)
print("Parte 6")

# Parte 6
# Lembre do conteudo de Manipulação de Strings
# OBS: Não se esqueca que o index começa em 6 - 1 = 5
# E vai até 0, no total são 6 letras
# Ou seja, o range vai de 5 até 0, e não de 6 até 0

for index in range(len(string)-1, -1, -1):
    print(string[index], end="")

print("\n" + "="*20)
