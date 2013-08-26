#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
void *producer(void *);
void *consumer(void *);
sem_t mutex,full,empty;
int buffer[5],front,rear;
int main()
{
    pthread_t t1,t2;
    sem_init(&mutex,0,1);
    sem_init(&full,0,1);
    sem_init(&empty,0,5);
    pthread_create(&t1,NULL,producer,NULL);
    pthread_create(&t2,NULL,consumer,NULL);
    pthread_join(t1,NULL);
    pthread_join(t2,NULL);
}

void *producer(void *arg)
{
    int i;
    for(i=0;i<3;i++)
    {
        sem_wait(&empty);
        sem_wait(&mutex);
        printf("Producer %d\n",i);
        rear++;
        buffer[(rear)%5]=i;
        sleep(1);
        sem_post(&mutex);
        sem_post(&full);
    }
}
void *consumer(void *arg)
{
    int item,i;
    for(i=0;i<3;i++)
    {
            sem_wait(&full);
            sem_wait(&mutex);
            front++;
            item=buffer[(front)%5];
            printf("Consumer %d\n",item);
            sleep(1);
            sem_post(&mutex);
            sem_post(&empty);
    }
}
