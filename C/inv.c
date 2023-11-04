#include <stdio.h>

int pickup(int called){
    int user;
    if (called == 0){
        printf("Would you like to pick up a Ruby? Gold? or Nothing?(1 2 or 3)\n");
        scanf("%d", &user);
    }
    if (called > 0){
        printf("Would you like to pick up another Ruby? Gold? or Nothing?(1 2 or 3)\n");
        scanf("%d", &user);
    }
    printf("%i", user);
    if (user == 1)
    return 0;
}

int read_inv(){
    FILE *fptr;

    // Open a file in read mode
    fptr = fopen("inv.txt", "r");

    // Store the content of the file
    char myString[100];

    // Read the content and store it inside myString
    fgets(myString, 100, fptr);

    // Print the file content
    printf("%s", myString);

    // Close the file
    fclose(fptr);   
    }

int add_inv(int item_amount, int item_code){
    FILE *fptr;

    // Open a file in writing mode
    fptr = fopen("inv.txt", "w");

    // Write some text to the file
    fprintf(fptr, "Some text");

    // Close the file
    fclose(fptr);
}



int main(){
    read_inv();
}