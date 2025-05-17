# Introdução a Módulos em Python

"""

Módulos em Python são arquivos que contêm código Python (funções, variáveis, classes, etc.)
e que podem ser **importados** e reutilizados em outros arquivos.

Eles ajudam a:
- Organizar melhor o código
- Reutilizar funções
- Dividir responsabilidades em arquivos separados
"""

# Importando um módulo padrão do Python
import datetime as dt
from math import pi, ceil
import math  # Módulo da biblioteca padrão para operações matemáticas

raiz = math.sqrt(25)  # sqrt = square root = raiz quadrada
print("Raiz quadrada de 25:", raiz)


# Importando apenas partes de um módulo
print("Valor de pi:", pi)
print("Ceil de 4.2:", ceil(4.2))  # Arredonda para cima


# Renomeando um módulo (alias)
data_atual = dt.datetime.now()
print("Data e hora atual:", data_atual)


# Criando e usando seu próprio módulo
"""
Imagine que temos um arquivo chamado utilidades.py com este conteúdo:

# utilidades.py
def saudacao(nome):
    return f"Olá, {nome}!"

def dobro(n):
    return n * 2
"""

# Para usar essas funções em outro arquivo:
# import utilidades

# print(utilidades.saudacao("Maria"))
# print(utilidades.dobro(10))

"""
📁 Estrutura de pasta:
meu_projeto/
│
├── main.py          <-- Aqui você importa e usa
└── utilidades.py    <-- Aqui estão as funções que você criou
"""

# Usando módulos externos (instalados com pip)

"""
Alguns módulos não vêm com o Python e precisam ser instalados usando o pip.
Exemplo: requests (faz requisições HTTP)

Terminal:
pip install requests

Uso:
import requests
resposta = requests.get("https://api.github.com")
print(resposta.status_code)
"""

# Verificando os módulos disponíveis

help("modules")  # Mostra uma lista de todos os módulos instalados

"""
Resumo:
- Módulo = qualquer arquivo .py que pode ser importado
- Use módulos para organizar e reutilizar seu código
- Você pode importar módulos do Python, seus próprios, ou externos
- Evite códigos gigantes em um único arquivo — divida com módulos!
"""
