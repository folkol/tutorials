#include <stdio.h>

#define TAB_STOP 4

int main(void) {
    int c, l = TAB_STOP;
    while (c = getchar(), c != EOF) {
        ++l;
        if (c == '\n') {
            l = 0;
        }

        if (c == '\t') {
            for (int i = 0; i < TAB_STOP - l % TAB_STOP; ++i) {
                putchar(' ');
            }
        } else {
            putchar(c);
        }
    }
    return 0;
}
