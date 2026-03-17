# 5. Palindrome Check

# Problem Statement:
# Given a string S, print 'yes' if it is a palindrome or 'no' if it is not a palindrome.

# Sample Input:
# lappal
# Sample Output:
# yes

S = input()
rev_S = S[::-1]
if S == rev_S:
    print("yes")
else:
    print("no")