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
    elif n == 1:
        a += 1 + (((x ** (n - 1))/fatorial(n-1)) * (x/n))
    else:
        a = 1  # Como divisão por zero é impossível, tivemos que adaptar o programa para que o primeiro termo do
                # polinômio com n = 0 aparecesse.
        for i in range(1, n+1):
            a += ((x ** (i - 1))/(fatorial(i - 1)))*(x/i)
    return a


print(taylor(2, 1))
print(taylor(2, 2))
print(taylor(2, 5))
print(taylor(2, 10))
print(taylor(2, 100))
print(taylor(2, 200))
print(taylor(2, 500))
print(taylor(2, 1000))
print(taylor(2, 2000))
print(taylor(2, 5000))