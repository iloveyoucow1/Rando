#include <stdio.h>

int main() {
    int i = 0;
    while (i < 5){
        printf("%i \n", i);
        i++;
    }
    
    for (int x = 0; x < 5; x++){
        printf("%i \n", x);
    }
    int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} };
    printf("%d %d %d\n", matrix[0][0], matrix[0][1], matrix[0][2]);
    printf("%d %d %d\n", matrix[1][0], matrix[1][1], matrix[1][2]);
}