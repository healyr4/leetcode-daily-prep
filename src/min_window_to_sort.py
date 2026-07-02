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

def main():
    left_bound = 0
    right_bound = 0
    for i in range(len(test_case)-1):
        curr_val = test_case[i]
        next_val = test_case[i+1]
        if curr_val <= next_val:
            continue
        else:
            left_bound = i
            break
    for j in range(len(test_case)-1, 0, -1):
        if test_case[j] < test_case[j-1]:
            right_bound = j
            break

    print(left_bound, right_bound)





if __name__ == '__main__':
    main()