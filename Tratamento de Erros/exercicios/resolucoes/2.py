"""
Crie uma função divisao_segura(a, b) que realiza a divisão entre a e b. 
Se b for zero, capture o erro e exiba a mensagem "Não é possível dividir por zero".

OUTPUT:
5.0
Não é possível dividir por zero.
None
"""


def divisao_segura(a, b):
    try:
        # Tenta realizar a divisão normalmente
        return a / b
    except ZeroDivisionError:
        # Se o divisor for zero, exibe mensagem e evita crash
        print("Não é possível dividir por zero.")


print(divisao_segura(10, 2))  # 5.0
print(divisao_segura(10, 0))  # Exibe erro, mas não quebra
