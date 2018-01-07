#include <stdio.h>

#define MAXLINE 80

int mygetline(char s[], int lim) {
    int c, i;
    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i) {
        s[i] = (char) c;
    }
    if (c == '\n') {
        s[i] = (char) c;
        ++i;
    }
    s[i] = '\0';
    return i;
}

int main(void) {
    int len;
    char line[MAXLINE + 1];

    while (len = mygetline(line, MAXLINE + 1), len > 0) {
        printf("%s", line);
        if (line[len - 1] != '\n') {
            putchar('\n');
        }
    }
    return 0;
}
