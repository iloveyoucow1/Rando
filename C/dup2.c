#include <stdio.h>
#include <stdbool.h>

int main(){
    int nums[] = {1,1,1,3,3,4,3,2,4,2};
    int size = sizeof(nums)/sizeof(nums[0]);

    if(size == 1){
        return false;
    }
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