#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        if (i % 2 == 1) printf(" ");
        for (int j = 0; j < n - 1; j++) printf("* ");
        printf("*\n");
    }
    return 0;
}