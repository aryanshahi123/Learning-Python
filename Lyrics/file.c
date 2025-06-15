#include <stdio.h>
#include <stdlib.h>
int main()
{
    FILE *fp;
    fp = fopen("data.txt", "w");
    int a;
    if (fp == NULL)
    {
        printf("error");
    }
    int arr[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
    {
        fprintf(fp, "%d ", arr[i]);
    }
    fclose(fp);
    fp = fopen("data.txt", "r");
    for (int i = 0; i < 5; i++)
    {
        fscanf(fp, "%d ", &a);
        printf(" %d", a);
    }
    fclose(fp);
}