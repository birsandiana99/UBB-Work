#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#define T 4

int v2=0,v3=0,v5=0,counter=0;

pthread_mutex_t mtx;

void * problema(void * p)
{
	while(counter<30)
	{
		pthread_mutex_lock(&mtx);
		if(counter>=30)
		{
			pthread_mutex_unlock(&mtx);
			return NULL;
		}
		int nr=rand();
                printf("%d\n",nr);
                counter++;
                pthread_mutex_unlock(&mtx);
		if(nr%2==0)
		{
			pthread_mutex_lock(&mtx);
			v2++;
			pthread_mutex_unlock(&mtx);
		}
		if(nr%3==0)
		{
			pthread_mutex_lock(&mtx);
			v3++;
			pthread_mutex_unlock(&mtx);
		}
		if(nr%5==0)
		{
			pthread_mutex_lock(&mtx);
			v5++;
			pthread_mutex_unlock(&mtx);
		}
	}
	return NULL;
}

int main()
{
	srand(time(NULL));

	int i;
	pthread_t thr[T];
	
	pthread_mutex_init(&mtx,NULL);

	for(i=0;i<T;i++)
	{
		pthread_create(&thr[i], NULL, problema, NULL);
	}

	for(i=0;i<T;i++)
	{
		pthread_join(thr[i], NULL);
	}

	pthread_mutex_destroy(&mtx);

	printf("counter=%d\n",counter);

	printf("v2= %d; v3= %d; v5= %d;\n",v2,v3,v5);

	return 0;
}
