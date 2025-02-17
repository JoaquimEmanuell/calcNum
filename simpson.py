#Definição da função que vai ser integrada
def f(x):
    return 1 / (1+x**4)

#Definição do método
def metodo_simpson(f, a, b, n):
    #Verifica se o número de subintervalos é par
    if n % 2 != 0:
        raise ValueError("O número de subintervalos 'n' deve ser par")

    #Calcula o tamanho de cada subdivisão
    h = (b - a) / n
    x = a 
    integral = f(a) + f(b) #Adiciona os valores nos estremos

    #Loop para calcular a soma ponderada
    for i in range(1, n):
        x += h
        if i % 2 == 0: #Coeficiente 2 para os indices pares
            integral += 2 * f(x)
        else: #Coeficiente 4 para os indicies ímpares
            integral += 4 * f(x)
    
    #Multiplicação pelo fator h/3
    integral *= h / 3 
    return integral

a = 0 #Limite inferior
b = 2 #Limite superior
n = 4 #Número de subintervalos (deve ser par)

resultado = metodo_simpson(f, a, b, n)
print("Resultado: {}".format(resultado))