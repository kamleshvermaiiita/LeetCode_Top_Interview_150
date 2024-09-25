class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # Varibles
        f = 0
        l = len(nums)-1
        
        # Logic
        while f <= l:
            m = (f+l) // 2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                f = m + 1
            else:
                l = m - 1
        
        return f
        
        