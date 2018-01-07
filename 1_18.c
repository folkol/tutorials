#include <stdio.h>

#define MAXLINE 80

int mygetline(char line[], int maxline);

void copy(char to[], char from[]);


int main(void) {
    int len, c;
    char line[MAXLINE + 1];

    while (len = mygetline(line, MAXLINE + 1), len > 0) {
        while (c = line[len - 1], len >= 0 && (c == ' ' || c == '\t' || c == '\n')) {
            line[len - 1] = '\n';
            line[len] = '\0';
            len--;
        }
        if (len > 0) {
            printf("%s", line);
        }
    }
    return 0;
}

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

void copy(char to[], char from[]) {
    int i = 0;
    while (to[i] = from[i], to[i] != '\0') {
        ++i;
    }
}
