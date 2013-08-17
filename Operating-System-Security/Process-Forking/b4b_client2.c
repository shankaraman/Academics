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
    if ((msg_id = msgget(key,0666)) < 0)
    {
        perror("msgget");
        exit(1);
    }

    if (msgrcv(msg_id,&obj,SIZE,1,0) < 0)
    {
        perror("msgrcv");
        exit(1);
    }

    printf("\n%s\n",obj.MESSAGE);
    exit(0);
}
