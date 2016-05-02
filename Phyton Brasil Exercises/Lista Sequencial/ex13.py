altura=float(input("Entre com sua altura"))
sexo=input("ENTRE COM O SEXO M OU F")
sexo.upper()
if (sexo=='M'):
    pesoideal=(72.7*altura)-58
elif(sexo=='F'):
    pesoideal=(62.1*altura)-44.7

print (pesoideal)

peso=float(input("entre com seu peso"))

if peso>pesoideal:
    print("Você está acima do peso")
elif peso<pesoideal:
    print("você está abaixo do peso")