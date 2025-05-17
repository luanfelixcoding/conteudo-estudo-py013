"""
Crie uma função chamada calculadora() que:

- Peça ao usuário dois números e uma operação (+, -, *, /).
- Tente realizar a operação.
- Caso o usuário digite um valor inválido (ex: texto ao invés de número), capture o erro.
- Caso tente dividir por zero, capture também.
- Ao final, mostre sempre a mensagem "Operação registrada no histórico." (use finally).
- Retorne o resultado se for possível, ou None caso ocorra erro.

OUTPUT:
Digite o primeiro número: 3
Digite o segundo número: 2
Digite a operação (+, -, *, /): +
Operação registrada no histórico.
Resultado: 5.0

OUTPUT (com erro):
Digite o primeiro número: 9
Digite o segundo número: 0
Digite a operação (+, -, *, /): /
Erro: Não é possível dividir por zero.
Operação registrada no histórico
"""


def calculadora():
    try:
        # Recebe os números e operação do usuário
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        # Verifica qual operação será realizada
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                raise ZeroDivisionError("Não é possível dividir por zero.")
            return a / b
        else:
            print("Operação inválida.")
            return None

    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Erro: Você digitou um valor não numérico.")
        return None

    except ZeroDivisionError as erro:
        # Tratamento da divisão por zero
        print("Erro:", erro)
        return None

    finally:
        # Executado sempre, com ou sem erro
        print("Operação registrada no histórico.")


resultado = calculadora()
if resultado is not None:
    print(f"Resultado: {resultado}")
