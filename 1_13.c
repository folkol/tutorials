#include <stdio.h>

#define OUT 0
#define IN  1
#define BINS 10
#define GUTTER 4

int main(void) {
    int c, l = 0, state = OUT;
    int hist[BINS] = {0};

    while (c = getchar(), c != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (state == IN) {
                if (l < 10)
                    ++hist[l];
                putchar('\n');
            }
            state = OUT;
        } else {
            if (state == OUT) {
                l = 0;
            }
            ++l;
            state = IN;
            putchar(c);
        }
    }
    int max = 0;
    for (int i = 0; i < BINS; ++i) {
        if (hist[i] > max)
            max = hist[i];
    }
    for (int i = max; i >= 0; --i) {
        printf("%3d|", i);
        for (int j = 0; j < BINS; ++j) {
            if (hist[j] >= i)
                putchar('*');
            else
                putchar(' ');
        }
        putchar('\n');
    }
    printf("   +");
    for (int j = GUTTER; j < BINS + GUTTER; ++j) {
        putchar('-');
    }
    putchar('\n');
}
