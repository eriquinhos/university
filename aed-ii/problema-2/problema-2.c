#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAMANHO 1000000

typedef struct cliente {
    int valor;
    int senha;
} TCliente;

typedef struct demanda {
    TCliente cliente;
    int numDemandas;
} TDemanda;

typedef TDemanda *PDemanda;

PDemanda maxHeapify(PDemanda, int, int);

int main() {
    int senha = 1;
    int valor;
    char operacao;

    PDemanda demandas = (PDemanda)malloc(sizeof(TDemanda) * TAMANHO);
    demandas->numDemandas = 0;

    while (1) {
        scanf(" %c", &operacao);

        if (operacao == 'c') {
            scanf("%d", &valor);
            demandas->cliente.valor = valor;
            demandas->cliente.senha = senha;
            demandas->numDemandas++;
            senha++;

            demandas = maxHeapify(demandas, 0, demandas->numDemandas);
        } else if (operacao == 'v') {
            if (demandas->numDemandas <= 0) {
                printf("0\n");
            } else {
                printf("%d\n", demandas->cliente.senha);
                demandas->numDemandas--;
                demandas->cliente = demandas[demandas->numDemandas].cliente;
                demandas = maxHeapify(demandas, 0, demandas->numDemandas);
            }
        } else if (operacao == 'f') {
            free(demandas);
            break;
        }
    }

    return 0;
}

PDemanda maxHeapify(PDemanda demandas, int i, int tam) {
    int esq = 2 * i + 1;
    int dir = 2 * i + 2;
    int maior = i;

    if (esq < tam && demandas[esq].cliente.valor > demandas[maior].cliente.valor) {
        maior = esq;
    }

    if (dir < tam && demandas[dir].cliente.valor > demandas[maior].cliente.valor) {
        maior = dir;
    }

    if (maior != i) {
        TDemanda aux = demandas[i];
        demandas[i] = demandas[maior];
        demandas[maior] = aux;
        maxHeapify(demandas, maior, tam);
    }

    return demandas;
}
