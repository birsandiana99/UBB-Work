#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<string.h>

//v vowels, n digits

int v=0, n=0;

pthread_mutex_t mtx;

void * problema(void * p)
{
	char * word = (char *)p;
	int i;

	for(i=0;i<strlen(word);i++)
	{
		if(strchr("aeiouAEIOU",word[i])!=NULL)
		{
			pthread_mutex_lock(&mtx);
			v++;
			pthread_mutex_unlock(&mtx);
		}
		if(strchr("0123456789",word[i])!=NULL)
		{
			pthread_mutex_lock(&mtx);
			n++;
			pthread_mutex_unlock(&mtx);
		}
	}

	return NULL;
}

int main(int argc, char** argv)
{
	int i;
	pthread_t thr[argc];

	pthread_mutex_init(&mtx, NULL);

	for(i=1;i<argc;i++)
	{
		pthread_create(&thr[i], NULL, problema, (void *)argv[i]);
	}

	for(i=1;i<argc;i++)
	{
		pthread_join(thr[i], NULL);
	}

	printf("v= %d; n= %d;\n",v,n);

	pthread_mutex_destroy(&mtx);

	return 0;
}
