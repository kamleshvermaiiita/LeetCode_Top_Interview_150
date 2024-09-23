class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # Varibles
        count = 1
        i = 0
        
        # Logic
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                count += 1
                if count > 1:
                    nums.pop(i+1)
                    count -= 1
            else:
                i += 1
        
        return len(nums)
            
            
        