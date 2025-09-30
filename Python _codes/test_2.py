nums = [2,3,1,1]


def Number(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[i] and j != i:
                return True
        
        return False


print(Number(nums))


