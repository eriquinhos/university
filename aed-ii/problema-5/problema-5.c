#include <stdlib.h>
#include <stdio.h>
#include <string.h>
 
typedef struct rnam{
    char codon[4];
    char proteina;
} RNAm;
 
int comparaCodon(const void*, const void*);
 
int buscaBinaria(RNAm*, char*, int);
 
 
int main() {
    int N, M, i, j, posicao;
    RNAm rnam, *dicionario;
    char sequencia[10000], codon[4];
 
    scanf("%d", &N);
 
    dicionario = (RNAm *) malloc(N * sizeof(RNAm));
 
    getchar();
 
    for (i = 0; i < N; i++) {
        scanf("%s", &rnam.codon);
 
        getchar();
 
        scanf("%c", &rnam.proteina);
 
        dicionario[i] = rnam;
    }
 
    qsort(dicionario, N, sizeof(RNAm), comparaCodon);
 
    scanf("%d", &M);
 
    for(i=0; i<M; i++){
        if(i!=0){
            printf("\n");
        }
        memset(sequencia, 0, sizeof(sequencia));
 
        scanf("%s", &sequencia);
 
        for(j=0; j<strlen(sequencia); j+=3){
            memset(codon, 0, sizeof(codon));
 
            codon[0] = sequencia[j];
            codon[1] = sequencia[j+1];
            codon[2] = sequencia[j+2];
 
            posicao = buscaBinaria(dicionario, codon, N);
 
            if(posicao != -1){
                printf("%c", dicionario[posicao].proteina);
            }else{
                printf("*");
            }
        }
 
    }
 
 
    return 0;
}
 
 
int comparaCodon(const void *codon1, const void *codon2) {
    return strcmp(((const RNAm *)codon1)->codon, ((const RNAm *)codon2)->codon);
}
 
int buscaBinaria(RNAm *sequencia, char *codon, int N){
    int inicio = 0, fim = N - 1, meio;
 
    while (inicio <= fim) {
        meio = (inicio + fim) / 2;
 
        if (strcmp(codon, sequencia[meio].codon) == 0) {
            return meio;
        } else if (strcmp(codon, sequencia[meio].codon) < 0) {
            fim = meio - 1;
        } else {
            inicio = meio + 1;
        }
    }
 
    return -1;
}