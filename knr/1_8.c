#include <stdio.h>

int main(void) {
    int c, nw = 0;

    while (c = getchar(), c != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            ++nw;
        }
    }
    printf("%d\n", nw);
}
