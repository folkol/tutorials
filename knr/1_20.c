#include <stdio.h>

#define TAB_STOP 4

int main(void) {
    int c, l = 0;
    while (c = getchar(), c != EOF) {
        ++l;
        if (c == '\n') {
            l = 0;
        }

        if (c == '\t') {
            putchar(' ');
            while (l++ % TAB_STOP) {
                putchar(' ');
            }
            l = 0;
        } else {
            putchar(c);
        }
    }
    return 0;
}
