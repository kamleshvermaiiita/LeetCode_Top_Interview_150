class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        Temp = []
        i = 0
        j = 0
        while (i < m and j < n):
            if (nums1[i] < nums2[j]):
                Temp.append(nums1[i])
                i += 1
            elif (nums1[i] > nums2[j]):
                Temp.append(nums2[j])
                j += 1
            else :
                Temp.append(nums1[i])
                Temp.append(nums2[j])
                i += 1
                j += 1
        
        if(i < m):
            while(i < m):
                Temp.append(nums1[i])
                i += 1

        if(j < n):
            while(j < n):
                Temp.append(nums2[j])
                j += 1

        nums1[0:m+n] = Temp[0:m+n]
        