#include <stdio.h>

int main(void){
    int theNum;
    theNum = 15;
    char theLetter;
    theLetter = 'c';
    float theFloat;
    theFloat = 9.2;
    char greet[] = "Hello";
    printf("%s here is a number: %i, a Float: %f and a char: %c", greet, theNum, theFloat, theLetter);
    printf("\n");
    return 0;
}