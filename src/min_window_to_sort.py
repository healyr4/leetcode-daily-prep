# Task
# Given an integer array, return the smallest continuous subarray which, if sorted, would make the entire array sorted.
# Input:  [1, 2, 6, 5, 5, 8, 9]
# Output: [2, 4]
#
# The subarray from index 2 to 4 is [6, 5, 5].
#
# Requirements:
#
# Return [-1, -1] if the array is already sorted.
# Aim for O(n) time and O(1) extra space.
# Explain how duplicates affect your solution.

test_case = [1, 2, 6, 5, 5, 8, 9]


def get_boundaries(test_case: list)-> tuple[int | None, int | None]:
    left_bound = None
    right_bound = None
    for i in range(len(test_case) - 1):
        curr_val = test_case[i]
        next_val = test_case[i + 1]
        if curr_val <= next_val:
            continue
        else:
            left_bound = i
            break
    if left_bound is None:
        return None, None
    for j in range(len(test_case) - 1, 0, -1):
        if test_case[j] < test_case[j - 1]:
            right_bound = j
            break

    return left_bound, right_bound


def get_min_max_of_subarray(test_case, lb, rb):
    subarray_min = min(test_case[lb : rb + 1])
    subarray_max = max(test_case[lb : rb + 1])
    return subarray_min, subarray_max


def expand_bounds(test_case, lb, rb, subarray_min, subarray_max):
    while lb > 0 and test_case[lb - 1] > subarray_min:
        lb -= 1

    while rb < len(test_case) - 1 and test_case[rb + 1] < subarray_max:
        rb += 1
    return lb, rb


def main():
    left_bound, right_bound = get_boundaries(test_case)
    if left_bound is None:
        return [-1, -1]
    subarray_min, subarray_max = get_min_max_of_subarray(
        test_case, left_bound, right_bound
    )
    left_bound_final, right_bound_final = expand_bounds(
        test_case, left_bound, right_bound, subarray_min, subarray_max
    )
    print([left_bound_final, right_bound_final])
    return [left_bound_final, right_bound_final]


if __name__ == "__main__":
    main()
