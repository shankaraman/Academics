#include<stdio.h>
#include<string.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/msg.h>

#define SIZE 130

struct BUFFER
{
    long t;
    char MESSAGE[SIZE];
};

int main()
{
    struct BUFFER obj;
    int msg_id;
    key_t key;
    key = 5678;
    size_t buffer_length;
    obj.t = 1;
    char arr[130];
    int i;
    
    if((msg_id = msgget(key,IPC_CREAT|0666)) < 0)
    {
        perror("msgget");
    }
    

    printf("\nType the message which u wanted to send:\n");
    scanf("%s",arr);
    strcpy(obj.MESSAGE,arr);
    buffer_length = strlen(obj.MESSAGE)+1;
    if(msgsnd(msg_id,&obj,buffer_length,IPC_NOWAIT) < 0)
    {
        perror("msgsnd");
        exit(1);
    }
    else
    {
        printf("\nMessage Sent:%s",obj.MESSAGE);
    }
    exit(0);
}
