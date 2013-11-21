#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define TRUE 1
int main(int argc, char *argv[], char *envp[])
{
    char buffer[70000];
    char *args[70000];
    int *ret_status;
    size_t nargs;
    pid_t pid;
    printf("\nPress CTRL+C to exit!\n");
    while(TRUE)
    {
        printf("h1dd3ntru7h> ");
        fgets(buffer, 70000, stdin);
        parse_args(buffer, args,70000, &nargs); 
        if (nargs==0)
        {
            continue;
        }
        pid = fork();
        if (pid)
        {
            pid = wait(ret_status);
        } 
        else 
        {
            if( execvp(args[0], args)) 
            {
                printf("\nError!\n");
            }
        }
    }    
    return 0;
}
void parse_args(char *buffer, char** args,size_t args_size, size_t *nargs)
{
    char *BUFFER[args_size];
    char **CHECK;
    char *WRITE_BUFFER;
    size_t i, j;
    WRITE_BUFFER=buffer;
    BUFFER[0]=buffer; 
    args[0] =buffer;
    for(CHECK=BUFFER; (*CHECK=strsep(&WRITE_BUFFER,"\n\t")) != NULL;)
    {
        if ((*CHECK != NULL) && (++CHECK >= &BUFFER[args_size]))
        {
            break;
        }
    }
    for (j=i=0; BUFFER[i]!=NULL; i++)
    {
        if(strlen(BUFFER[i])>0)
        {
            args[j++]=BUFFER[i];
        }
    }
    *nargs=j;
    args[j]=NULL;
}
