'''

Hints
For each test case, for each index in the array B, find the number of ways to fill the A in such a way that A[i] <= B[i].

Edit
Keeping in mind that the sample tests are not enough, I add a third testcase:
3
3
1 2 2

Since the output should be 5, I believe that the problem statement is incorrect and the output should be 1.

Solution

1.	Remember that, 1 ≤ B[i] ≤ N.
2.	For each index i, create an array of N zeroes and henceforth call it arr
3.	Increment arr[i] by 1 and  arr[i + 1] by 1 and  arr[i + 2] by 1 and  ........... and  arr[B[i]] by 1.
4.	Keep on doing this for all i.
5.	After this, if arr[i] > B[i] then the answer is 0.
6.	Else the answer is 1.

'''