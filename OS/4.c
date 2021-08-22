#include<stdlib.h>
#include<stdio.h>
#include<pthread.h>

int counter;
pthread_mutex_t mtx;

void * problema(void * p)
{
	int nr = atoi(p);

	if (nr%2==0)
	{
		pthread_mutex_lock(&mtx);
		counter++;
		pthread_mutex_unlock(&mtx);
	}
	else if (nr%5==0)
	{
		pthread_mutex_lock(&mtx);
		counter++;
		pthread_mutex_unlock(&mtx);
	}

	return NULL;
}

int main(int argc, char** argv){
	int i;
	pthread_t thr[argc];

	pthread_mutex_init(&mtx, NULL);

	for(i=1;i<argc;i++)
	{
		pthread_create(&thr[i], NULL, problema, (void*)argv[i]);
	}

	for(i=1;i<argc;i++)
	{
		pthread_join(thr[i], NULL);
	}

	printf("multiples= %d\n", counter);

	pthread_mutex_destroy(&mtx);

	return 0;
}

