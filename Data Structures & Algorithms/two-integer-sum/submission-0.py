class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        # create hashmap stor num to index for quick look up-empty dictionary 

        # loopusing enumerate
        for i,num in enumerate(nums):
            #enumerate creates index number based of array
            compliment = target - num
        
            if compliment in num_to_index:
                # if that  number is in the array
                return[num_to_index[compliment],i]
                # get the index for it

            #if not then fill up hashmap so u can refer back to it
            num_to_index[num] = i
    