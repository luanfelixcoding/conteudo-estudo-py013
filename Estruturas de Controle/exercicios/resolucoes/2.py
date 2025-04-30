"""
Você é um professor e quer calcular a média de aluno
para saber se ele foi aprovado ou reprovado.

Peça ao usuário para digitar as notas do aluno.
Caso a media seja maior ou igual a 7, exiba a mensagem: "Aprovado!".
Caso a nota seja menor que 7, exiba a mensagem: "Reprovado!".

OBS: A média deve ser exibida com duas casas decimais.

OUTPUT:
Digite a nota 1 do aluno: 8
Digite a nota 2 do aluno: 6
Digite a nota 3 do aluno: 6

média: 6.67
Situação: Reprovado!
"""
# Solicita ao usuário as notas do aluno
nota_1 = float(input("Digite a nota 1 do aluno: "))
nota_2 = float(input("Digite a nota 2 do aluno: "))
nota_3 = float(input("Digite a nota 3 do aluno: "))

# Calcula a média
media = (nota_1 + nota_2 + nota_3) / 3

# Exibe a média
print(f"\nmédia: {media:.2f}")

# Verifica a situação do aluno
if media >= 7:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
