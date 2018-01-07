#include <stdio.h>

#define MAXLINE 80

int main(void) {
    int c, p = 0;

    while (c = getchar(), c != EOF) {
        if (c == '"') {
            putchar(c);
            while (c = getchar(), c != EOF && !(c == '"' && p != '\\')) {
                putchar(c);
                p = c;
            }
            if (c == EOF)
                break;
        } else if (c == '\'') {
            putchar(c);
            while (c = getchar(), c != EOF && !(c == '\'' && p != '\\')) {
                putchar(c);
                p = c;
            }
            if (c == EOF)
                break;
        } else if (c == '/') {
            p = c;
            c = getchar();
            if (c == '/') {
                while (c = getchar(), c != EOF && c != '\n')
                    ;
            } else {
                putchar(p);
            }
        }
        putchar(c);
        p = c;
    }
    return 0;
}
