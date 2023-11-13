# Considere f(x) = sqrt(x ** 2 +1) - 1
# Provado que f(x) = (x ** 2)/(sqrt(x ** 2 + 1) + 1) faça um programa que, dado x, verifica se f(x) > 0, usando as duas
# formulações de f

from math import sqrt
import itertools


def isnumber(string):
    '''
    Essa função deve ser usada no lugar da função primária do Python "isnumeric()", uma vez que esta não considera
    valores do tipo 'float' como numéricos.

    :param string: O usuário deve inserir um valor do tipo string, para que a função tente converte-lo para um float
    type
    :return: CAso o valor inserido seja um número do tipo int ou float, a função retorna True. Caso não seja de nenhum
    dos dois tipo, a função retorna False.
    '''
    try:
        float(string)
        return True
    except ValueError:
        return False


def f(x):  # Primeiramente definimos uma função f(x) que calculará a função f para algum x dado pelo usuário
    """
    Verifica se para um x, determinado pelo usuário,  0 < f(x) = sqrt(x ** 2 +1) - 1
    :param x: Valor de x na função
    :return: Verdadeiro se f(x) > 0 e Falso se f(x) <= 0
    """
    x = str(x)  # Primeiro transformamos esse x em uma variável do tipo string para uma verificação prévia
    if not isnumber(x):  # Caso o x não seja um número, um erro será levantado e explicado ao usuário
        raise ValueError('x precisa ser um valor numérico.')
    else:  # Caso x seja um número, ele será convertido a um número de ponto flutuante
       x = float(x)
    f = sqrt(x ** 2 + 1) - 1  # Realizaremos então as duas operações de f
    g = (x ** 2)/(sqrt(x ** 2 + 1) + 1)
    if f > 0 and g > 0:  # Como ambas são iguais, caso ambas sejam positivas, retornará que a sentença de que f(x) > 0 é
        # verdadeira

        return True

    else:  # Caso não, retornará falso
        return False


def g(x):
    """
    Essa função calcula o valor de g(x) = sqrt(x ** 2 + 1) - 1, ou seja, a primeira forma de f(x) na atividade proposta

    :param x: Um valor numérico qualquer a ser inserido pelo usuário
    :return: O valor de g(x)
    """
    x = str(x)  # Primeiramente, transformamos o valor digitado em uma string
    if not isnumber(x):  # Caso esse valor não seja numérico, ocorrerá um erro no programa
        raise ValueError('O valor digitado deve ser numérico')
    else:  # Caso contrário o número será convertido para o tipo float e a operação será realizada
        x = float(x)
    f = sqrt(x ** 2 + 1) - 1
    return f  # Retornado o valor de g(x) ao final


def h(x):
    """
    Essa função calcula o valor de h(x) = (x ** 2) / (sqrt(x ** 2 + 1) + 1), ou seja, a segunda forma de f(x) na
    atividade proposta

    :param x: Um valor numérico qualquer a ser inserido pelo usuário
    :return: O valor de h(x)
    """
    x = str(x)  # Primeiramente, transformamos o valor digitado em uma string
    if not isnumber(x):  # Caso esse valor não seja numérico, ocorrerá um erro no programa
        raise ValueError('O valor digitado deve ser numérico')
    else:  # Caso contrário o número será convertido para o tipo float e a operação será realizada
        x = float(x)
    f = (x ** 2) / (sqrt(x ** 2 + 1) + 1)
    return f  # Retornado o valor de h(x) ao final


# Testando a função f(x):

for i in itertools.count(-(10 ** -10), step=10 ** -11):
    if i < 10 ** -10:
        print(f'x = {float(i):.2}, f(x) = {f(i)}')

# Podemos observar aqui que o programa só retorna valores Falsos, uma vez que uma das formas de f(x) não possui precisão
# suficiente, considerando números da ordem de 10 ** -8 como já muito próximos de zero. Nesse caso, podemos descobrir
# quando cada forma da função passa a considerar que f(x) = 0, fazendo com que, partindo de x = 1, essa operação seja
# realizada a cada loop, dividindo x por 2 a cada loop e parando quando f(x) = 0:

x = 1

while True:
    if g(x) > 0:
        x = x/2
    else:
        print(x)
        break

x = 1

while True:
    if h(x) > 0:
        x = x/2
    else:
        print(x)
        break

# Observamos então que a segunda forma de f(x) apresenta uma maior precisão, fazendo com que apenas considera f(x) = 0,
# quando x é da ordem de 10 ** -162
