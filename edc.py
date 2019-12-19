#Exercicio 1
#
#def implica(p,q):
#    if p == 0 and q == 0:
#        return 'Verdadeiro'
#    elif p == 0 and q == 1:
#        return 'Verdadeiro'
#    elif p == 1 and q == 0:
#        return 'Falso'
#    elif p == 1 and q == 1:
#        return 'Verdadeiro'
#
#p = int(input('Insira o valor lógico da variável p assumindo que Verdadeiro = 1 e Falso = 0: '))
#q = int(input('Insira o valor lógico da variável q assumindo que Verdadeiro = 1 e Falso = 0: '))
#print(implica(p,q))
#
##Exercicio 2
#
#def implica(p,q):
#    if p == 0 and q == 0:
#        return 'Verdadeiro'
#    elif p == 0 and q == 1:
#        return 'Verdadeiro'
#    elif p == 1 and q == 0:
#        return 'Falso'
#    elif p == 1 and q == 1:
#        return 'Verdadeiro'

#Exercicio 3a (Sem Recursividade)

def mdc1(x, y):
    while y is not 0:
        resto = x % y
        x = y
        y = resto
    return x

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: ')) 
print(mdc1(n1,n2))

#Exercicio 3b (Com recursividade)

def mdc2 (x,y): 
    if y == 0:
        return  x
    else:
        return  mdc2(y, x % y)

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
print (mdc2(n1, n2))

#Exercicio 4 

def fatores_primos(x):
    fatores_primos = []
    

