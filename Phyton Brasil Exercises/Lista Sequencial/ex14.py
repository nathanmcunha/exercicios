peso=float(input("entre com o peso dos peixes em kg "))

if(peso<50):
    print("Não excedeu o peso")
else:
    excecido=peso-50
    multa=excecido*4.0
print("valor da multa é",multa)    