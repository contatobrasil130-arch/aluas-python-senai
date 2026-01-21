nome_aluno  = input("Digite o nome  do  aluno: ")
nota1 = int(input("digite o primeira nota: "))
nota2 = int(input("digite o segundo nota: "))

media = (nota1 + nota2 + ) / 2
print (f"A soma das notas: {media}")

if media >= 7:
    print("O   aluno   esta aprovado")

if media <= 7:
    print("O   aluno   esta reprovado")
elif media >= 10:
    print("aprovado com distinção")

else:
    print("O ALUNO ESTA REPROVADO!")
