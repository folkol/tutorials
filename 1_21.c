#include <stdio.h>

#define TAB_STOP 4

int main(void) {
    int c, l = 0;
    while (c = getchar(), c != EOF) {
        int num_blanks;
        for (num_blanks = 0; c == ' '; c = getchar())
            ++num_blanks;

        while (num_blanks > 0) {
            int next_stop = 0;
            while (next_stop <= l)
                next_stop += TAB_STOP;

            int leap = next_stop - l;
            if (leap <= num_blanks) {
                putchar('\t');
                num_blanks -= leap;
                l += leap;
            } else {
                putchar(' ');
                --num_blanks;
                ++l;
            }
        }
        ++l;
        if (c == '\n') {
            l = 0;
        }
        putchar(c);
    }
    return 0;
}
