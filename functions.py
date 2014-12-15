__author__ = 'Flavios'

def quadrado(num):
    return num*num

def convertTemp(temp,scale):
    if scale=="c":
        return(temp -32.0)*(5.0/9.0)
    elif scale=="f":
        return temp * 9.0/5.0 +32

def onePerLine(str):
    for i in str:
        print(i)

temps = int(input("Digite a temperatura:"))
scales = input("Digite a escala de destino:")
print("A Temperatura convertida é:",convertTemp(temps,scales))

print (quadrado(4))


