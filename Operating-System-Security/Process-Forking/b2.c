#include<stdio.h>
#include<sys/types.h>
int main()
{
    pid_t value;
    value = fork();
    if (value >= 0) //FORK1 is successful
    {
        if (value == 0) //CHILD
        {
            /*DO NOTHING*/
        }
        else //PARENT
        {
            printf("\nIm Parent and my PID:%d",getpid());
            printf("\nIm Parent and my value inside variable value is:%d\n",value);
            pid_t value1;
            pid_t value2;
            value1 = fork();//Creating Child1 and Parent1
            if (value1 >= 0) //FORK2 is successful
            {
                if (value1 == 0)//CHILD1
                {
                    printf("\nIm child1 and my PID:%d",getpid());
                    printf("\nIm child1 and my PPID:%d",getppid());
                    printf("\nIm child1 and my value in variable 
					value1 is:%d\n",value1);
                }
                else//PARENT1
                {
                    /*DO NOTHING*/
                }
            }
            else //FORK2 is unsuccessful
            {
                printf("\nFORK2 is unsuccessful!");
            }
            value2 = fork();//Creating Child2 and Parent2
            if (value2 >= 0)//Child2
            {
                printf("\nIm Child2 and my PID:%d",getpid());
                printf("\nIm Child2 and my PPID:%d",getppid());
                printf("\nIm Child2 and my value in the variable value2 is
				:%d\n",value2);

                pid_t child3,child4;
                child3 = fork(); //Creating Child3 and Parent 3

                if (child3 >= 0)//FORK3 is successful
                {
                    if (child3 == 0)//CHILD3
                    {
                        printf("\nI am child3 and my PID is:%d",getpid());
                        printf("\nI am child3 and my PPID is:%d",getppid());
                        printf("\nI am child3 and my value in the variable
						 is:%d\n",child3);
                    }
                    else//PARENT3
                    {
                        /*DO NOTHING*/
                    }
                }
                else
                {
                    printf("\nFORK3 is unsuccessful");
                }
                
                child4 = fork();//Creating Child4 and Parent4
                if(child3 >= 0)//FORK4 is successful
                {
                    if (child4 >= 0) //Child4
                    {
                        printf("\nI am child4 and my PID is:%d",getpid());
                        printf("\nI am child4 and my PPID is:%d",getppid());
                        printf("\nI am child4 and my value in variable child4 
						is:%d\n",child4);
                    }
                    else//PARENT4
                    {
                        /*DO NOTHING*/
                    }
                }
                else//FORK4 unsuccessful
                {
                    printf("\nFORK4 is unsuccessful");
                }

            }
            else//Parent2
            {
                /*DO NOTHING*/
            }
        }
    }
    else //FORK1 is successful
    {
        printf("\nFORK1 is unsuccessful!");
    }
}
