def findDuplicate(nums):
    xor = 0
    for i in range(len(nums)):
        xor ^= nums[i]
    for i in range(1, len(nums)):
        xor ^= i
    return xor

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 6]
    print('The duplicate element is: ', findDuplicate(nums))