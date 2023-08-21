#Solution to contains-duplicate leetcode number 217
nums = [1,1,1,3,3,4,3,2,4,2]

def dups(nums):
    nums.sort()
    pointer0 = 0
    pointer1 = 1
    try:
        for i in nums:
            if nums[pointer0] == nums[pointer1]:
                return True
            pointer0 += 1
            pointer1 += 1
    except IndexError:
        return False











print(dups(nums))






                #print(point1)
                #print(point2)
                #print(nums[point1])
                #print(nums[point2])