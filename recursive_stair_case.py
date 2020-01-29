"""
There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
"""

# following two solutiuon only if x = 1,2 means can climb one or two steps at a time.

# def count_ways(n):  #recursive way and not optimised. only works till n=8
#     if n == 0 or n == 1: return 1
#     result = []
#     result.append(1)
#     result.append(1)


#     for i in range(n):
#         result = count_ways(n-1) + count_ways(n-2)
    
#     return result

# print count_ways(10)


def count_ways_by_dp(n):  #via dp called as botton up approach
    if n == 0: return 1
    result = []
    result.append(1)
    result.append(1)

    for i in range(2, n+1):
        result.append(result[-1] + result[-2])
        result.pop(0)
    # print result
    return result[-1]

print count_ways_by_dp(10)



# # solution where the x can be [1, 3, 5] or can be any number.
def count_ways_by_dp(n, x):
    if n == 0: return 1
    result = []
    result.append(1)
    result.append(1)

    for i in range(2, n+1):
        sum = 0
        for j in x:
            if i-j>=0:
                sum += result[-j]
        result.append(sum)
    result.pop(0)
    return result[-1]

print count_ways_by_dp(10, [1,2])
