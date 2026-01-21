numero1 = float(input("escolha um número: "))
numero2 = float(input("escolha segundo número: "))
numero3 = float(input("escolha terceiro número: "))

if numero1 > numero2:
    maior = numero1

else:
    maior = numero2

if numero3 > maior:
    maior = numero3

print("O maior número é: ", maior)                
