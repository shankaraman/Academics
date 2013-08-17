#include<stdio.h>
#include<sys/ipc.h>
#include<sys/shm.h>
#include<sys/types.h>
#include<stdlib.h>

#define SIZE 100
int main()
{
    char character,*shared_memory,*shared;
    int shared_memory_id,i;

    key_t key;
    key = 1678;

    if ((shared_memory_id = shmget(key ,SIZE , IPC_CREAT | 0666)) < 0)
	//Creating and Granting read and write access to the server
	//Getting access to a shared memory with a key and a size with permissions
    {
        perror("shmget");
        exit(1);
    }

    if ((shared_memory = shmat(shared_memory_id,NULL,0)) == (char *)-1) 
	//Since shm is a char * and  thus we are type casting -1 to char *
	//Attaching the shared memory id to the shared memory
    {
        perror("shmat");
        exit(1);
    }

    shared = shared_memory;

    printf("\nEnter 4 Characters:\n");
    for(i=0;i<8;i++)
    {
        scanf("%c",&character);
        *shared++ = character;
    }
    *shared = NULL; 
	//A string to determine the boundary for the client. See the client snippet 
	//to understand the usage of this marker.
    exit(0);
}
