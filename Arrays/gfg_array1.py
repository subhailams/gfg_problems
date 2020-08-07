'''
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum

Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of two lines. The first line of each test case is N and S, where N is the size of array and S is the sum. The second line of each test case contains N space separated integers denoting the array elements.

Output:
For each testcase, in a new line, print the starting and ending positions(1 indexing) of first such occuring subarray from the left if sum equals to subarray, else print -1.

Constraints:
1 <= T <= 100
1 <= N <= 107
1 <= Ai <= 1010

Example:
Input:
2
5 12
1 2 3 7 5
10 15
1 2 3 4 5 6 7 8 9 10
Output:
2 4
1 5

Explanation :
Testcase1: sum of elements from 2nd position to 4th position is 12
Testcase2: sum of elements from 1st position to 5th position is 15
'''

#### Code ####

t = int(input())
arr=[]
for k in range(t):
    n,s = map(int,input().split())
    arr = list(map(int,input().split()))
    
    sum_dict = {}
    curr_sum = 0
    for i in range(0,n):
    	curr_sum = curr_sum + arr[i]
    	if curr_sum == s:
    	    print(sum_dict)
    	    print("Sum found between indexes 0 to", i)
    	    break
    	if (curr_sum - s) in sum_dict:
    	    print(sum_dict)
    	    print("Sum found between indexes ", sum_dict[curr_sum - s] + 1, "to", i)
    	    break
    	sum_dict[curr_sum] = i
    	print(sum_dict)
