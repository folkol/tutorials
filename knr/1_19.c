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

void copy(char to[], char from[]) {
    int i = 0;
    while (to[i] = from[i], to[i] != '\0') {
        ++i;
    }
}

void reverse(char s[], int len) {
    len -= 1;
    for (int i = 0; i <= len / 2; ++i) {
//        printf("%d %d\n", i, len - 1 - i);
        int tmp = s[i];
        s[i] = s[len - i];
        s[len - i] = (char) tmp;
    }
}


int main(void) {
    int len;
    char line[MAXLINE + 1];

    while (len = mygetline(line, MAXLINE + 1), len > 0) {
        if (line[len - 1] == '\n') {
            --len;
        }
        reverse(line, len);
        printf("%s", line);
    }
    return 0;
}
