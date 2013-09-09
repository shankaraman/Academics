#include<stdio.h>
void helloFromC(int x)
{
  printf("\nI am from C\n");
  printf("I got value %d", x);
}

if (sched_setaffinity( gettid(), sizeof( cpu_set_t ), &set ))
{
  perror( "sched_setaffinity" );
  return NULL;
}
