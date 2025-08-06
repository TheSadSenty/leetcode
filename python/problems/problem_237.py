# Definition for singly-linked list.
from typing import Any, Self


class ListNode:
    val: Any
    next: Self | None

    def __init__(self, x) -> None:
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
