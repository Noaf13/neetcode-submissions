class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_close  ={"{":"}","[":"]","(":")"}

        for char in s:
            if char in open_close:
                # looks through the key
                stack.append(char)
            elif len(stack) == 0 or open_close[stack.pop()] != char :
                return False
        else:
             return len(stack) == 0 

        