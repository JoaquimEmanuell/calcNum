from math import *

#Define a função a ser integrada
def f(x):
    return 1 / (1+x**4)

def metodo_simpson(f, a, b):
    #Calcula o tamanho de cada subdivisão
    h = (b - a) / 2

    #Inicializa x com o valor mínimo da integral
    x = a

    #Calcula o valor da integral
    integral = f(a) + f(a+h) + f(b)
    integral *= (h/3)

    return integral

a = 0
b = 2

resultado = metodo_simpson(f, a, b)
print("O resultado é: {}".format(resultado))
