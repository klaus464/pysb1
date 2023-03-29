#include <stdio.h>

int number_of_digits_in(long n)
{
    if (n == 0)
    {
        return 1;
    }

    int digit_count = 0;
    while (n != 0)
    {
        n /= 10;
        digit_count++;
    }

    return digit_count;
}

int main(void)
{
    long n;
    printf("Enter the number: ");
    scanf("%li", &n);

    printf("Number of digits in number are: %i\n", number_of_digits_in(n));
    return 0;
}