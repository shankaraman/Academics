#include <pthread.h>
#include <stdio.h>
#include<sys/wait.h>

int main()
{
	pthread_t T1;
	pthread_t T2;
	pthread_t T3;
	void *f1(),*f2(),*f3();
	pthread_create(&T1, NULL, f1, NULL);
	pthread_create(&T2, NULL,f2, NULL);
	pthread_create(&T3, NULL,f3,NULL);
	pthread_join(T1,NULL);
	pthread_join(T2,NULL);
	pthread_join(T3,NULL);
	return 0;
}
void *f1()
{
	printf("Thread 1");
	usleep(1);
	return NULL;
}
void *f2()
{
	printf("\nThread 2\n");
	usleep(1);
	return NULL;
}
void *f3()
{
	printf("\nThread 3\n");
	usleep(1);
	return NULL;
}
