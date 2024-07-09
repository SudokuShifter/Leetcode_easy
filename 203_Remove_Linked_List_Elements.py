from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return None

        new_head = ListNode(0)
        new_head.next = head

        current = new_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return new_head.next