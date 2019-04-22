#include <stdio.h>

#define MAXLINE 80

int mygetline(char s[], int lim) {
    int i, c;
    for(i = 0; c = getchar(), c != EOF && i < lim - 1 && c != '\n'; i++) {
        s[i] = (char) c;
    }
    while(s[i - 1] == ' ' || s[i - 1] == '\n')
        i--;
    if(c == EOF && i == 0)
        return EOF;
    s[i] = '\0';
    return i;
}

int main(void) {
    int len;
    char line[MAXLINE + 1];

    while (len = mygetline(line, MAXLINE + 1), len != EOF) {
        fprintf(stderr, ">> %d %s'\n", len, line);
        printf("%s\n", line);
    }
    return 0;
}
