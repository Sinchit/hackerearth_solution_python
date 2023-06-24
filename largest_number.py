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
try:
    my_input=input()
    #print(my_input)
except EOFError:
    pass
 
my_input_li=my_input.split()
#print("my_input_li ",my_input_li)
no=my_input_li[0]
# print("no ", no)
# print("len(no) ",len(no)  )
# print("int(my_input_li[1]) ",int(my_input_li[1])  )
len_allow=len(no)-int(my_input_li[1])
#print("len_allow ", len_allow)
 
max_no1=0
#len(no)
for i in range(len(no)):
    max_no=no[i]
    for j in range(i+1,len(no)):
        if len(max_no)<len_allow:
                max_no=max_no+no[j]
                #print("max_no : ",max_no)
                #print("max_no1 ", max_no1)
                if max_no1<int(max_no):
                    max_no1=int(max_no)
                    #print("max_no1 : ",max_no1)
 
print(max_no1)
