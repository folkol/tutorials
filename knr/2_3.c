#include <assert.h>
#include <string.h>
#include <math.h>

int ctoi(char c) {
    if (c >= '0' && c <= '9') {
        return c - '0';
    }
    if (c >= 'a' && c <= 'f') {
        return 10 + c - 'a';
    }
    if (c >= 'A' && c <= 'F') {
        return 10 + c - 'A';
    }
    assert(0 && "Unknown char");
}

unsigned int htoi(char *s) {
    size_t len = strlen(s);
    if (len > 1) {
        if (s[0] == '0' && (s[1] == 'x' || s[1] == 'X')) {
            s += 2;
            len -= 2;
        }
    }
    unsigned int val = 0;
    for (int i = 0; i < len; ++i) {
        val += pow(16, i) * ctoi(s[len - i - 1]);
    }
    return val;
}

int main(int argc, char *argv[]) {
    assert(htoi("0") == 0);
    assert(htoi("1") == 1);
    assert(htoi("ff") == 255);
    assert(htoi("FF") == 255);
    assert(htoi("0xFF") == 255);
    assert(htoi("0XFF") == 255);
    assert(htoi("0xCAFEBABE") == 3405691582);
    assert(htoi("0xCAFED00D") == 3405697037);
}
