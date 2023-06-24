"""
Problem
A zoo have two types of creatures, type A has 
 hands and type B has 
 hands. Spawn the smallest number of creatures so they can grab each other hands in the following conditions:

Each creature should only grab the hands of another creature type.
Each creature should grab with all of its hands.
What is the smallest number of creature needed?

Note: It is guaranteed that under the given conditions answer is unique.

Sample Input
1
20 2
Sample Output
1 10
"""  

import math  

def main():
    try:
        no_test_case=int(input())
        pass
        for i in range(no_test_case):
            input1=input()
            input1=input1.split()
            a=float(input1[0])
            b=float(input1[1])
            lcm_result=lcm(a,b)
            #print(lcm_result)
            print(int(round(lcm_result/a,0)),int(round(lcm_result/b,0)))
            
    except EOFError:
        pass

def lcm(a,b):
    min_no=min(a,b)
    hcf = gcd(a,b)
    return (a*b)/hcf

def gcd(a,b):
    if (b == 0):
        return a;
    return gcd(b, a % b);


if __name__ == '__main__':
    #print(math.ceil(0.001))
    main()

 