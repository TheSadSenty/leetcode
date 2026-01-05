# Definition for singly-linked list.

from typing import Any, Self


# Definition for singly-linked list.
class ListNode:
    val: Any
    next: Self | None

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        res = ListNode(0, head)
        dummy = res

        for _ in range(n):
            head = head.next

        while head:
            head = head.next
            dummy = dummy.next

        dummy.next = dummy.next.next

        return res.next
