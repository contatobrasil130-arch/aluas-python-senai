nome = input("Como você se chama: ")
peso= float(input("digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura * altura)

if imc <=  18.5:
    print("Cuidado com sua saúde")
elif imc <= 24.9:
    print="Abaixo do peso"  
elif imc <= 24.9:
    print="peso normal"
elif imc <=29.9:
    print="Sobre peso"
elif imc <= 34.9:
    print="obsidade gral II"
elif imc <=40.0:
    print="obsediade grau III"
