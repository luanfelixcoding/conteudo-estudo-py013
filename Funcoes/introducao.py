# Introdução às Funções em Python

"""
Funções são blocos de código reutilizáveis que executam uma tarefa específica.

Elas ajudam a:
- Evitar repetição de código
- Organizar melhor o programa
- Dividir um problema grande em partes menores
"""

# Criando uma função simples


def saudacao():
    print("Olá, seja bem-vindo(a)!")


# Chamando a função
saudacao()  # Olá, seja bem-vindo(a)!


# Função com parâmetros (entrada de dados)
def apresentar(nome):
    print(f"Olá, {nome}!")


apresentar("Lucas")  # Olá, Lucas!


# Função com mais de um parâmetro
def soma(a, b):
    resultado = a + b
    print(f"Soma: {resultado}")


soma(5, 3)  # Soma: 8


# Função que retorna um valor com return
def quadrado(numero):
    return numero ** 2


res = quadrado(4)
print(f"Quadrado: {res}")  # Quadrado: 16


# Parâmetros opcionais (valores padrão)
def boas_vindas(nome="visitante"):
    print(f"Bem-vindo, {nome}!")


boas_vindas()         # Bem-vindo, visitante!
boas_vindas("Ana")    # Bem-vindo, Ana!


# Argumentos nomeados (palavra-chave)
def exibir_dados(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")


exibir_dados(idade=30, nome="Carlos")  # Nome: Carlos, Idade: 30


# Funções com número variável de argumentos (*args)
def somar_todos(*numeros):
    return sum(numeros)


print(somar_todos(1, 2, 3, 4, 5))  # Saída: 15


# Funções com argumentos nomeados variáveis (**kwargs)
def mostrar_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


mostrar_info(nome="Joana", idade=25, cidade="Recife")
# nome: Joana
# idade: 25
# cidade: Recife


# Funções aninhadas (definidas dentro de outras)
def calcular():
    def dobrar(x):
        return x * 2
    return dobrar(10)


print(calcular())  # 20


# Função como parâmetro de outra função
def aplicar(funcao, valor):
    return funcao(valor)


def triplo(n):
    return n * 3


print(aplicar(triplo, 4))  # 12


# Função lambda (função anônima)
def dobro(x): return x * 2


print(dobro(6))  # 12


# Escopo de variáveis (local vs global)
mensagem = "Olá"


def alterar():
    global mensagem  # Torna possível modificar a variável global
    mensagem = "Oi"


alterar()
print(mensagem)  # Saída: Oi


# Documentação de função (docstring)
def exemplo(a, b):
    """
    Retorna a soma de dois números.
    Parâmetros:
      - a: número 1
      - b: número 2
    Retorna:
      - soma de a + b
    """
    return a + b


print(exemplo(2, 3))  # Saída: 5
print(exemplo.__doc__)  # Exibe a documentação da função
