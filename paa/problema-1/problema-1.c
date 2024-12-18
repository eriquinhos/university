#include <stdio.h>
#include <stdint.h>

uint64_t sumOnesOnInterval(uint64_t N) {
    uint64_t count = 0;
    uint64_t fator = 1;

    while (fator <= N) {
        uint64_t blocosCompletos = (N / (fator * 2)) * fator;
        uint64_t resto = N % (fator * 2);
        uint64_t maisUm = resto >= fator ? resto - fator + 1 : 0;

        count += blocosCompletos + maisUm;
        fator *= 2;
    }

    return count;
}

int main() {
    uint64_t X, Y, somaAcumulada;

    scanf("%llu %llu", &X, &Y);
    
    if (X == 0) {
        somaAcumulada = sumOnesOnInterval(Y);
    } else {
        somaAcumulada = sumOnesOnInterval(Y) - sumOnesOnInterval(X - 1);
    }

    printf("%llu\n", somaAcumulada);

    return 0;
}
