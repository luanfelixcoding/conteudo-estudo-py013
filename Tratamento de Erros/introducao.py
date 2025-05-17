# Introdução ao Tratamento de Erros em Python (try/except/raise)

"""
Erros (ou exceções) são situações inesperadas que podem interromper a execução do programa.

Exemplos comuns:
- Divisão por zero
- Acesso a índice inexistente
- Conversão de tipos inválidos

Com o tratamento de erros, podemos **evitar que o programa pare** e lidar melhor com situações problemáticas.
"""

"""
Exemplo sem tratamento de erro (vai quebrar o programa)

numero = int("abc")  # ValueError
"""

# Iniciando com try/except
try:
    numero = int("abc")  # Tenta converter uma string inválida em inteiro
except ValueError:
    print("Erro: Não foi possível converter para número.")  # Mensagem amigável

print("Programa continua funcionando!\n")

# Capturando tipos diferentes de erros
try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
except IndexError:
    print("Erro: Índice fora da lista.")
except Exception as erro:
    print("Erro genérico:", erro)


# Usando else e finally
try:
    numero = int(input("Digite um número: "))
except ValueError:
    print("Erro: Entrada inválida.")
else:
    print(f"O número digitado foi {numero}.")  # Executa se não houve erro
finally:
    print("Fim do bloco try/except.\n")  # Sempre executa, com ou sem erro


# Usando raise para lançar erros
def dividir(a, b):
    if b == 0:
        # Lança um erro manualmente com uma mensagem personalizada
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b


try:
    resultado = dividir(10, 0)
except ZeroDivisionError as erro:
    print("Erro detectado:", erro)


# Criando exceções personalizadas (avançado, mas introdutivo)
class ErroIdadeInvalida(Exception):
    """Exceção personalizada para idades menores que zero."""
    pass


def definir_idade(idade):
    if idade < 0:
        raise ErroIdadeInvalida("Idade não pode ser negativa.")
    print(f"Idade registrada: {idade}")


try:
    definir_idade(-5)
except ErroIdadeInvalida as erro:
    print("Erro personalizado:", erro)

"""
Resumo:
- Use try/except para capturar erros e manter o programa rodando.
- Use else para executar algo se tudo deu certo.
- Use finally para executar algo sempre, mesmo com erro.
- Use raise para lançar seus próprios erros.
:)
"""
