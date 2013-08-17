#include<stdio.h>
int main()
{
    int buffer[2];
    char string[100];

    printf("\nLeave ur message:\n");
    scanf("%s",string);

    pipe(buffer);

    if(fork() == 0)
    {
        close(buffer[0]);
        write(buffer[1],string);
        wait(0);
    }

    else
    {
        close(buffer[1]);
        read(buffer[0],string);
        printf("Hi I am from the pipe:%s\n",string);
    }
};
