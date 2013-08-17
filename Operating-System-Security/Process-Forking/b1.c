#include<stdio.h>
#include<sys/types.h>
int main()
{
    pid_t values;
    values = fork();

    if (values >= 0)// Fork1 is successful
    {
        if (values == 0)//Child process
        {
/*            printf("\nI am Child and my PID will be:%d",getpid());
            printf("\nI am Child and my PPID will be:%d",getppid());
            printf("\nI am Child and my value in the variable is:%d\n",values);*/
        }
        else // Parent Process
        {
            printf("\nI am the Parent and my PID will be:%d",getpid());
            printf("\nI am the Parent and my value in variable values will be:%d\n"
			,values);
            pid_t child1 = fork();

            if (child1 >= 0)// Fork2 is successful
            {
                if (child1 == 0)// Child1
                {
                    printf("\nIm Child1 PID:%d",getpid());
                    printf("\nIm Child1 PPID:%d\n",getppid());
                    printf("\nIm Child1 and value in my variable child1 is:%d\n"
					,child1);

                    pid_t child2;
                    child2 = fork();

                    if (child2 >= 0)//Fork3 is successful
                    {
                        if (child2 == 0) //Child2
                        {
                            printf("\nIm child2 and my PID is:%d",getpid());
                            printf("\nIm child2 and my PPID is:%d",getppid());
                            printf("\nIm child2 and my value in variable 
								child2:%d\n",child2);
                        }
                        else //Parent2
                        {
/*                         
                        }
                    }
                    else //Fork3 is Unsuccessful
                    {
                        printf("\nFork3 is unsuccessful!");
                    }
                }   
                else // Parent1
                {
/*                   
                }   
            }
            else //Fork2 Unsuccessful
            {
                printf("\nFork1 unsuccessful!");
            }
        }

    }
    else//Fork1 is Unsuccessful
    {
        printf("\nFork1 is not successful:");
    }
}
