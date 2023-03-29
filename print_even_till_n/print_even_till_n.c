#include <stdio.h>

void print_even_till(int n)
{
    for (int i = 2; i <= n; i += 2)
    {
        printf("%i ", i);
    }
    printf("\n");
    return;
}

int main(void)
{
    int n;
    printf("Enter the value of n: ");
    scanf("%i", &n);

    print_even_till(n);
    return 0;
}