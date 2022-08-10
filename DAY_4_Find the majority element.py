#Brute-Force Method : Using 2 for loops

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            if count > len(nums)/2:
                return nums[i]
        return -1

#By Dictionary

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt = {}
        for num in nums:
            if num in dictt:
                dictt[num] += 1
            else:
                dictt[num] = 1
            
        maxvalue = max(dictt.values())
        keys = [k for k, v in dictt.items() if v == maxvalue]
        return keys[0]
        

#Using Moore's Voting Algorithm

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        cnt = 1
        for i in range(len(nums)):
            if nums[candidate] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                candidate = i
                cnt = 1
        return nums[candidate]
        

        
