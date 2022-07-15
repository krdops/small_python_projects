''''


from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        
        for i, v in enumerate(nums):
            nums[i] = v
            
    print(nums)

nums = [1,2,3,5,6,7]
x = Solution()




x.searchInsert(nums, target)
'''



'''
from typing import List
nums = [1,2,3,5,7]

target=6
en = {}


for i, v in enumerate(nums):

    en[v] = i


if target in en:
    print(target)
elif target not in en:
    en[target+1] = target

print(en)

'''
nums = [1,2,3,5,7]

target=6

for idx, num in enumerate(nums):
    if (num >= target):
        print(idx)

print(len(nums))
      


