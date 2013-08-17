#include<stdio.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<stdlib.h>
int main(int argc, char *argv[])
{
    int status=0,retval=0;
    if (argc < 2)
    {
        printf("\nProvide atmost one argument:");
    }
    else
    {
        pid_t pid;
        pid = fork();
        if (pid >= 0)
        {
            if (pid == 0)
            {
                printf("\n");
                system(argv[1]);
                printf("\nChild process execution over!\n");
                printf("\nEnter a code:");
                scanf("%d",&retval);
                printf("\nChild:Bye!\n");
                exit(retval);
            }
            else
            {
//                printf("\nParent is waiting!");
                wait(&status);
//                system("ifconfig");
                printf("\nParent:Bye!\n");
                exit(0);
            }
        }
        else
        {
            printf("\nError!");
        }
    }
    return 0;
}
