#include <stdio.h>

void main()
{
    int num, i, count = 0, sum = 0, c = 0;
    while (count < 5)
    {
        printf("Enter a number:");
        scanf("%d", &num);
        c = 0;
        for (i = 1; i <= num; i++)
        {
            if (num % i == 0)
            {
                c++;
            }
        }
        if (c == 2)
        {
            sum += num;
            count++;
        }
        else
        {
            printf("Not a prime number.\n");
        }
    }
    printf("The sum of prime numbers is %d", sum);
}