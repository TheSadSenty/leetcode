import pytest

from problems.problem_268 import Solution


@pytest.mark.parametrize(
    "input_value,expected_output",
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test_success(input_value, expected_output) -> None:
    problem_solver = Solution()
    assert problem_solver.missingNumber(input_value) == expected_output
