'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

Input:
The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

Output:
Print the maximum sum of the contiguous sub-array in a separate line for each test case.

Constraints:
1 ≤ T ≤ 110
1 ≤ N ≤ 106
-107 ≤ A[i] <= 107

Example:
Input
2
5
1 2 3 -2 5
4
-1 -2 -3 -4
Output
9
-1

Explanation:
Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
'''
#code
t = int(input())

for k in range(t):
    n = int(input())
    arr = list( map(int,input().split()))
    max_so_far = arr[0] 
    curr_max = arr[0]
    
    for i in range(1,n):
        curr_max = max(arr[i], curr_max + arr[i])
        max_so_far = max(max_so_far,curr_max) # to handle if all are -ve
                    # curr_max = -2    (-2, -1-2)
                    # curr_max = -3    (-3, -2-3)
                    # curr_max = -4    (-4, -3-3)            
                                    
        
    print(max_so_far)