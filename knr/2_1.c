#include <limits.h>
#include <printf.h>

int main(int argc, char *argv[]) {
    unsigned char uchar_min = 0;
    unsigned char uchar_max = ~uchar_min;
    signed char schar_max = 0b01111111;
    signed char schar_min = ~schar_max;
    // ...

    printf("%8s %25s %25s %10s %10s\n", "type", "dmin", "dmax", "cmin", "cmax");
    printf("----------------------------------------------------\n");
    printf("%8s %25d %25d %10d %10d\n", "uchar", 0, UCHAR_MAX, uchar_min, uchar_max);
    printf("%8s %25d %25d %10d %10d\n", "schar", SCHAR_MIN, SCHAR_MAX, schar_min, schar_max);
    printf("%8s %25d %25d %10d %10d\n", "ushort", 0, USHRT_MAX, 0, 0);
    printf("%8s %25d %25d %10d %10d\n", "sshort", SHRT_MIN, SHRT_MAX, 0, 0);
    printf("%8s %25d %25d %10d %10d\n", "uint", 0, UINT_MAX, 0, 0);
    printf("%8s %25d %25d %10d %10d\n", "sint", INT_MIN, INT_MAX, 0, 0);
    printf("%8s %25lu %25lu %10d %10d\n", "ulong", 0UL, ULONG_MAX, 0, 0);
    printf("%8s %25ld %25ld %10d %10d\n", "slong", LONG_MIN, LONG_MAX, 0, 0);
    printf("%8s %25llu %25llu %10d %10d\n", "ullong", 0ULL, ULLONG_MAX, 0, 0);
    printf("%8s %25lld %25lld %10d %10d\n", "sllong", LLONG_MIN, LLONG_MAX, 0, 0);
    return 0;
}
