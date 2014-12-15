__author__ = 'Flavios'
class Forma:
    def __init__(self,xcor,ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return ('x:'+str(self.x)+' y:'+str(self.y))

    def move(self,x1,y1):
        self.x = self.x + x1
        self.y = self.y + y1

class Retangulo(Forma):

    def __init__(self,xcor,ycor,altura,largura):
        Forma.__init__(self,xcor,ycor)
        self.altura = altura
        self.largura = largura

    def __str__(self):
        retstr = Forma.__str__(self)
        retstr =retstr+' largura='+str(self.largura)+' altura='+str(self.altura)
        return retstr

retan = Retangulo(5,10,8,9)
print(retan)
retan.move(5,9)
print(retan)
