class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Input: strs = ["act","pots","tops","cat","stop","hat"]
        # dict key same for each value 
        # 'act'= [act,cat]
        # 'opst'= [opst,tops,stop]
        # 'aht'= [hat]
        anagram = defaultdict(list)
        for word in strs:
            # sort out the keys for it  
            sorted_word = "".join(sorted(word))
            #you can not use a list as a dictionary key as its not hashable
            print(sorted_word)

            #appemd to the dictionary 
            anagram[sorted_word].append(word)

        return list(anagram.values())
