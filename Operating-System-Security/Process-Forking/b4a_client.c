#include<stdio.h>
#include<stdlib.h>
#include<sys/types.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#define SIZE 100

int main()
{
    int shared_memory_id;
    char *shared_memory,*objects;

    key_t key;
    key = 1678;

    if ((shared_memory_id = shmget(key, SIZE, 0666)) < 0)
    {
        perror("shmget");
        exit(1);
    }

    if ((shared_memory = shmat(shared_memory_id,NULL,0)) == (char *)-1)
    {
        perror("shmat");
        exit(1);
    }
    printf("\nHere we go! I got your Six Characters from the Shared memory!\n");

    for(objects=shared_memory;*objects!=NULL;objects++)
    {
        putchar(*objects);
    }
    putchar('\n');
    exit(0);
}
