hora=int(input("entre com as horas trabalhadas"))
valorh=float(input("entre com o valor da hora"))
bruto=hora*valorh
inss=bruto*0.08
sindicato=bruto*0.05
imposto=bruto*0.11
liquido=(bruto-inss-sindicato-imposto)
print("Salario Bruto: %f \nSindicato: %f \nImposto:%f \nINSS:%f" %(bruto,sindicato,imposto,inss))
