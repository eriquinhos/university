#include <stdlib.h>
#include <stdio.h>
#include <math.h>

typedef struct ponto {
    double x, y;
} TPonto;

typedef TPonto* PPonto;

double calcula_distancia_ao_quadrado(TPonto, TPonto);
double calcula_distancia_real(TPonto, TPonto);
void mergeSort(PPonto, int, int, char);
void merge(PPonto, int, int, int, char);
double calcula_menor_distancia(PPonto, PPonto, int, int);

int main() {
    int N, i;
    double menor_distancia;
    PPonto coordenadas, vetor_temporario;

    scanf("%d", &N);

    coordenadas = (PPonto)malloc(N * sizeof(TPonto));
    vetor_temporario = (PPonto)malloc(N * sizeof(TPonto));

    for (i = 0; i < N; i++) {
        scanf("%lf %lf", &coordenadas[i].x, &coordenadas[i].y);
    }

    mergeSort(coordenadas, 0, N - 1, 'x');

    menor_distancia = sqrt(calcula_menor_distancia(coordenadas, vetor_temporario, 0, N));

    printf("%.10f\n", menor_distancia);

    free(coordenadas);
    free(vetor_temporario);
    return 0;
}

double calcula_distancia_ao_quadrado(TPonto p, TPonto q) {
    return (q.x - p.x) * (q.x - p.x) + (q.y - p.y) * (q.y - p.y);
}

double calcula_distancia_real(TPonto p, TPonto q) {
    return sqrt((q.x - p.x) * (q.x - p.x) + (q.y - p.y) * (q.y - p.y));
}

void mergeSort(PPonto coordenadas, int inicio, int fim, char eixo) {
    if (inicio < fim) {
        int meio = (inicio + fim) / 2;
        mergeSort(coordenadas, inicio, meio, eixo);
        mergeSort(coordenadas, meio + 1, fim, eixo);
        merge(coordenadas, inicio, meio, fim, eixo);
    }
}

void merge(PPonto coordenadas, int inicio, int meio, int fim, char eixo) {
    int i, j, k;
    int n1 = meio - inicio + 1;
    int n2 = fim - meio;

    PPonto L = (PPonto)malloc(n1 * sizeof(TPonto));
    PPonto R = (PPonto)malloc(n2 * sizeof(TPonto));

    for (i = 0; i < n1; i++) {
        L[i] = coordenadas[inicio + i];
    }
    for (j = 0; j < n2; j++) {
        R[j] = coordenadas[meio + 1 + j];
    }

    i = 0;
    j = 0;
    k = inicio;

    while (i < n1 && j < n2) {
        if ((eixo == 'x' && L[i].x <= R[j].x) || (eixo == 'y' && L[i].y <= R[j].y)) {
            coordenadas[k++] = L[i++];
        } else {
            coordenadas[k++] = R[j++];
        }
    }

    while (i < n1) {
        coordenadas[k++] = L[i++];
    }
    while (j < n2) {
        coordenadas[k++] = R[j++];
    }

    free(L);
    free(R);
}

double calcula_menor_distancia(PPonto coordenadas, PPonto vetor_temporario, int inicio, int fim) {
    if (fim - inicio <= 1) {
        return INFINITY;
    }

    if (fim - inicio == 2) {
        return calcula_distancia_ao_quadrado(coordenadas[inicio], coordenadas[inicio + 1]);
    }

    int meio = (inicio + fim) / 2;
    double d1 = calcula_menor_distancia(coordenadas, vetor_temporario, inicio, meio);
    double d2 = calcula_menor_distancia(coordenadas, vetor_temporario, meio, fim);
    double menor_distancia = fmin(d1, d2);

    int j = 0;
    for (int i = inicio; i < fim; i++) {
        if (fabs(coordenadas[i].x - coordenadas[meio].x) < sqrt(menor_distancia)) {
            vetor_temporario[j++] = coordenadas[i];
        }
    }

    mergeSort(vetor_temporario, 0, j - 1, 'y');

    for (int i = 0; i < j; i++) {
        for (int k = i + 1; k < j && (vetor_temporario[k].y - vetor_temporario[i].y) < sqrt(menor_distancia); k++) {
            double d = calcula_distancia_ao_quadrado(vetor_temporario[i], vetor_temporario[k]);
            menor_distancia = fmin(menor_distancia, d);
        }
    }

    return menor_distancia;
}
