from math import e


def fatorial(num=1):
    """
    Esta função calcula o fatorial de um número
    :param num: Deve ser digitado um número inteiro maior ou igual a zero.
    :return: Retorna o fatorial do número.
    """
    fat = 1
    if num == 0:
        fat = 1
    elif num < 0 or type(num) == float:
        return ValueError
    else:
        while num > 0:
            fat *= num
            num -= 1
    return fat


def taylor(x=0, n=0):
    """
    Essa é uma função que calcula uma aproximação de e^x pela fórmula de Taylor
    :param x: Número ao qual x está elevado
    :param n: Número de parcelas no polinômio de Taylor. Quanto maior esse número, mais precisa deve ser a aproximação
    :return: Retorna a aproximação da função pela fórmula de Taylor
    """
    a = 0
    if n == 0:
        a += (x ** n)/fatorial(n)
    else:
        for i in range(0, n+1):
            a += (x ** i)/(fatorial(i))
    return a


print(f'A aproximação de e = {taylor(2,1)} e o erro é de {(e ** 2) - taylor(2,1)}')
print(f'A aproximação de e = {taylor(2,2)} e o erro é de {(e ** 2) - taylor(2,2)}')
print(f'A aproximação de e = {taylor(2,5)} e o erro é de {(e ** 2) - taylor(2,5)}')
print(f'A aproximação de e = {taylor(2,10)} e o erro é de {(e ** 2) - taylor(2,10)}')
print(f'A aproximação de e = {taylor(2,100)} e o erro é de {(e ** 2) - taylor(2,100)}')
print(f'A aproximação de e = {taylor(2,200)} e o erro é de {(e ** 2) - taylor(2,200)}')
print(f'A aproximação de e = {taylor(2,500)} e o erro é de {(e ** 2) - taylor(2,500)}')
print(f'A aproximação de e = {taylor(2,1000)} e o erro é de {(e ** 2) - taylor(2,1000)}')
print(f'A aproximação de e = {taylor(2,2000)} e o erro é de {(e ** 2) - taylor(2,2000)}')
print(f'A aproximação de e = {taylor(2,5000)} e o erro é de {(e ** 2) - taylor(2,5000)}')
