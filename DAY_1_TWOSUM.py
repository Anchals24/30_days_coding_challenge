#PROBLEM STATEMENT

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

#Please give me time till EOD to update all the approaches.


"""
Brute-Force Approach:
"""
class Solution:
    def twoSum(self, nums, target):
        
        result_list = []
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result_list.append(i)
                    result_list.append(j)

        return result_list

  
"""
Approach 2 : Using set/dictionary
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, size = 0,len(nums)
        temp = set()
        while(i<size):
            find = target - nums[i]
            if find in temp:
                return [i,nums.index(find)]
            else:
                temp.add(nums[i])
            i += 1
                
        return []

      
"""
Approach 3 : Using 2 pointers
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        arr=[]
        for i,val in enumerate(nums):
            arr.append([val,i])
        
        arr.sort()
        
        i=0
        j=len(nums)-1
        
        while i<j:
            if arr[i][0]+arr[j][0]==target:
                return [arr[i][1],arr[j][1]]
            elif arr[i][0]+arr[j][0]<target:
                i+=1
            else:
                j-=1
  
