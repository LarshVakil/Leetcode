
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
            
        curr = head
        
        while curr and curr.next:

            val1 = curr.val
            val2 = curr.next.val
            gcd = 0 
            a = val1
            b = val2

            while b > 0 :
                a , b = b , a%b 

                gcd = a

            new = ListNode(gcd)
            new.next = curr.next
            curr.next = new

            curr = new.next

        return head
    