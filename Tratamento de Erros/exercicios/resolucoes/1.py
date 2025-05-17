"""
Crie uma função ler_numero() que pede ao usuário para digitar um número inteiro. 
Se o valor digitado não for um número válido, exiba uma mensagem de erro e retorne None.

Exemplo de entrada:
ler_numero(5)
ler_numero("abc")

OUTPUT:
5
Erro: Valor inválido. Digite um número inteiro.
Número lido: None
"""

# Criando funcao


def ler_numero():
    # Usando bloco try/except para detectar caso um erro aconteça
    try:
        # Pegando valor do usuario
        valor = int(input("Digite um número inteiro: "))
        return valor
    except ValueError:  # Bloco de detecção de erro(ValueError)
        print("Erro: Valor inválido. Digite um número inteiro.")
        return None


numero = ler_numero()
print("Número lido:", numero)
