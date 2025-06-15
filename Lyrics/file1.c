#include <stdio.h>
#include <stdlib.h>

void main()
{
    FILE *fp1, *fp2;

    fp1 = fopen("NUM.DAT", "r");
    fp2 = fopen("INT.DAT", "w");
    float num, check;
    while (fscanf(fp1, "%f ", &num) != EOF)
    {
        check = num - (int)num;
        if (check == 0)
        {
            fprintf(fp2, "%d ", (int)num);
        }
    }
    printf("Copied Successfully");
    fclose(fp1);
    fclose(fp2);
}