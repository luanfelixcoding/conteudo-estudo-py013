"""
Em sua casa você tem maçãs e morangos. 
Você quer fazer um suco de frutas, mas para isso 
precisa saber se as frutas estão boas ou azedas.

Peça ao usuário para informar se a maçã e o morango estão boas ou azedas.

Caso ambas as frutas estejam boas, exiba a mensagem: "As frutas estão boas!".
Caso ambas as frutas estejam azedas, exiba a mensagem: "As frutas estão azedas!".
Caso apenas a maçã esteja azeda, exiba a mensagem: "Somente a maçã está azeda!".
Caso apenas o morango esteja azedo, exiba a mensagem: "Somente o melancia está azeda!".

OUTPUT:
Situacao da Maçã: boa
Situacao da Melancia: boa

As frutas estão boas!
"""

# Solicita ao usuário a situação da maçã e da melancia
maca = input("Situacao da Maçã: ").lower()
melancia = input("Situacao da Melancia: ").lower()

# Verificação das condições
if maca == "azeda" and melancia == "azeda":
    print("\nAs frutas estão azedas!")
elif melancia == "azeda" and maca == "boa":
    print("\nSomente o melancia está azedo!")
elif melancia == "boa" and maca == "azeda":
    print("\nSomente a maçã está azeda!")
else:
    print("\nAs frutas estão boas!")
