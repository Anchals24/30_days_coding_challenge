#Brute-Force Method : Using 2 for loops

class Solution:
    def findDuplicate(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
	            if nums[i]==nums[j]:
		            return nums[i]

#By sorting the array

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

#Using Binary Search

class Solution:
    def findDuplicate(self, nums: List[int]) -> None:
        nums.sort()
        l,r = 0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]<mid+1:
		r = mid - 1
            else:
		l = mid + 1
        return l

#By Linked List Cycle Method

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow ==fast:
                break
        
        fast = nums[0]
        while slow !=fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

#By using Hashmap 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for k,v in hashmap.items():
            if v > 1:
                return k
