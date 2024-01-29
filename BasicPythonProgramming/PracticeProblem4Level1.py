def find_nine(nums):
    #Remove pass and write your code here
    for i in range(len(nums) if len(nums)<5 else 4):
        if nums[i]==9:
            return True
        
    return False

nums=[1,9,4,5,6]
print(find_nine(nums))

