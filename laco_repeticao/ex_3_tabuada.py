##3) Tabuada Leia um número inteiro n e imprima sua tabuada de 1 a 10

numero = int(input("Digite o número que deseja calculado: "))
i =10

for multiplicador in range(numero + 1):
    print(f"{numero} X {multiplicador} = {numero*multiplicador}")

