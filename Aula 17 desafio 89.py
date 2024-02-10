infos = []
escolha = int(input("Quantos alunos você quer adicionar? "))
for x in range(0,escolha):
    nome = input(f"Digite o nome do {x+1}° aluno: ")
    nota1=(int(input(f"Digite a 1° nota do {nome}: ")))
    nota2=(int(input(f"Digite a 2° nota do {nome}: ")))
    notas = [nota1 , nota2]
    média = sum(notas) / 2
    infos.append([nome,notas,média])

print("No. Nome         Média")
print("-----------------------")
for y in range(0,escolha):
    print(f"{y} - {infos[y][0].ljust(14)} {infos[y][2]:.1f}")
print("-----------------------")
print(infos)
