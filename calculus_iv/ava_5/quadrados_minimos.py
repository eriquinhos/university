# Construa uma função que receba como entrada dois vetores x, y ∈ R^m e um número n ∈ N, n < m, e retorne os
# coeficientes do polinômio de grau menor ou igual a n relativo ao ajuste de quadrados mínimos dos pares (xi , yi),
# i ∈ {0, · · · m}.

import numpy as np
from numpy import linalg


def quadrados_Minimos(x=np.zeros(2), y=np.zeros(2), n=1):
    """
    Dados x,y, dois vetores de tamanho m, essa função calcula a aproximação desses pontos a uma função pelo método dos
    Quadrados Mínimos por um polinônio aproximador de grau n

    :param x: Os valores de x dos pontos (x,y) de R^2 que devem ser aproximados pelo método dos Quadrados Mínimos
    :param y: Os valores de y dos pontos (x,y) de R^2 que devem ser aproximados pelo método dos Quadrados Mínimos
    :param n: O grau do polinômio aproximador
    :return: Coeficientes do polinômio aproximador pelo método dos Quadrados mínimos
    """
    # Em primeiro lugar, temos que x e y devem ser dois vetores. Portanto, caso seja fornecido pelo usuário apenas um
    # valor para cada ou uma lista/tupla de números, já serão convertidos para um vetor. Ademais, para realizarmos
    # nossas operações, é importante que nossos dados sejam do tipo float.

    x = np.array(x).astype('float')
    y = np.array(y).astype('float')

    # Para que (x,y) sejam um conjunto de pares ordenados, temos que o tamanho do vetor x e o vetor y devem ter o mesmo
    # tamanho
    if np.shape(x)[0] != np.shape(y)[0]:
        raise ValueError('os vetores x e y devem ser do mesmo tamanho.')

    # Além disso, para o nosso método de Quadrados Mínimos, precisamos dos nossos vetores gi(x), i ∈ {0, · · · n}. Para
    # isso, criamos um vetor H com n+1 linhas e  número de colunas igual ao número de pontos (x,y). Inicialmente ele
    # será formado apenas de zeros, sendo depois substituído por x^i, para cada gi(x);

    G = np.zeros((n+1, np.shape(x)[0]))
    for i in np.arange(n+1):
        for j in np.arange((np.shape(x)[0])):
            G[i, j] = pow(x[j], i)  # Aqui, podemos ver que cada elemento j da linha i será elevado a potência i. Como
            # em programação começamos com a linha 0, a primeira linha será formada totalmente por 1, pois todo número
            # será elevado a 0, a segunda linha será os próprios valores de x, a terceira será todos os elementos de x
            # elevalos ao quadrado e assim por diante.

    # O próximo passo é criar o sistema Ax = b e para isso temos que criar a matriz A, e a matriz b. Essa primeira é
    # formada pelos produtos internos de gi e gj: <gi, gj>, i,j  ∈ {0, · · · n}. Já a segunda, é formada pelos produtos
    # internos dos valores de y com gi:
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)
    for i in np.arange(n+1):
        b[i] = np.dot(y, G[i])
        for j in np.arange(n+1):
            A[i, j] = np.dot(G[i], G[j])

    # Possuindo os valores de A e b, podemos resolver o sistema linear em questão pela função solve() da biblioteca
    # linalg do NumPy. Desse modo, conseguimos o valor dos coeficientes do polinômio aproximador:

    alpha = linalg.solve(A, b)
    return alpha


x = np.array([-5, -3, -1, 0, 2, 4, 5])  # Valores de x da função tabela
y = np.array([25.1, 8.93, 0.98, 0.03, 3.96, 16.05, 25])  # Valores de y da função tabela

for n in range(1, 7):
    print(quadrados_Minimos(x, y, n))  # Chamando a função para os respectivos valores de x e y da função tabelada, e
    # grau de polinômio indo de 1 a 6



