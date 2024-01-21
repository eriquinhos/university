#include <stdio.h>
#include <stdlib.h>

typedef int *TVetor;

TVetor mergeSort(TVetor, int, int);
TVetor merge(TVetor, int, int, int);
int contaParesSomas(TVetor, int, int, int);


int main(){
    int S, N, i;
    int soma = 0;
    TVetor V;

    scanf("%d", &S);

    V = (int *) malloc(S * sizeof(int));

    scanf("%d", &N);

    for(i = 0; i < S; i++){
        scanf("%d", &V[i]);
    }

    V = mergeSort(V, 0, S - 1);

    soma = contaParesSomas(V, 0, S - 1, N);

    printf("%d", soma);

    return 0;
}


TVetor mergeSort(TVetor V, int inicio, int fim){
    int meio;

    if(inicio < fim){
        meio = (inicio + fim) / 2;

        mergeSort(V, inicio, meio);
        mergeSort(V, meio + 1, fim);
        merge(V, inicio, meio, fim);
    }

    return V;
}

TVetor merge(TVetor V, int inicio, int meio, int fim){
    int i, j, k;
    int *Vaux;

    Vaux = (int *) malloc((fim - inicio + 1) * sizeof(int));

    i = inicio;
    j = meio + 1;
    k = 0;

    while(i <= meio && j <= fim){
        if(V[i] <= V[j]){
            Vaux[k] = V[i];
            i++;
        }else{
            Vaux[k] = V[j];
            j++;
        }

        k++;
    }

    while(i <= meio){
        Vaux[k] = V[i];
        i++;
        k++;
    }

    while(j <= fim){
        Vaux[k] = V[j];
        j++;
        k++;
    }

    for(i = inicio; i <= fim; i++){
        V[i] = Vaux[i - inicio];
    }

    free(Vaux);

    return V;
}

int contaParesSomas(TVetor V, int inicio, int fim, int soma){
    int i, j, cont = 0;

    i = inicio;
    j = fim;

    while(i < j){
        if(V[i] + V[j] == soma){
            cont++;
            i++;
            j--;
        }else if(V[i] + V[j] < soma){
            i++;
        }else{
            j--;
        }
    }

    return cont;
}