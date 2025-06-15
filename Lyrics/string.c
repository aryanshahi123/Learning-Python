#include <stdio.h>
#include <string.h>

int length(char str[20]);

void main()
{
    char st[20];
    printf("Enter a string:");
    scanf("%[^\n]", st);
    int l = length(st);
    printf("The length of string is %d", l);
}

int length(char str[20])
{
    int val;
    val = strlen(str);
    return val;
}