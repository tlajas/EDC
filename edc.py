##Exercicio 1
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

#---------------------------------------------------------------------------------------------------------------------------#

##Exercicio 2 (Nota: tv = tabela de verdade)
#
#tv_s = [1, 1, 1, 1, 0, 0, 0, 0]
#tv_t = [1, 1, 0, 0, 1, 1, 0, 0]
#tv_u = [1, 0, 1, 0, 1, 0, 1, 0]
#
##Criação da tabela de verdade não_s
#
#def nao_s():
#    tv_nao_s = []
#    for x in range(0, 8):
#        if tv_s[x] == 1:
#            tv_nao_s.append(0)
#        elif tv_s[x] == 0:
#            tv_nao_s.append(1)
#    return tv_nao_s
#nao_s()
#
##Criação da tabela de verdade s_implica_t
#
#def s_implica_t():
#    tv_s_implica_t = []
#    for n in range(0, 8):
#        if (tv_s[n] == 0 and tv_t[n] == 0) or (tv_s[n] == 0 and tv_t[n] == 1) or (tv_s[n] == 1 and tv_t[n] == 1):
#            tv_s_implica_t.append(1)
#        elif tv_s[n] == 1 and tv_t[n] == 0:
#            tv_s_implica_t.append(0)
#s_implica_t()
#
#
##Criação da tabela de verdade de u_ou_t
#
#def u_ou_t():
#    tv_u_ou_t = []
#    for y in range(0, 8):
#        if (tv_u[y] == 0 and tv_t[y] == 0):
#            tv_u_ou_t.append(0)
#        elif (tv_u[y] == 0 and tv_t[y] == 1) or (tv_u[y] == 1 and tv_t[y] == 0) or (tv_u[y] == 1 and tv_t[y] == 1):
#            tv_u_ou_t.append(1) 
#    return tv_u_ou_t
#u_ou_t()
#
##Criação da tabela de verdade de (u_ou_t)_ou_(não_s)
#
#def uout_ou_ns(tv_u_ou_t, tv_nao_s):
#    tv_uout_ou_ns = []
#    for f in range(0, 8):
#        if (tv_u_ou_t[f] == 0 and tv_nao_s[f] == 0):
#            tv_uout_ou_ns.append(0)
#        elif (tv_u_ou_t[f] == 0 and tv_nao_s[f] == 1) or (tv_u_ou_t[f] == 1 and tv_nao_s[f] == 0) or (tv_u_ou_t[f] == 1 and tv_nao_s[f] == 1):
#            tv_uout_ou_ns.append(1)
#uout_ou_ns(u_ou_t(), nao_s())

#---------------------------------------------------------------------------------------------------------------------------#

##Exercicio 3a (Sem Recursividade)
#
#def mdc1(x, y):
#    while y is not 0:
#        resto = x % y
#        x = y
#        y = resto
#    return x
#
#n1 = int(input('Insira o primeiro número: '))
#n2 = int(input('Insira o segundo número: ')) 
#print(mdc1(n1,n2))
#
##Exercicio 3b (Com recursividade)
#
#def mdc2 (x,y): 
#    if y == 0:
#        return  x
#    else:
#        return  mdc2(y, x % y)
#
#n1 = int(input('Insira o primeiro número: '))
#n2 = int(input('Insira o segundo número: '))
#print (mdc2(n1, n2))

#---------------------------------------------------------------------------------------------------------------------------#

##Exercicio 4 
#
#def forPrimo(x):
#    for divisor in range(2, x):
#        if x%divisor == 0:
#            return False
#    else: 
#        return True
#
#def fatorizacao(x):
#    FatoresPrimos = []
#    divisor = 2
#    while x > 1:
#        if forPrimo(divisor):
#            if x % divisor == 0:
#                x = x / divisor
#                FatoresPrimos.append(divisor)
#            else:
#                divisor += 1
#        else:
#            divisor += 1
#    return FatoresPrimos
    

