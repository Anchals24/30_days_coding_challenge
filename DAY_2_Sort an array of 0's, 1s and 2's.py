#Using Inbuilt sort method

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()

#Using Count Sort

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #[2,0,2,1,1,0]
        maxi = max(nums) #2
        L = [0] * (maxi+1) #[0,0,0]
        #print(L)
        for i in nums: #i = 0
            L[i] += 1  #[2,2,2]
        #print(L)#L = [2,2,2]
        j = 0 #0
        k = 0 #0
        while j < len(L): #3
            if L[j] != 0: #j = 0, k = 2
                nums[k] = j #[0,0,2,1,1,0]
                k += 1 #2
                L[j] -= 1  #[0,2,2]
            else:
                #k += 1
                j += 1

#using 3 pointers

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j , k = 0, 0, len(nums)-1
        """
        i = 1
        j = 0
        k = 4
        [0,0,2,1,1,2]
        """
        while j <= k: 
            if nums[j] == 1:
                j += 1
            elif nums[j] == 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
            elif nums[j] == 2:
                if j != k:
                    nums[j], nums[k] = nums[k], nums[j]
                k -= 1

#By maintaining the count.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_zero = 0
        cnt_one = 0
        cnt_two = 0
        for n in nums:
            if n == 0:
                cnt_zero += 1
            elif n == 1:
                cnt_one += 1
            elif n == 2:
                cnt_two += 1
        ind = 0
        while cnt_zero != 0:
            nums[ind] = 0
            cnt_zero -= 1
            ind += 1
        while cnt_one != 0:
            nums[ind] = 1
            cnt_one -= 1
            ind += 1
        while cnt_two != 0:
            nums[ind] = 2
            cnt_two -= 1
            ind += 1
            
