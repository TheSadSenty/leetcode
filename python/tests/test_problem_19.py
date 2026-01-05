from problems.problem_19 import ListNode, Solution


def test_success_1() -> None:
    root_node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

    problem_solver = Solution()
    new_root_node = problem_solver.removeNthFromEnd(root_node, 2)

    assert new_root_node
    assert new_root_node.val == 1

    assert new_root_node.next
    assert new_root_node.next.val == 2

    assert new_root_node.next.next
    assert new_root_node.next.next.val == 3

    assert new_root_node.next.next.next
    assert new_root_node.next.next.next.val == 5


def test_success_2() -> None:
    root_node = ListNode(1)

    problem_solver = Solution()
    new_root_node = problem_solver.removeNthFromEnd(root_node, 1)

    assert new_root_node is None


def test_success_3() -> None:
    root_node = ListNode(1, ListNode(2))

    problem_solver = Solution()
    new_root_node = problem_solver.removeNthFromEnd(root_node, 1)

    assert new_root_node
    assert new_root_node.val == 1
    assert new_root_node.next is None
