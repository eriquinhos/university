# Considere A uma matriz quadrada de dimensão n, que só possui elementos não nulos nas entradas: a(i, 1), a(i, i),
# a(i, i + 1), a(n, 1), a(n, n), para todo i ∈ {1, 2, · · · , n − 1}. Construa uma função que resolva um sistema Ax = b
# pelo método de Jacobo que aproveite a estrutura de A e receba como parâmetros de entrada A, b, o ponto inicial, a
# tolerância máxima exigida e um número máximo de iterações.


from __future__ import division
import numpy as np
from numpy import linalg
from numpy.linalg import LinAlgError


def jacobi(A, b, x0, tol, N):
    """
    Resolve um sistema linear pelo método iterativo de Gauss-Jacobi, considerando que A seja uma matriz quadrada de
    dimensão n, que só possui elementos não nulos nas entradas: a(i, 1), a(i, i), a(i, i + 1), a(n, 1), a(n, n), para
    todo i ∈ {1, 2, · · · , n − 1}.

    :param A: Uma matriz quadrada de ordem n,cujas entradas são especificadas acima
    :param b: A matriz de coeficientes do sistema linear
    :param x0: Ponto inicial de iteração, deve ser uma lista cujo tamanho é igual ao número de variáveis
    :param tol: Máximo de erro que o programa pode cometer na resolução desse sistema
    :param N: Número máximo de iterações
    :return: A solução do sistema linear
    """
    # Em primeiro lugar, devemos tentar converter a variável A inserida pelo usuário em uma matriz
    A = np.array(A)

    # Agora, temos que conferir se a matriz A tem os requisitos necessários pré-estabelecidos: Em primeiro lugar, a
    # matriz deve ser quadrada

    if np.shape(A)[0] != np.shape(A)[1]:
        raise LinAlgError('A matriz não é quadrada!')

    # Caso o primeiro requisito seja cumprido, devemos analisar se A só possui elementos não nulos nas entradas:
    # a(i, 1), a(i, i), a(i, i + 1), a(n, 1), a(n, n), para todo i ∈ {1, 2, · · · , n − 1}.
    else:
        for i in range(0, A.shape[0] - 1):
            for j in A[i, 0]:
                if j == 0:
                    raise ValueError('Os elementos da primeira coluna devem ser não-nulos.')
            for k in A[i, i]:
                if k == 0:
                    raise ValueError('Os elementos da diagonal principal devem ser não-nulos.')
            for l in A[i, i+1]:
                if l == 0:
                    raise ValueError('Os elementos imediatamente acima da diagonal principal devem ser não-nulos.')
        for m in A[A.shape[0], 0]:
            if m == 0:
                raise ValueError('Os elementos da primeira coluna devem ser não-nulos.')
        for c in A[A.shape[0], A.shape[0]]:
            if c == 0:
                raise ValueError('O elemento a(n, n) deve ser não nulo')

    # Agora, teremos que fazer com que o tipo de dado dentro da nossa matriz seja "float", uma vez que precisamos
    # realizar algumas iterações com essa matriz

    A = A.astype('double')
    b = b.astype('double')
    x0 = x0.astype('double')

    n = np.shape(A)[0]  # Esse número se refera ao tamanho da matriz, previamente definida como quadrada

    x = np.zeros(n)  # x é um vetor unidimensional de tamanho n cujas entradas são todas nulas

    it = 0  # Estamos atualmente na iteração 0, uma vez que não começamos o processo de Jacobi

    # Começaremos então definindo que, enquanto o número de iterações for menor que aquele pré-estabelecido pelo
    # usuário, o programa continuará fazendo o processo de Jacobi
    while it < N:
        it += 1  # A iteração atual será a anterior + 1

        for i in np.arange(n):  # Para cada elemento i em um vetor de tamanho n, sendo A uma matriz nxn

            x[i] = b[i]  # O elemento i do vetor x, primeiramente recebe o elemento i do vetor b (matriz dos termos
            # independentes)
            
            for j in np.concatenate((np.arange(0, i), np.arange(i+1, n))):
                x[i] -= A[i, j]*x0[j]
            x[i] /= A[i, i]
        #  tolerancia
        if np.linalg.norm(x-x0, np.inf) < tol:
            return x
        #  prepara nova iteracao
        x0 = np.copy(x)
    raise NameError('num. max. de iteracoes excedido.')

A = np.zeros((3,2))
print(A.astype('double'))