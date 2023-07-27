from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        n1 = l1.val
        n2 = l2.val
        
        node1 = l1
        while node1.next:
            n1 = n1 + node1.next.val
            node = l1.next
        
        node2 = l2
        while node2.next:
            n2 = n2 + node2.next.val
            node2 = l2.next
        
        return n1+n2


def main():
    Solution().addTwoNumbers()


if __name__ == '__main__':
    main()
