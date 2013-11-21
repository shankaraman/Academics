#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
//#include<ipc/sem.h>
sem_t f,s;
void w1()
{
    sem_wait(&f);
    sem_wait(&s);
    sleep(10);
    sem_wait(&s);
    sem_wait(&f);
}

void w2()
{
    sem_wait(&s);
    sem_wait(&f);
    sleep(10);
    sem_wait(&f);
    sem_wait(&s);
}

int main()
{
    sem_init(&f,0,10);
    sem_init(&s,0,10);
    w1();
    w2();
 //   pthread_mutex_init(&f,NULL);
 //   pthread_mutex_init(&s,NULL);
}
