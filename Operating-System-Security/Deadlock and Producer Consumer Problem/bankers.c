#include<stdio.h>
#define PASS 1
#define FAIL 0
int allocate(int);
int deallocate(int);
int check();
int ac(int);

/* Global Variables and Resources */

int ps,src;
int MAX_RESOURCE[10][10],resources[10],int current[10][10],need[10][10];
int total[10],available[10],finish[10];
 
int main()
{
 
	int i, j;
	printf("\n \n Enter the no. of processes and the shared resource:");
	scanf(" %d", &ps);
	scanf(" %d", &src); 
/* Maximum resource available */
	printf("\Enter the maximum resource available matrix:");
	for(i = 1; i <= src; i++)
		scanf(" %d", &resources[i]);
		
 /* Maximum needed */
    printf("\nEnter the maximum needed:");
	for(i = 1; i <= ps; i++)
	{
		for(j = 1; j <= src; j++)
		{
			printf("\n Resource %d for Process %d :", j, i);
			scanf(" %d", &MAX_RESOURCE[i][j]);
		}
	}
/* Currently Allocated Matrix */ 
	printf("\n Enter the current allocated matrix:");
	for(i = 1; i <= ps; i++)
	{
		for(j = 1; j <= src; j++)
		{
			printf("\n Resources %d for Process %d :", j, i);
			scanf(" %d", &current[i][j]);
 
		}
	}
 /* Need Matrix can be calculated as Max - Allocated */
	for(i = 1; i <= src; i++)
	{
		for(j = 1; j <= ps; j++)
		{
			total[i] = total[i]+ current[j][i];
			need[j][i] = MAX_RESOURCE[j][i] - current[j][i];
		}
		available[i] = resources[i] - total[i];
	}
	
/* Remaining resources for allocation */ 

	printf("\n Remaining Resource: \n");		
	for(i = 1; i <= src; i++)
	{
		printf(" %d \t ", available[i]);
	}
	
	while(check(ps)!=0)
	{
		for(i = 1; i <= ps; i++)
		{
			if(finish[i] ==  0)
			{
				if(ac(i))
				{
					printf("\n \n Allocated: \n");					
					allocate(i);
					printf("\n \n Deallocated: \n");
					deallocate(i);
				}
			}
		}
	}
}
 
 
int check()
{
	int i;
	for(i = 1; i <= ps; i++)
	{
		if(finish[i] == FAIL)
			return PASS;
	}
	return FAIL;
}
 
int ac(int data)
{
	int i, j, flag = FAIL;
	for(i = 1; i <= src; i++)
	{
		if(available[i] < need[data][i])
		{
			flag = PASS;
			break;
		}
 
	}
	if(flag == FAIL)
		return PASS;
 
	return FAIL;
}
 
 
int allocate( int data)
{
	int i,j;
	for(i = 1; i <= src; i++)
	{
		available[i] = available[i] - need[data][i];
		current[data][i] = MAX_RESOURCE[data][i];
	}
 
	for(i = 1; i <= ps; i++)
	{
		for(j = 1; j <= src; j++)
		{
			printf("%d\t", current[i][j]);
		}
	}
	printf("\n Resource after allocation:\n");
	for(i = 1; i <= src; i++)
	{
		printf("%d\t", available[i]);
    }
 
}
 
int deallocate(int data)
{
	int i, j;
	for(i = 1; i <= src; i++)
	{
		available[i] = available[i] + current[data][i];
		current[data][i] = FAIL;
	}
 	finish[data] = PASS;
 
	for( i = 1; i <= ps; i++)
	{
		for(j = 1; j <= src; j++)
		{
			printf("%d\t", current[i][j]);
		}
	}
 
	printf("\n \n");
	printf("\nResource After deallocation :\n");
	for(i = 1; i <= src; i++)
	{
		printf(" %d \t", available[i]);
    }
}
