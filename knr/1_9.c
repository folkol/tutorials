#include <stdio.h>

int main(void) {
    int c, p = 0, nw = 0;

    while (c = getchar(), c != EOF) {
        if (p == ' ' && c == ' ')
            continue;
        putchar(c);
        p = c;
    }
}
