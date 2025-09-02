# LEETCODE


# class Solution(object):
#     def searchRange(self, nums, target):
#         result = [-1, -1]
        
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 if result[0] == -1:   
#                     result[0] = i
#                 result[1] = i         
        
#         return result


nums = [5,7,7,8,8,10]
target = 8
result = [-1, -1]

for i in range(len(nums)):
    if nums[i] == target:
        if result[0] == -1:   # first occurrence
            result[0] = i
        result[1] = i         # keep updating last occurrence



print(result) #[3,4]

