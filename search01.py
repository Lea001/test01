def searchInsert1( nums, target):
    lenght = len(nums)
    # 比所有数值大
    if target > nums[lenght - 1]:
        return lenght
    # 比所有数值小
    elif target <= nums[0]:
        return 0
    else:
        left = 0
        right = lenght - 1
        while left <= right :
            mid = left + ((right - left) // 2)
            if target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid - 1
            elif target == nums[mid] :
                return mid
        return left
def searchInsert2(nums,target):
    lenght = len(nums)
    for i in range(lenght):
        if nums[i] >= target:
            return i
    if nums[i] < target:
        return i+1

nums = [1,3,5,6]
target = 7
print(searchInsert1(nums,target))
print(searchInsert2(nums,target))


