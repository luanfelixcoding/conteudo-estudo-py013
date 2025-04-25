print("Bem-vindo ao provador de tipos de dados!")

# Definindo categorias (tipos de dados)
camisa = "camisa de manga longa"      # string
bermuda = "bermuda jeans"             # string
numero_de_tenis = 42                  # inteiro (int)
preco_do_chapeu = 39.99               # ponto flutuante (float)
tem_estilo = True                     # booleano (bool)

print("\nVamos conhecer algumas peças do seu look estiloso!")

# Mostrando os tipos de dados de cada "peça"
print(f"\n- Camisa: {camisa} - tipo: '{type(camisa)}'")
print(f"- Bermuda: {bermuda} - tipo: '{type(bermuda)}'")
print(f"- Tamanho do tênis: {numero_de_tenis} - tipo: '{type(numero_de_tenis)}'")
print(f"- Preço do chapéu: {preco_do_chapeu} - tipo: '{type(preco_do_chapeu)}'")
print(f"- Você tem estilo? {tem_estilo} - tipo: '{type(tem_estilo)}'")

print("\nConclusão: Cada peça tem seu lugar, assim como cada tipo de dado em Python!")
