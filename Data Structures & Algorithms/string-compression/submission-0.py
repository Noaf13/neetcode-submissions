class Solution:
    def compress(self, chars: List[str]) -> int:

        i = 0 
        insert = 0
        n = len(chars)
        while i < n:
            group = 1

            while i + group < n and chars[i + group] == chars[i]:
                group +=1

            chars[insert] = chars[i]
            #move insert pointer 1 to the right
            insert +=1

            if group > 1 :
                string_number = str(group)
                chars[insert:insert + len(string_number)] = list(string_number)
                insert += len(string_number)
            i+= group
        return insert

        