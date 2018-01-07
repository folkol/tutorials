#include <stdio.h>

#define LOWER 0
#define UPPER 300
#define STEP 20

float to_celsius(float fahr) {
    return (5.0f / 9.0f) * (fahr - 32.0f);
}

int main(void) {
    printf("Fahr Celcius\n");
    for (int fahr = LOWER; fahr <= UPPER; fahr += STEP)
        printf("%3d %6.1f\n", fahr, to_celsius(fahr));
    return 0;
}
