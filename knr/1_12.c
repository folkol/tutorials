#include <stdio.h>

#define OUT 0
#define IN  1

int main(void) {
    int c, state = OUT;

    while (c = getchar(), c != EOF) {
        if (c == ' ' || c == '\t' || c == '\n') {
            if (state == IN) {
                putchar('\n');
            }
            state = OUT;
        } else {
            state = IN;
            putchar(c);
        }
    }
}
