#include <stdio.h>

int test(int item){
    int test1 = 0;
    int test2 = 0;

    test2 = test1 + item;
    printf("%i\n", test1);
    printf("%i\n", test2);
    return 0;
}

int main(){
    int pam = 1;
    test(pam);
    test(pam);
}