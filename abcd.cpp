#include <stdio.h>
double power(double base, int exponent) {
    double result = 1.0;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}
void fibonacci(int n) {
    int first = 0, second = 1, next;
    printf("Fibonacci series up to %d:\n", n);
    printf("%d, %d", first, second);
    next = first + second;
    while (next <= n) {
        printf(", %d", next);
        first = second;
        second = next;
        next = first + second;
    }
    printf("\n");
}
int main() {
    double base;
    int exponent, limit;
    printf("Enter base number: ");
    scanf("%lf", &base);
    printf("Enter exponent: ");
    scanf("%d", &exponent);
    double result = power(base, exponent);
    printf("%.2lf raised to the power of %d is %.2lf\n", base, exponent, result);
    printf("Enter the limit for Fibonacci series: ");
    scanf("%d", &limit);
    fibonacci(limit);
    return 0;
}
