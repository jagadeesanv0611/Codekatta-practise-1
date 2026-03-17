# 4. Next Greater Power of 2
# Question:
# Given a number N, find its next immediate greater power of 2(i.e 2^1, 2^2, 2^3...).

# Input Description:
# The input consists of a number N where N <= 1000.

# Sample Input:
# 4
# Sample Output:
# 8

N = int(input())
if N <= 1000:
    n = 0
    while 2 ** n <= N:
        if 2 ** n == N:
            print(2 * N)
            break
        n += 1
    else:
        print(2 ** n)
else:
    pass