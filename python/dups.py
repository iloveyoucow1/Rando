#Solution to contains-duplicate leetcode number 217 fails at time check brute force
nums = nums = [1,2,3,1]

def dups(nums):
    pointer0 = 0
    for i in nums:
        pointer1 = 0
        for x in nums:
            if pointer0 != pointer1:
                if nums[pointer0] == nums[pointer1]:
                    return True
            pointer1 = pointer1 + 1
        pointer0 = pointer0 + 1

    return False

print(dups(nums))