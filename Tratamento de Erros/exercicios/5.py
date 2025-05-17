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
