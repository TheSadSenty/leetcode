from problems.problem_53 import Solution
import pytest


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ],
)
def test_success(input_value, expected_output) -> None:
    problem_solver = Solution()
    assert problem_solver.maxSubArray(input_value) == expected_output
