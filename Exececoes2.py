__author__ = 'Flavios'

try:
    number = int(input("Digite um numero:"))
    print(number)

    aFile = open('aqasdf.py')
    print(aFile.readline())
except ValueError:
    print('Não foi digitado um numero tente novamente:')
    number = int(input("Digite um numero:"))

except IOError:
    print('Não foi possivel abrir o arquivo!')

print('Final!!')