"""
Crie uma função cadastrar_idade(idade) que lança um ValueError com a 
mensagem "Idade não pode ser negativa" se o valor for menor que zero. 
Capture esse erro no bloco try/except.

Exemplo de entrada:
cadastrar_idade(25) 
cadastrar_idade(-3)   

OUTPUT:
Idade cadastrada com sucesso: 25
Erro: Idade não pode ser negativa.
"""


def cadastrar_idade(idade):
    try:
        # Verifica se a idade é negativa
        if idade < 0:
            # Lança um erro manualmente se for inválida
            raise ValueError("Idade não pode ser negativa.")

        # Caso a idade seja válida
        print(f"Idade cadastrada com sucesso: {idade}")

    except ValueError as erro:
        # Captura o erro lançado e exibe a mensagem personalizada
        print("Erro:", erro)


cadastrar_idade(25)   # Válida
cadastrar_idade(-3)   # Inválida
