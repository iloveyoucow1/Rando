#include <stdio.h>
#include <stdbool.h>

int main(){

    int nums[] = {0};

    int arr = sizeof(nums);
    int size = arr / 4;

    for(int i = 0; i < size; i++){
        if(i == size){
            printf("false\n");
            return false;
        }
        for(int x = 0; x < size; x++){
            printf("%d , %d\n", nums[i], nums[x]);
            if(i != x && nums[i] == nums[x]){
                printf("true\n");
                return true;
            }
        }
    }
    printf("false\n");
    return false;
}
