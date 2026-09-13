# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
   # 1. find the middle 
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        #slow is middle - cut to the first elem of second section
        curr2 = slow.next

        #2. cut it at middle 
        slow.next = None
        prev = None
        #3. reverse

        while curr2:
            temp = curr2.next 
            
            curr2.next = prev
            prev = curr2
            curr2 = temp
        #prev = head of the second reversed section

        firsth = head
        secondh = prev

        while secondh:
            temp1 = firsth.next
            temp2 = secondh.next 

            firsth.next = secondh
            secondh.next = temp1 

            firsth = temp1
            secondh = temp2

    
