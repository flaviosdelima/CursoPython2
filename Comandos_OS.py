__author__ = 'Flavios'
import os
os.system('cls') #Comando cls do command do DOS
os.system('dir')

numbers = [1,2,3,4,5]

#Listas / Arrays
for i in numbers:
    print(i)

#Dicionarios
valores = {'Bobs':'333','Bober':'111','Boba':'222'}
print(valores['Bober'])
print(list(valores.keys()))
print(list(valores.values()))
for valor in valores.keys():
    print(valor+' - '+valores[valor] )
print(valores.get('Bober'))

numer = 12
denom = 2
if denom!=0:
    print(numer/denom)
else:
    print('Divisão por Zero!')


grade = 85

if grade>=90:
    letterGrade = 'A'
elif grade >=80:
    letterGrade = 'B'
else:
    letterGrade = 'F'
print(letterGrade)



