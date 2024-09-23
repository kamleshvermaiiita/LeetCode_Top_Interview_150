class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        #Varibles
        i = 0
        
        # Logic
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
        