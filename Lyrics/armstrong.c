#include <stdio.h>

void main()
{
    int n, rem, sum = 0, count = 0, mul, ori, i;
    printf("Enter a number:");
    scanf("%d", &n);
    ori = n;
    while (n > 0)
    {
        count += 1;
        n = n / 10;
    }
    n = ori;
    while (n > 0)
    {
        rem = n % 10;
        mul = 1;
        for (i = 1; i <= count; i++)
        {
            mul = mul * rem;
        }
        sum += mul;
        n = n / 10;
    }
    if (sum == ori)
    {
        printf("%8.3s", "Armstrong.");
    }
}