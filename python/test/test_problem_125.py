import pytest

from problems.problem_125 import Solution


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".,", True),
    ],
)
def test_success(input_value, expected_output) -> None:
    problem_solver = Solution()
    assert problem_solver.isPalindrome(input_value) == expected_output
