#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int d;
    long ld;
    char c;
    float f;
    double lf;
    scanf(" %d ", &d);
    scanf(" %ld ", &ld);
    fflush(stdin);
    scanf(" %c ", &c);
    fflush(stdin);
    scanf(" %f ", &f);
    scanf(" %lf ", &lf);
    
    printf("%d\n", d);
    printf("%ld\n", ld);
    printf("%c\n", c);
    printf("%.3f\n", f);
    printf("%.9lf\n", lf);
    return 0;
}
