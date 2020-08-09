'''
You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

Input :
The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. Each test case consists of three lines. The first line of each test case contains an integer N denoting size array. Then in the next line are N space separated values of the array A. The last line of each test case contains two integers  x and y.

Output :
Print the minimum index based distance between x and y.

Your Task:
Complete the function minDist() which takes the array, n, x and y as input parameters and returns the minimum distance between x and y in the array. If no such distance is possible then return -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= T <= 100
1 <= N <= 105
0 <= A[i], x, y <= 105

Example:
Sample Input:
2
4
1 2 3 2
1 2
7
86 39 90 67 84 66 62 
42 12

Sample Output:
1
-1

Explanation:
Testcase1: x = 1 and y = 2. There are two distances between x and y, which are 1 and 3 out of which the least is 1.
Testcase2: x = 42 and y = 12. We return -1 as x and y don't exist in the array.
'''

import sys

def minDist(arr, n, x, y):
    # Code here
    
    INT_MAX = sys.maxsize
    min_dist = INT_MAX

    # # Method 1 O(n^2)
    
    # for i in range(n): 
    #     for j in range(i + 1, n): 
    #         if (x == arr[i] and y == arr[j] or
    #         y == arr[i] and x == arr[j]) and abs(i-j) < min_dist: 
    #             min_dist = abs(i-j) 
    
    # if(min_dist == INT_MAX): 
    #   return -1
      
    # return min_dist
    
    # Method 2 O(n)
    
    prev_elem = -1
    i = 0
    for i in range(n):
        
        if(arr[i] ==x or arr[i] == y):
            
            if(arr[i] != arr[prev_elem] and prev_elem != -1):
                min_dist = min(min_dist,i - prev_elem)
            
            prev_elem = i
          
      
    #If distance is equal to int max  
    if(min_dist == INT_MAX): 
      return -1
       
    return min_dist 
    
