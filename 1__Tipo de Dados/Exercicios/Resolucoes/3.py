"""
Crie uma variável com o valor "10" (como string).
Converta para inteiro, depois float, e exiba o tipo em cada conversão.

OUTPUT:
"10"
<class 'string'>
10
<class 'int'>
10.0
<class 'float'>
"""

# Criando a variavel
num = "10"

# Imprimindo na tela a variavel e o seu tipo
print(num)
print(type(num))

# Convertendo a variavel de string -> int
num = int(num)
print(num)
print(type(num))

# Convertendo a variavel de int -> float
num = float(num)
print(num)
print(type(num))
