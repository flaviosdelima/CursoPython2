__author__ = 'Flavios'

beatles = ['Jhon','Paul','George','Ringo']
print(len(beatles))
print(beatles[0])
print(beatles[2:])
beatles.sort()
print(beatles)
beatles.reverse()
print(beatles)
beatles.append('Flavio')
print(beatles)
indece = beatles.index('Flavio')
print(indece)
del beatles[indece]
print(beatles)
print(beatles.pop())