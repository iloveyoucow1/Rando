nums = [2,7,11,15]
target = 9


def twosum(nums, target) :
    for x in nums :
        for y in nums:
            if x + y == target :
                return [x, y]


print(twosum(nums, target))