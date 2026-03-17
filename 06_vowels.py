# 6. Vowel Check in String

# Given a string S, print 'yes' if it has a vowel in it else print 'no'.

# Sample Input:
# codekata
# Sample Output:
# yes

letter = input()
for ch in letter:
    if ch.lower() in "aeiou":
        print("yes")
        break
else:
    print("no")