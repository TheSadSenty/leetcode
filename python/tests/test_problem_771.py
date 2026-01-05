from problems.problem_771 import Solution
import pytest


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (["aA", "aAAbbbb"], 3),
        (["z", "ZZ"], 0),
    ],
)
def test_success(input_value, expected_output) -> None:
    jewels, stones = input_value
    problem_solver = Solution()
    assert problem_solver.numJewelsInStones(jewels, stones) == expected_output
