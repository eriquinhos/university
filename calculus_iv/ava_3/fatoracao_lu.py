# 1. Construa duas funções, com entrada uma matriz A, uma que calcule a fatoração LU de A sem
# pivoteamento e a outra com pivoteamento.
import numpy as np


def factlu_nopiv(a=np.ones(1)):  # Primeiramente, vamos fazer a função de fatoração LU sem pivoteamento
    """
    Essa função realizará a fatoração LU de uma matriz A qualquer, retornando duas matrizes: L (diagonal inferior) e
    U (diagonal superior), que se multiplicadas, retornam à matriz original
    :param a: Uma matriz A qualquer. Tem como valor padrão uma matriz quadrada de ordem 1, com a11 == 1;
    :return: Retorna as matrizes L e U, tal que L*U == A;
    """
    if not a.shape[0] == a.shape[1]:
        raise ValueError("A matriz inserida deve ser quadrada")  # Para a fatoração LU, a matriz inserida deve ser
        # quadrada, portanto, caso não for, a função retorna um erro

    u = np.copy(a)  # Para que facilitemos a visualização do que está acontecendo, podemos dizer que,
    # inicialmente, U é uma cópia da matriz A, definida pelo usuário.

    n = np.shape(u)[0]  # A variável n é definida como o primeiro valor da dimensão de U, ou seja, sendo U uma matriz
    # 3x3, np.shape(A) retornará uma tupla (3, 3), sendo que o primeiro valor se refere às linhas e o segundo às
    # colunas. Portanto, n é o número de linhas de A.

    l = np.eye(n, dtype="float64")  # A matriz L será uma matriz identidade de ordem n.

    for j in np.arange(n - 1):  # Aqui, para cada elemento j em uma matriz linha, que varia de 0 a n-2 (já que o último
        # valor nesta linguagem de programação é exclusive) teremos que:

        for i in np.arange(j + 1, n):  # Para cada elemento i pertencente à outras matrizes linhas que se formarão
            # variando de cada j+1 até n-1, o valor de L(i, j) será de:

            l[i, j] = u[i, j] / u[j, j]  # Note, que não se trata de uma divisão de matrizes, e sim de uma divisão entre
            # elementos da matriz U

            # Em verdade, o que está acontecendo nesse laço é que, como n tem o número de linhas de L e U e nós não
            # queremos zerar o último valor da matriz L(no caso L(n, n)), nem o último valor da matriz U
            # (no caso U(n, n)), pegamos j variando de 0 a n-2.
            # Depois, como j variará de 0 a n-2, com cada ciclo aumentando seu valor, portanto:
            # ciclo 1: j == 0; ciclo 2: j == 1; ...; ciclo n-1: j == n-2;
            # Agora, pegamos um valor i que variará de j+1 a n-1, o que fará com que no primeiro ciclo haja mais
            # operações (como esperado), uma vez que há mais valores debaixo de L(1, 1) que de L(2, 2)
            # Agora u[i,j] / u[j,j] é o valor do multiplicador para que os valores abaixo da diagonal principal de U se
            # anulem, e esses multiplicadores são inseridos debaixo diagonal principal de L, portanto L se tornará uma
            # matriz diagonal inferior, enquanto U se torna uma diagonal superior.

            for k in np.arange(j + 1, n):  # Agora, ainda dentro desse laço, a variável k varia no mesmo intervalo da
                # variável i, mas a cada ciclo deste laço serão realizadas diversas operações. Sendo L(i, j) um
                # multiplicador, temos que para zerar os valores abaixo da diagonal principal de U, cada U(i, k) deve
                # ser substituído pelo próprio valor subtraído do produto entre o multiplicador e U(j, k).

                u[i, k] = u[i, k] - l[i, j] * u[j, k]
            u[i, j] = 0
    return l, u


def factlu_piv(a=np.ones(1)):  # Agora podemos fazer uma função que calcule a fatoração LU com pivoteamento parcial
    """
    Essa função realizará a fatoração LU de uma matriz A qualquer, retornando duas matrizes: L (diagonal inferior) e
    U (diagonal superior), que se multiplicadas, retornam a matriz P multiplicada por A.
    :param a: Uma matriz A qualquer. Tem como valor padrão uma matriz quadrada de ordem 1, com a11 == 1;
    :return: Retorna as matrizes L, U e P, tal que L*U == P*A;

    """
    if not a.shape[0] == a.shape[1]:
        raise ValueError("A matriz inserida deve ser quadrada")  # Para a fatoração LU, a matriz inserida deve ser
        # quadrada, portanto, caso não for, a função retorna um erro
    u = np.copy(a)  # Para que facilitemos a visualização do que está acontecendo, podemos dizer que,
    # inicialmente, U é uma cópia da matriz A, definida pelo usuário.

    n = np.shape(u)[0]  # A variável n é definida como o primeiro valor da dimensão de U, ou seja, sendo U uma matriz
    # 3x3, np.shape(A) retornará uma tupla (3, 3), sendo que o primeiro valor se refere às linhas e o segundo às
    # colunas. Portanto, n é o número de linhas de A.

    l = np.eye(n, dtype="float64")  # A matriz L será uma matriz identidade de ordem n.

    p = np.arange(n)  # p é uma matriz linha tal que se refere ordem das linhas, as quais serão trocadas

    for j in np.arange(n-1):  # Para cada elemento em um array unidimensional que varia de 0 a n-2, temos que:

        pivo = u[j, j]  # Originalmente, o pivô é o elemento j, j da matriz U

        l_pivo = j  # A linha em que o pivô se encontra é j

        for k in np.arange(j+1, n):  # Nesse laço, percorremos uma array unidimensional de j+1 até n, para que
            # analisemos os números da mesma colna do pivô u[j, j], mas abaixo dele

            if abs(u[k, j]) > abs(pivo):  # Se o pivô da linha k e coluna j for maior em valor absoluto que o pivô
                # vigente o pivô se torna esse número

                pivo = u[k, j]
                l_pivo = k  # E, nesse caso, a linha em que o pivô se encontra passa a ser k

        if pivo == 0:  # Caso o pivô encontrado seja igual a 0, isso significa que a nossa matriz é não singular,
            # portanto o programa se encerrará com um erro

            raise ValueError("A matriz inserida é singular")

        elif l_pivo != j:  # Caso o pivô seja diferente do pivô original, definimos uma variável troca
            troca = p[j]  # Primeiramente, essa troca vai receber o elemento j de p
            p[j] = p[l_pivo]  # O elemento j de p recebe agora o número do real pivô
            p[l_pivo] = troca  # E o elemento do l_pivo recebe o valor da posição j

            # O que ocorreu nesse condicional foi que o elemento p[j] e p[l_pivo] trocaram de lugar, portanto, no
            # primeiro ciclo em que p == [1, 2, 3, ..., n], se l_pivô == 2, teremos que p == [3, 2, 1,..., n]

            for i in range(0, n):  # Agora, precisamos trocar os elementos na matriz U propriamente dita, por isso
                # criamos um laço que vai fzer o mesmo processo apresentado anteriormente, mas com cada um dos elementos
                # da matriz

                troca = u[j, i]
                u[j, i] = u[l_pivo, i]
                u[l_pivo, i] = troca

        for m in np.arange(j + 1, n):  # Para cada elemento i pertencente à outras matrizes linhas que se formarão
            # variando de cada j+1 até n-1, o valor de L(m, j) será de:

            l[m, j] = u[m, j] / u[j, j]  # Note, que não se trata de uma divisão de matrizes, e sim de uma divisão entre
            # elementos da matriz U
            for o in np.arange(j + 1, n):  # Agora, ainda dentro desse laço, a variável o varia no mesmo intervalo da
                # variável m, mas a cada ciclo deste laço serão realizadas diversas operações. Sendo L(m, j) um
                # multiplicador, temos que para zerar os valores abaixo da diagonal principal de U, cada U(m, o) deve
                # ser substituído pelo próprio valor subtraído do produto entre o multiplicador e U(j, o).

                u[m, o] = u[m, o] - (l[m, j] * u[j, o])
            u[m, j] = 0
    P = np.zeros((n, n))
    for b in range(0, n):
        P[b, p[b]] = 1
    return l, u, P


# Usando as funções do item anterior, construa uma função que calcula a inversa de uma matriz A.


def invmat(A):  # Vamos definir essa função para que possamos realizar a inversão de uma matriz por meio da fatoração LU
    # sem pivoteamento e vamos mostrar que por meio da fatoração LU é muito mais fácil realizar a inversão de uma matriz,
    # já que a resolução de vários sistemas lineares não escalonados pode se tornar bastante difícil quando se tem uma
    # matriz quadrada de ordem muito grande
    """
    Essa matriz calcula a inversa de uma função por meio da fatoração LU.
    :param A: matriz não-singular a ser invertida;
    :return: A**(-1), ou seja, a inversa de A.
    """
    if not A.shape[0] == A.shape[1]:
        raise ValueError("A matriz inserida deve ser quadrada")  # Para a fatoração LU, a matriz inserida deve ser
        # quadrada, portanto, caso não for, a função retorna um erro

    L = factlu_nopiv(A)[0]  # Por meio das nossas funções criadas anteriormente, podemos simplesmente utilizá-las para
    # que realizem a fatoração LU. O retorno dessa função se dá em uma tupla, em que o elemento 0 é a matriz L e o
    # elemento 1 é a matriz U

    U = factlu_nopiv(A)[1]
    n = np.shape(A)[0]
    I = np.identity(n)  # Como a multiplicação de uma matriz A com sua inversa resulta em uma matriz identidade,
    # vamos também precisar de uma matriz identidade de tamanho igual a de A
    A_inv = np.zeros(n)

    for i in range(0, n):  # Aqui, fazemos um laço que nos permite calcular pegar cada linha da matriz identidade para
        # calcularmos a solução
        Ii = np.array([I[0:n, i]], dtype='int32').transpose()  # Como esse método transforma as colunas em uma array com
        # uma linha apenas, temos que transpor para conseguirmos uma matriz coluna
        Yi = np.linalg.solve(U, Ii)  # Por meio da biblioteca numpy, podemos resolver esse sistema linear fácilmente por
        # meio da função solve(), portanto, Ii é tal que U*y = Ii

        Xi = np.linalg.solve(L, Yi)  # Desse resultado temos que o nosso resultado x, tal que L*x = y
        for j in range(0, n):
            A_inv[j, i] = Xi[0, i]  # E aqui compilamos os resultados, tendo no final a matriz inversa
    return A_inv


A = np.array([[2, 4, 2, 3], [-2, -5, -3, -2], [4, 7, 6, 8], [6, 10, 1, 2]])
B = np.array([[1, 2, -3, 4], [4, 8, 12, -8], [2, 3, 2, 1], [-3, -1, 1, -4]])

print(factlu_nopiv(A))
print(factlu_piv(B))
print(invmat(np.array([[-1, 2, 3], [2, -1, 1], [-1, 1, 1]])))