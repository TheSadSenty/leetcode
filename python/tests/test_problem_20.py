import pytest

from problems.problem_20 import Solution


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("([)]", False),
        ("[", False),
    ],
)
def test_success(input_value, expected_output) -> None:
    problem_solver = Solution()
    assert problem_solver.isValid(input_value) == expected_output
