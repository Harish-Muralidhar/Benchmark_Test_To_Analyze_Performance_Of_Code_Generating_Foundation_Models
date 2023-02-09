
Explanation
In the example, the smallest partial sum modulo P that is at least K is
2.



#### Solution:

```python
import sys
lines = sys.stdin.readlines()

n, k, p = map(int, lines[0].split())

array = [0]*n

for i in range(n):
    array[i] = int(lines[i+1])

partial_sum = 0

index = 0
min_index = 0

for i in range(n):
    partial_sum += array[i]

    while (partial_sum >= k):
        if partial_sum % p < array[index] % p:
            min_index = index + 1
        partial_sum -= array[index]
        index += 1

    if partial_sum % p == 0 and partial_sum >= k:
        print(partial_sum % p)
        break

if partial_sum % p != 0:
    print(partial_sum % p)
```

## Problem 7:

### Problem Statement:

You have been given an array A of size N. You need to print the total sum of the elements of the array.

### Constraints:

- 1 <= N <= 100
- 1 <= a[i] <= 100

### Input Format:

The first line of the input consists of a single integer N denoting the size of the array. The next line consists of N space separated integers denoting the elements of the array

### Output Format:

Print the total sum of the elements of the array

### Example:

#### Sample Input:

```
6
1 2 3 4 10 11
```

#### Sample Output:

```
31
```

#### Solution:

```python
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
```

## Problem 8:

### Problem Statement:

You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

### Constraints:

- The length of the string will not exceed 1000.

### Input Format:

The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

### Output Format:

Print the required answer on a single line.

### Example:

#### Sample Input:

```
aba
```

#### Sample Output:

```
YES
```

#### Solution:

```python
s = input()
print("YES" if s == s[::-1] else "NO")
```

## Problem 9:

### Problem Statement:

You have been given an array A of size N. You need to sort this array non-decreasing oder using bubble sort. However, you do not need to print the sorted array. You just need to print the number of swaps required to sort this array using bubble sort.

### Constraints:

- 1 <= N <= 100
- 1 <= a[i] <= 100

### Input Format:

The first line consists of a single integer N denoting size of the array. The next line contains N space separated integers denoting the elements of the array.

### Output Format:

Print the required answer in a single line

### Example:

#### Sample Input:

```
3
3 2 1
```

#### Sample Output:

```
3
```

#### Solution:

```python
n = int(input())
a = list(map(int, input().split()))
count = 0
for _ in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            count += 1
print(count)
```

## Problem 10:

### Problem Statement:

You have been given an integer N. You need to find and print the factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

### Constraints:

- 1 <= N <= 100

### Input Format:

The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

### Output Format:

Output a single line denoting the factorial of the number N.

### Example:

#### Sample Input:

```
2
```

#### Sample Output:

```
2
```

#### Solution:

```python
n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)
```