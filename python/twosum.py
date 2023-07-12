nums = [3,3]
target = 6


def twosum (nums, target) :
    anwser = []
    i = 0 
    while i < len(nums) :
        x = 0
        while x < len(nums) :
            if i != x :
                temp = nums[i] + nums[x]
                if temp == target :
                    anwser.append(i)
                    anwser.append(x)
                    return anwser
            x = x + 1
        i = i + 1

print(twosum(nums, target))