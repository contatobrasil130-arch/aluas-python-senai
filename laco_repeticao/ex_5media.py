
soma = 0
contador = 0
while True:
    entrada = input("Digite a nota (ou Enter para sair- - 1): ")
    if entrada == "": # Condição de parada: entrada vazia
        break
    soma += float(entrada)
    contador += 1

if contador > 0:
    print(f"A média é: {soma / contador}")