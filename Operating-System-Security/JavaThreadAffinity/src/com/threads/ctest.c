#define _GNU_SOURCE
#include <stdio.h>
#include <errno.h>
#include <sched.h>

int _setaffinity_thread(int pid, int n, int *masks) {
  int i;
  int retval=0;

  cpu_set_t  mask;

  CPU_ZERO(&mask);
  for(i=0;i<n;i++)
    CPU_SET(masks[i], &mask);

  retval = sched_setaffinity(pid, sizeof(cpu_set_t), &mask);
  if ( retval == 0 )
    return 0;

  if (errno == EFAULT)
    return 1;
  else if (errno == EINVAL)
    return 2;
  else if (errno == EPERM)
    return 3;
  else if (errno == ESRCH)
    return 4;
}



int _getcpu() {
  return sched_getcpu();
}

