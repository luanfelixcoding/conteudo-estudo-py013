# Contagem simples de 1 a 5
print("Contagem de 1 a 5:")
i = 1
while i <= 5:
    print(i)
    i += 1

print("=" * 20)

# Validação de entrada
senha = ""
tentativas = 0

while senha != "python123":
    senha = input("Digite a senha: ")
    tentativas += 1
    if senha != "python123":
        print("Senha incorreta. Tente novamente.")
print(f"Acesso permitido após {tentativas} tentativas.")

print("=" * 20)

# Soma até que o usuário digite zero
print("Soma de números (digite 0 para encerrar):")
soma = 0
numero = None

while numero != 0:
    numero = int(input("Digite um número: "))
    soma += numero

print("Soma total:", soma)

print("=" * 20)

# Contagem regressiva com while
print("Contagem regressiva:")
contagem = 5

while contagem > 0:
    print(contagem)
    contagem -= 1
print("Fim da contagem!")

print("=" * 20)

# Menu interativo com while
opcao = None

while opcao != 0:
    print("\nMenu:")
    print("1 - Dizer Olá")
    print("2 - Mostrar um número aleatório")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\nOlá, usuário!")
    elif opcao == 2:
        import random
        print("\nNúmero aleatório:", random.randint(1, 100))
    elif opcao == 0:
        print("\nEncerrando o programa.")
    else:
        print("\nOpção inválida. Tente novamente.")
