""" 
Problem
<https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/largest-number-10-ca319b09/>
Given an integer which has N digits. 
You have to delete exactly K digits in integer.

Find out the largest possible number which can be built from 
after removing exactly digits.

Sample Input
3412 1

Sample Output
412
"""

from decimal import *

try:
    my_input = input()
except EOFError:
    pass

my_input_li = my_input.split()
n = int(my_input_li[0])
k = int(my_input_li[1])
#print(n, k)
for j in range(k):
    ans = 0
    i = 1
    while (int(n / i) > 0): 
        temp_n = int(n/(i*10))*i+(n % i)
        i = i*10
        ans = max(ans, temp_n)
    n = int(ans)
    #print(n)

    
print(n)