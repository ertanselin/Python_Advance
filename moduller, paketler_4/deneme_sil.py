"""Bu program deneme amacıyla modül olarak 
kadedimiştir. Fonk. kullanımı   """

def __dir__():
	return ['faktoriyel','topla']

def faktoriyel(x):
    f = 1
    for i in range(2,x+1):
        f = f*i
    return f 

def topla(x,y):
	return x+y