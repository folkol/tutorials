#include <stdio.h>

int main(void) {
    int c, paren = 0, bracket = 0, brace = 0;

    while (c = getchar(), c != EOF) {
        switch (c) {
            case '(':
                ++paren;
                break;
            case ')':
                --paren;
                if (paren < 0) {
                    goto out;
                }
                break;
            case '[':
                ++bracket;
                break;
            case ']':
                --bracket;
                if (bracket < 0) {
                    goto out;
                }
                break;
            case '{':
                ++brace;
                break;
            case '}':
                --brace;
                if (brace < 0) {
                    goto out;
                }
                break;
        }
    }
    out:
    if (paren) {
        puts("unmatched paren");
    }
    if (bracket) {
        puts("unmatched bracket");
    }
    if (brace) {
        puts("unmatched brace");
    }
    return 0;
}
