#include <stdio.h>

void file(){
    FILE *fptr;

    fptr = fopen("filename.txt", "w");

    fprintf(fptr, "This Work?");

    fclose(fptr);
}

int main(){
    file();
    return 0;
}