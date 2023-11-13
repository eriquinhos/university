# Construa uma função que receba como entrada dois números reais a < b, um valor n ∈ N, o número de intervalos no
# processo numérico, e uma função f(x) e retorne uma aproximação da integral de f(x) entre a e b usando a regra de
# trapézios repetidos.

import math
from itertools import count


def trapeziosRepetida(a, b, n=1, f=lambda x: x):
    """
    Calcula uma aproximação da integral de f, calculada entre a e b, pelo Método dos Trapézios Repetida
    :param a: Limite inferior da integral definida
    :param b: Limite superior da integral definida
    :param n: Número de intervalos no processo numérico
    :param f: Função matemática em x
    :return: Aproximação da integral de f, calculada entre a e b
    """
    # Primeiramente temos que definir que a < b, então caso seja o contrário, podemos realizar a troca desses valores

    troca = 0
    trocou = False

    if a > b:  # Portanto, definindo uma variável de troca, temos que, pelo método de cascata, troca vai receber o valor
        # de a, a trocará de valor e passará a ser b e b receberá o antigo valor de a:

        troca = a
        a = b
        b = troca
        trocou = True

    # Como houve a inversão dos limites superior e inferior, temos que indicar que essa troca foi feita pela variável
    # trocou, que no final será usada para que, caso seja verdadeira, sabendo que a integral de a até b, com a < b, é o
    # oposto da integral de b até a, possamos trocar o sinal do resultado aproximado da integral.

    elif a == b:  # Agora, caso a seja igual a b, o programa levantará um erro, indicando que esses números não podem ser
        # iguais
        raise ValueError('o valor de a deve ser diferente do valor de b.')

    h = (b - a)/n  # a altura h de cada trapézio para calcular a área é dado por esta fórmula

    # Os valores de x em que a f deve ser calculada são valores i, entre a e b, igualmente espaçados. Dessa forma, a
    # variável fun, é dada por uma lista dos valores de f calculada em i
    fun = []
    for i in count(a, step=h):
        fun.append(round(f(float(i)), 10))
        if round(i, 10)+h > b:
            break

    qx = 0  # Primeiramente, definimos q(x) = f(x0) + 2f(x1) + 2f(x2) + ... + f(xn) = 0

    for j in range(0, len(fun)):  # Agora, vamos somar os valores de f(xi), i ∈ {0, 1, ..., n}, fazendo com que os
        # números nas extremidades sejam somados apenas uma vez e ou outros, duas vezes
        if j == 0 or j == n:
            qx += fun[j]
        else:
            qx += 2 * fun[j]

    integral = (h * qx)/2  # A aproximação da integral é dada por essa fórmula:

    if not trocou:
        return integral
    else:
        return -integral


a = 1
b = 5
f1 = (lambda x1: 3*x1 + 5)
f2 = (lambda x2: 7*(x2**2) + 3*x2 + 5)
f3 = (lambda x3: -8*(x3**3) + 7*(x3**2) + 3*x3 + 5)
f4 = (lambda x4: (x4 ** 4) - 8*(x4**3) + 7*(x4**2) + 3*x4 + 5)
f5 = (lambda x5: 2*(x5 ** 5) + (x5 ** 4) - 8*(x5**3) + 7*(x5**2) + 3*x5 + 5)
f6 = (lambda x6: 2*math.cos(x6) + 4*math.sin(2*x6) + 7)
n = [2, 4, 10, 20, 50]

for v in n:
    print(f'\033[1;31m{trapeziosRepetida(a, b, v, f1)}')
    print(f'\033[1;32m{trapeziosRepetida(a, b, v, f2)}')
    print(f'\033[1;33m{trapeziosRepetida(a, b, v, f3)}')
    print(f'\033[1;34m{trapeziosRepetida(a, b, v, f4)}')
    print(f'\033[1;35m{trapeziosRepetida(a, b, v, f5)}')
    print(f'\033[1;36m{trapeziosRepetida(a, b, v, f6)}')
    print()