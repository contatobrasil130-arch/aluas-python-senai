##4) Soma acumulada Leia números inteiros até o usuário digitar 0. Ao final, mostre a soma.

acumula = 0
numero = int(input("Digite um numero inteiro: "))


while numero != 0:   
    acumula += numero
    numero = int(input("Digite um numero inteiro (0 - Sair): "))
    
print(acumula)




