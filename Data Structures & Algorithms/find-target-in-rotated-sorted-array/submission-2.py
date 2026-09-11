class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1 

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m 
            
            # Left sorted section
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m
                else:
                    l = m+1

            else:        
            # right sorted section

                if target>= nums[m] and target <= nums[r]:
                    l = m 
                else:
                    r = m -1
        return -1
            


            
            

