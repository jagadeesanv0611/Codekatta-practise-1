# 7. Number Range Check

# Question:
# Given 3 numbers N , L and R. Print 'yes' if N is between L and R else print 'no'.

# Sample Input:
# 3
# 2 6
# Sample Output:
# yes

N = int(input())
L, R = map(int, input().split())
if (N > L and N < R) or (N < L and N > R):
    print("yes")
else:
    print("no")