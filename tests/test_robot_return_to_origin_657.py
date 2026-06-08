from src.robot_return_to_origin_657 import Solution

solution = Solution()


def test_returns_true_for_up_down():
    solution = Solution()
    assert solution.judge_circle("UD") is True


def test_returns_false_for_two_lefts():
    solution = Solution()
    assert solution.judge_circle("LL") is False


def test_returns_true_for_balanced_all_directions():
    solution = Solution()
    assert solution.judge_circle("UDLR") is True


def test_returns_false_for_unbalanced_vertical():
    solution = Solution()
    assert solution.judge_circle("UUD") is False


def test_returns_false_for_unbalanced_horizontal():
    solution = Solution()
    assert solution.judge_circle("RRRL") is False
