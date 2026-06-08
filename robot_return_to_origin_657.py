from collections import Counter

class Solution:
    def judge_circle(self, moves: str) -> bool:
        counts = Counter(moves)
        return counts["U"] == counts["D"] and counts["L"] == counts["R"]

if __name__ == "__main__":
    solution = Solution()

    assert solution.judge_circle("UD") is True
    assert solution.judge_circle("LL") is False
    assert solution.judge_circle("UDLR") is True
    assert solution.judge_circle("UU") is False

    print("All tests passed!")





