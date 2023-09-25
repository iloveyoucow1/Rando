#include <stdio.h>

int main(){
    int myNum = 5;
    int yourNum = 5;
    int sum = myNum + yourNum;

    printf("My num is %i your num is %i and the sum is %i", myNum, yourNum, sum);
    printf("\n");

    if (myNum == yourNum){
        printf("My num is equal to your num.");
        printf("\n");
    }


    return 0;
}