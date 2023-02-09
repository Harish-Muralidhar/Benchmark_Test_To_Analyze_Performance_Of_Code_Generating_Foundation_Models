'''

Explanation
Input example #1
Let's consider the following shuffles:

(2, 1) -> (2, 1) // this is the first shuffle
(1, 2) -> (1, 2) // this is the second shuffle

Then the algorithm will complete sorting.

Input example #2
Let's consider the following shuffles:

(6, 5, 4, 3, 2, 1) -> (4, 3, 5, 1, 2, 6) // this is the first shuffle
(4, 3, 1, 5, 2, 6) -> (4, 3, 1, 5, 2, 6) // this is the second shuffle
(1, 4, 3, 5, 2, 6) -> (1, 3, 4, 5, 2, 6) // this is the third shuffle
(3, 1, 4, 5, 2, 6) -> (3, 1, 4, 5, 2, 6) // this is the forth shuffle
(1, 3, 4, 5, 2, 6) -> (1, 3, 4, 5, 2, 6) // this is the fifth shuffle
(1, 2, 3, 4, 5, 6) -> (1, 2, 3, 4, 5, 6) // this is the sixth shuffle

Then the algorithm will complete sorting.

Input example #3
Let's consider the following suffles:

(10, 9, 8, 7, 6, 5, 4, 3, 2, 1) -> (5, 3, 9, 2, 8, 4, 10, 1, 6, 7) // this is the first shuffle
(5, 2, 3, 9, 8, 4, 10, 1, 6, 7) -> (5, 2, 3, 8, 4, 9, 10, 1, 6, 7) // this is the second shuffle
(5, 2, 3, 4, 8, 9, 10, 1, 6, 7) -> (5, 2, 3, 4, 1, 9, 10, 8, 6, 7) // this is the third shuffle
(5, 2, 3, 4, 1, 9, 10, 6, 8, 7) -> (5, 2, 3, 4, 1, 6, 10, 8, 9, 7) // this is the fourth shuffle
(5, 2, 3, 4, 1, 6, 8, 10, 9, 7) -> (5, 2, 3, 4, 1, 6, 8, 7, 9, 10) // this is the fifth shuffle
(5, 2, 3, 1, 4, 6, 8, 7, 9, 10) -> (5, 2, 3, 1, 4, 6, 7, 8, 9, 10) // this is the sixth shuffle
(5, 2, 1, 3, 4, 6, 7, 8, 9, 10) -> (5, 2, 1, 3, 4, 6, 7, 8, 9, 10) // this is the seventh shuffle
(5, 2, 1, 3, 4, 6, 7, 8, 9, 10) -> (5, 2, 1, 3, 4, 6, 7, 8, 9, 10) // this is the eighth shuffle
(5, 2, 1, 3, 4, 6, 7, 8, 9, 10) -> (5, 2, 1, 3, 4, 6, 7, 8, 9, 10) // this is the ninth shuffle
(5, 2, 1, 3, 4, 6, 7, 8, 9, 10) -> (5, 2, 1, 3, 4, 6, 7, 8, 9, 10) // this is the tenth shuffle

Then the algorithm will complete sorting.

Note
In the first example the expected amount of shuffles is 2 because we get two random permutations of sequence (2, 1) on each shuffle.

In the second example the expected amount of shuffles is 1826/189 = 9.82879791... The only shuffles that are not optimal are the first and the second one. The first one is optimal with the probability 2/6 because 2 and 6 are in the right places. The second one is optimal with the probability 3/6.

In the third example the expected amount of shuffles is 877318/35343 = 24.89359425... The optimal shuffles are the first, the second, the third, the fourth, the sixth and the tenth with the probability 1/3, 2/4, 3/5, 4/6, 5/7 and 10/10 respectively.

Input
6
2
6
8
10
14
20

Output
2
1826/189
4320/225
877318/35343
2416/105
1575/64

Input
5
5
10
15
20
25

Output
4
46/3
2346/105
7226/225
1216/35

Input
3
3
7
10

Output
3
49/8
6516/315

Input
10
2
3
4
5
6
7
8
9
10
11
12

Output
2
3
8
20
44
92
180
322
522
780

Input
1
12

Output
780

Input
3
3
7
10

Output
3
49/8
6516/315

Input
10
2
3
4
5
6
7
8
9
10
11
12

Output
2
3
8
20
44
92
180
322
522
780

Input
1
10

Output
877318/35343

Input
5
2
6
8
10
14
20

Output
2
1826/189
4320/225
877318/35343
2416/105

'''