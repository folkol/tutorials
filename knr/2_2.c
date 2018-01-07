

#include <stdio.h>

int main(int argc, char *argv[]) {
    int lim = 1024, s[lim], i, c;

    i = 0;
    while (1) {
        if (i < lim - 1) {
            if ((c = getchar()) != '\n') {
                if(c != EOF) {
                    s[i] = c;
                } else {
                    break;
                }
            } else {
                break;
            }
        }
        else {
            break;
        }
        ++i;
    }
}
