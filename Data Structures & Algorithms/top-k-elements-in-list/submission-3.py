class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Input: nums = [1,2,2,3,3,3], k = 2
        # dict - key as unique numbers and each time it adds onje to the value 

        numberf = defaultdict(int) 

        for num in nums:
            numberf[num]+=1
        print(numberf)
        freq = sorted(numberf.keys(), key=lambda x: numberf[x], reverse=True)
        print(freq)
        return freq[:k]

      


       
        
        