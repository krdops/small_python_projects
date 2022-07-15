from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        count1 = 0
        count2 = 0
        for i in range(0, len(nums)):
            x = 0
            
            for z in range(0, len(nums)):
                
                y = nums[i] + nums[z]
                
                if y == target and i != z:
                    answer = [i,z]
                    return answer
                print(count2)
                count2 += 1
            count1 += 1
            
    def twoSumB(self, nums: List[int], target: int) -> List[int]:


        fullset = {}


        for i, value in enumerate(nums):
            remaining = target - nums[i]
         
            if remaining in fullset:
                return [i, fullset[remaining]]
            
            fullset[value] = i


sol = Solution()

nums = [3,2,4]
target = 6
print(sol.twoSumB(nums, target))

