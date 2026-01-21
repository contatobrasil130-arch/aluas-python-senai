nome_aluno  = input("Digite o nome  do  aluno: ")
nota1 = int(input("digite o primeira nota: "))
nota2 = int(input("digite o segundo nota: "))
nota3 = int(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print (f"A soma das notas: {media}")

if media >= 7:
    print("O   aluno   esta aprovado")

elif media >= 4:
    print("O   aluno   esta em reculperação")

else:
    print("O ALUNO ESTA REPROVADO!")
