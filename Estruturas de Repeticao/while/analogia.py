# Número Total de Caixas no Caminhão: 5
caixas_no_caminhao = 5

print("Comecei a tirar as caixas do caminhão...")

# Enquanto houver caixas no caminhão, continue tirando
while caixas_no_caminhao > 0:
    print("Tirei uma caixa do caminhão.")
    print("Criança pergunta se podemos brincar.")
    print(
        f"Eu digo que não podemos brincar ainda, pois resta {caixas_no_caminhao} caixas")
    caixas_no_caminhao -= 1
    print("-=" * 20)

# Quando não houver mais caixas, saimos do loop e brincamos
print("Tirei todas as caixas do caminhão.")
print("Agora podemos brincar")
