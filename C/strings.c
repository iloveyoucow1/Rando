#include <stdio.h>
#include <string.h>

int main(){
    char name0[20] = "dub ";
    char name1[] = "mcmillen";
    printf("%ld\n", strlen(name0));

    strcat(name0, name1);
    printf("%s\n", name0);

    return 0;
}