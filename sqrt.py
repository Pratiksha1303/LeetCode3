# LEETCODE


# class Solution(object):
#     def mySqrt(self, x):
#         if x < 2:  # 0 and 1 are their own square roots
#             return x

#         left = 1
#         right = x // 2
#         result = 0

#         while left <= right:
#             mid = (left + right) // 2
#             if mid * mid == x:
#                 return mid  # perfect square
#             elif mid * mid < x:
#                 result = mid  # store the best answer so far
#                 left = mid + 1
#             else:
#                 right = mid - 1

#         return result


def mySqrt(x):
    if x < 2:  # 0 and 1 are their own square roots
        return x

    left = 1
    right = x // 2
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid  # perfect square
        elif mid * mid < x:
            result = mid  # store the best answer so far
            left = mid + 1
        else:
            right = mid - 1

    return result

# Test
print(mySqrt(4))  # Output: 2

