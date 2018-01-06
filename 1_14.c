#include <stdio.h>

#define OUT 0
#define IN  1
#define GUTTER 4

int main(void) {
    int c, nc = 0, state = OUT;
    int hist['z' - 'a'] = {0};

    while (c = getchar(), c != EOF) {
        if (c >= 'a' && c <= 'z') {
            ++nc;
            ++hist[c - 'a'];
        }
    }
    for (int i = 0; i < 'z' - 'a'; ++i) {
        hist[i] = hist[i] * 100 / nc;
    }
    int max = 0;
    for (int i = 0; i < 'z' - 'a'; ++i) {
        if (hist[i] > max)
            max = hist[i];
    }
    for (int i = max; i >= 0; --i) {
        printf("%3d|", i);
        for (int j = 0; j < 'z' - 'a'; ++j) {
            if (hist[j] >= i)
                putchar('*');
            else
                putchar(' ');
        }
        putchar('\n');
    }
    printf("   +");
    for (int j = GUTTER; j < 'z' - 'a' + GUTTER; ++j) {
        putchar('-');
    }
    putchar('\n');
    printf("    ");
    for (int j = 'a'; j < 'z'; ++j) {
        putchar(j);
    }
    putchar('\n');
}
