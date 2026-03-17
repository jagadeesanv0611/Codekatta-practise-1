# 2. Prime Number Check

# Problem Statement:
# Given a number N, check whether it is prime or not. Print 'yes' if it is prime else print 'no'.

# Input Description:
# The input consists of a single integer N.

# Output Description:
# The output is 'yes' if N is prime, otherwise 'no'.

# Sample Input:
# 123
# Sample Output:
# no

N = int(input())                       #inputs only one input is 843
if N <= 1:
       print("no")
else:
        Sq_rt = int(N**0.5)
        for i in range(2, Sq_rt + 1):
            if N % i == 0:
               print("no")
               break    
        else:
            print("yes")             #output is no