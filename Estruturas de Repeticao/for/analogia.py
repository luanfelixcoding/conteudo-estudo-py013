print("Olá estagiário novato!")
print("Tenho uma tarefa para você!")
print("Você terá que carimbar alguns documentos da empresa que lhe pedirei!")
print("Boa sorte!")

quantidade_documentos = int(
    input("Quantos documentos tenho que carimbar? "))

for carimbada in range(quantidade_documentos):
    print(f"\nCarimbando documento número {carimbada + 1}")
    print("Documento carimbado com sucesso!")
    print(f"Você já carimbou {carimbada + 1} documentos!")
    print(f"Faltam {quantidade_documentos - (carimbada + 1)} documentos!")
    print("="*20)
