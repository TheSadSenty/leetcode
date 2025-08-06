from problems.problem_237 import ListNode, Solution


def test_success_1() -> None:
    root_node = ListNode(4)
    root_node.next = ListNode(5)
    root_node.next.next = ListNode(1)
    root_node.next.next.next = ListNode(9)

    problem_solver = Solution()
    problem_solver.deleteNode(root_node.next)

    assert root_node.val == 4
    assert root_node.next.val == 1
    assert root_node.next.next.val == 9
    assert root_node.next.next.next is None


def test_success_2() -> None:
    root_node = ListNode(4)
    root_node.next = ListNode(5)
    root_node.next.next = ListNode(1)
    root_node.next.next.next = ListNode(9)

    problem_solver = Solution()
    problem_solver.deleteNode(root_node.next.next)

    assert root_node.val == 4
    assert root_node.next.val == 5
    assert root_node.next.next.val == 9
    assert root_node.next.next.next is None
