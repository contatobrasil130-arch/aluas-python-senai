valores = [7, 2, 9, 1, 5]
maior = None
menor = None

for i, num in enumerate(valores):
    if i == 0:  # 
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f"Maior: {maior}, Menor: {menor}")