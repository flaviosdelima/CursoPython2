__author__ = 'Flavios'
import funcoes #primeira forma de fazer importação
from Objetos2 import Forma #segunda forma de fazer importação
from Objetos2 import Retangulo


temp = 212
convTemp = funcoes.ftoc(temp)#primeira forma de fazer importação
print(" O valor convertido é:"+str(convTemp))
temp = 0
convTemp = funcoes.ctof(temp)
print(" O valor convertido é:"+str(convTemp))


s1 = Forma(2,5)
print(s1)
