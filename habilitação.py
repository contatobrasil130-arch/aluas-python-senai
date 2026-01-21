nome = input ("qual é o seu nome?")
idade = int(input("qual a sua idade?"))
possui_carteira = input("Possui cartira de motorisra?\n(1-sim / 2-não)")

if idade >= 18:

    if possui_carteira == "1":
        print("Pode dirigir: ")
    else:
        print ("Não pode dirigir: ")

else:
    print ("menor de idade.")
    
