"""
Problem
You are given an array A consisting of N integers. 

Task
Print the sum of the elements in the array. 

Sample Input
5
1000000001 1000000002 1000000003 1000000004 1000000005

Sample Output
5000000015
"""




#name = input()                  # Reading input from STDIN
name1=[]
#print('Hi, %s.' % name)         # Writing output to STDOUT
 
 
try:
    namesize=input()
    pass
    name=input()
    name=name.split()
    #print(name)
    name1.extend(name)
    #print(name1)
except EOFError:
    pass
name1=[int(i) for i in name1]
print(sum(name1))
 