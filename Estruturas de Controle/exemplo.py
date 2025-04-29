print("Bem-Vindo ao campo de batalha curandeiro!")
print("Seus aliados estão perdendo vida inclusive você!")
print("Decida quem deve receber o feitiço de cura!")

print("\nVocê tem 3 aliados e você: ")
print("1 - Aliado 1 possui 30/90 de hp")
print("2 - Aliado 2 possui 80/90 de hp")
print("3 - Aliado 3 possui 40/90 de hp")
print("4 - Você possui 50/90 de hp")

hp_aliado1 = 30
hp_aliado2 = 80
hp_aliado3 = 40

hp_curandeiro = 50
hp_maximo = 90
cura = 20

decisao = int(input("Escolha qual aliado deve ser curado: 1, 2, 3 ou 4: "))

if decisao == 1:
    hp_aliado1 += cura
    if hp_aliado1 > hp_maximo:
        hp_aliado1 = hp_maximo
    print(f"\nAliado 1 curado! HP atual: {hp_aliado1}/{hp_maximo}")

elif decisao == 2:
    hp_aliado2 += cura
    if hp_aliado2 > hp_maximo:
        hp_aliado2 = hp_maximo
    print(f"\nAliado 2 curado! HP atual: {hp_aliado2}/{hp_maximo}")

elif decisao == 3:
    hp_aliado3 += cura
    if hp_aliado3 > hp_maximo:
        hp_aliado3 = hp_maximo
    print(f"\nAliado 3 curado! HP atual: {hp_aliado3}/{hp_maximo}")

elif decisao == 4:
    hp_curandeiro += cura
    if hp_curandeiro > hp_maximo:
        hp_curandeiro = hp_maximo
    print(f"\nVocê se curou! HP atual: {hp_curandeiro}/{hp_maximo}")

else:
    print("\nNenhum aliado foi curado. Vocês perderam a batalha!")
