print("Você recebeu uma nova tarefa!")
print("Vamos verificar qual tarefa deverá ser feita primeiro!\n")

prazo_novo = input(
    "A tarefa atual tem prazo de entregue para amanha? (sim/nao): "
).lower()

prazo_anterior = input(
    "A tarefa anterior tem prazo de entregue para amanha? (sim/nao): "
).lower()

if prazo_novo == "sim" and prazo_anterior == "sim":
    print("\nAmbas as tarefas tem que ser feitas!")

elif prazo_anterior == "sim":
    print("\nFaça a tarefa anterior primeiro!")

elif prazo_novo == "sim":
    print("\nFaça a nova tarefa primeiro!")

else:
    print("\nVocê não tem tarefas com prazo para amanhã! Faça o que quiser!")
