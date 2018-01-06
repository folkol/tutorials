#include <stdio.h>

int main(void) {
    float fahr, celsius;
    int lower, upper, step;

    lower = 0;
    upper = 150;
    step = 10;

    celsius = lower;
    printf("Celcius Fahr\n");
    while (celsius <= upper) {
        fahr = 32.f + celsius / (5.0f / 9.0f);
        printf("%3.0f %6.1f\n", celsius, fahr);
        celsius = celsius + step;
    }
    return 0;
}
