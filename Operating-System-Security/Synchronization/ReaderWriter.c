#include<stdio.h>  
#include<semaphore.h>
#include<sys/types.h>
#include<stdlib.h>
#include<pthread.h>  

void *reader(void *) ;  
void *writer (void *) ;  
sem_t X,Y,READ,WRITE ;  
int rc=0 ;  
int wc=0 ;  

void *reader(void * arg)  
{  
	int c = (int)arg ;   
    sem_wait(&READ);  
    sem_wait(&X);  
    rc++;  
    if(rc==1)  
	{
         sem_wait(&WRITE) ;  
	}
   sem_post(&X);  
   sem_post(&READ);  
   sleep(1);  

   printf("\nReader %d using\n ",c);  
   sleep(1) ;  
   printf("\nReader%d has finished\n",c); 
   sem_wait(&X);  
   rc-- ;  
   if(rc == 0)  
   {
      sem_post(&WRITE);  
   }
  sem_post(&X);  
} 
 
void *writer(void * arg)  
{  
	int c = (int)arg;
	sem_wait(&Y);  
	wc++;  
	if(wc == 0)  
	{
      sem_wait(&READ);  
	}
	sem_post(&Y);  
	sem_wait(&WRITE);  
	printf("\nWriter %d is using\n",c) ;  
	sleep(1);  
	printf("\nWriter%d has finished\n",c);  
	sem_post(&WRITE);  
	sem_wait(&Y);  
	wc--;  
    if(wc == 0)  
    {
      sem_post(&READ);  
	}
    sem_post(&Y);  
 }
  
int main()  
{ 
	pthread_t READER1,READER2,WRITER1,WRITER2; 
	sem_init(&WRITE,0,1) ;  
	sem_init(&X,0,1) ;  
	sem_init(&READ,0,1) ;  
	sem_init(&Y,0,1) ;  
    int count1=1,count2=1;  
	pthread_create(&READER1,NULL,reader,(void *)count1++);  
	pthread_create(&WRITER2,NULL,writer,(void *)count2++);  
	pthread_create(&READER2,NULL,reader,(void *)count1++);  
	pthread_create(&WRITER2,NULL,writer,(void *)count2++);  
	pthread_join(READER1,NULL);  
	pthread_join(WRITER1,NULL);  
	pthread_join(READER2,NULL);  
	pthread_join(WRITER2,NULL) ;  
 }  
