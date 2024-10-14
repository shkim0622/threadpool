#include<stdio.h>
#include<pthread.h>
#include<unistd.h>

void *test( void *a);

int main() {
    pthread_t t0;

    int ste = pthread_create( &t0, NULL, test, NULL );
    printf("create Thread \n");
    if (ste == -1) {
        printf("thread fail");
        pthread_exit(PTHREAD_CANCELED);
    }
    pthread_join(t0, NULL);
    return 0;
}

void *test( void *a)    {
    int i = 0;
    while(i<5){
        sleep(1);
        printf("thread : %d\n", i);
        i++; 
    }
    pthread_exit(PTHREAD_CANCELED);
}

