'''

Note: Your code should be able to convert the sample input into the sample output. However, this is not enough to pass the challenge, because the code will be run on multiple test cases. Therefore, your code must solve this problem statement.

Solution

Approach 1: Brute Force [Time Limit Exceeded]
Intuition

Find all subsequences of the given string S and check whether each subsequence occurs exactly 2 times or not.

Algorithm

Generate all the subsequences of the given string S.

For each subsequence T, count the number of occurrences of T in S as a subsequence and return T if it occurs exactly 2 times.

Otherwise, return -1.

 

Implementation

In the following implementation, we will first generate all the subsequences of the given string S using backtracking. 

The function generateSubsequences() calls itself recursively for every index of the given string S and maintains a string temp to store current subsequence. It also maintains a set subsequences to store all the subsequences of the string S.

The function countOccurrences() returns the number of occurrences of the given string T as a subsequence in the given string S.

Complexity Analysis

Time complexity : O(2^N)O(2
​N
​​ ).
Generating all subsequences of the given string S of length N will require O(2^N)O(2
​N
​​ ) time.
Space complexity : O(2^N)O(2
​N
​​ ).
In worst case, all the characters of the string S can be used.

#include <bits/stdc++.h>
#include <string>
using namespace std;

void generateSubsequences(int index, string S, string temp, set<string> &subsequences) {
    // base case
    if (index == S.length()) {
        // If current subsequence is not empty
        if (temp.length() > 0) {
            subsequences.insert(temp);
        }
        return;
    }

    // Include current character S[index] in the subsequence
    temp.push_back(S[index]);
    generateSubsequences(index + 1, S, temp, subsequences);

    // Exclude current character S[index] in the subsequence
    temp.pop_back();
    generateSubsequences(index + 1, S, temp, subsequences);
}

int countOccurrences(string S, string T) {
    int N = S.length();
    int M = T.length();

    // T can't appear as a subsequence in S
    if (M > N) {
        return 0;
    }

    int count = 0;

    int i = 0;
    int j = 0;
    while (i < N && j < M) {
        if (S[i] == T[j]) {
            i++;
            j++;
        } else {
            i++;
        }

        // If all characters of T have been included
        if (j == M) {
            j = 0;
            count++;
        }
    }

    return count;
}

string solve(string S) {
    set<string> subsequences;
    string temp;
    generateSubsequences(0, S, temp, subsequences);

    string answer = "-1";
    for (string subsequence : subsequences) {
        if (countOccurrences(S, subsequence) == 2) {
            answer = subsequence;
            break;
        }
    }

    return answer;
}

// Driver code
int main() {
    string S = "BAB";
    cout << solve(S) << endl;

    S = "AABA";
    cout << solve(S) << endl;

    S = "AAAA";
    cout << solve(S) << endl;

    S = "AABB";
    cout << solve(S) << endl;

    return 0;
}

Approach 2: Dynamic Programming[Time Limit Exceeded]
Intuition

Instead of generating all subsequences of the given string S, we can find the answer using dynamic programming.

Algorithm

Let dp[i][j] be the count of occurrences of the string S{1...i} in the string T{1...j}.

The problem is equivalent to finding a string T that satisfies dp[N][M] = 2, where N and M denote the lengths of the strings S and T, respectively.

dp[i][j] = dp[i - 1][j], if S[i] != T[j]
dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1], if S[i] == T[j]

Complexity Analysis

Time complexity : O(N^2)O(N
​2
​​ ).
Two nested for loops are used to fill the dpdp array of size O(N^2)O(N
​2
​​ ).
Space complexity : O(N^2)O(N
​2
​​ ).
dpdp array of size O(N^2)O(N
​2
​​ ) is used.

string solve(string S) {
    int N = S.length();
    int M = N / 2;

    vector<vector<int>> dp(N + 1, vector<int>(M + 1));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= min(i, M); j++) {
            if (S[i - 1] == S[j - 1]) {
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1];
            } else {
                dp[i][j] = dp[i - 1][j];
            }
        }
    }

    string answer = "-1";
    for (int i = 1; i <= N; i++) {
        if (dp[N][i] == 2) {
            answer = S.substr(0, i);
            break;
        }
    }

    return answer;
}

Approach 3: Optimal [Accepted]
Intuition

The problem is equivalent to finding a string T that appears in S exactly twice.

If S is of odd length, the string T is not empty.
If S is of even length, the string T can be empty.

Algorithm

Iterate through all the characters of string S and use a map to store the frequency of each character.

If S is of odd length and at least one character occurs twice, return the string formed by that character.

If S is of even length, return the string formed by characters that occur exactly twice.

Complexity Analysis

Time complexity : O(N)O(N).
A single iteration over all the characters of the string S of length N is done.
Space complexity : O(N)O(N).
A map of size N is used.

string solve(string S) {
    int N = S.length();
    map<char, int> frequency;
    for (char ch : S) {
        frequency[ch]++;
    }

    bool odd = N % 2 == 1;
    string answer = "";
    for (auto &pair : frequency) {
        char ch = pair.first;
        int count = pair.second;
        if (count == 2) {
            answer += ch;
        } else if (count > 2) {
            if (odd && count % 2 == 1) {
                answer += ch;
            } else if (!odd) {
                answer += ch;
            }
        }
    }

    if (answer == "") {
        answer = "-1";
    }

    return answer;
}

Approach 4: Optimal [Accepted]
Intuition

If a character appears exactly once in the given string S, the string T can't contain this character.

Algorithm

The problem is equivalent to finding the string T formed by characters that appear exactly once in the given string S.

Iterate through all the characters of string S and use a map to store the frequency of each character.

Return the string formed by characters that appear exactly once in the given string S.

Complexity Analysis

Time complexity : O(N)O(N).
A single iteration over all the characters of the string S of length N is done.
Space complexity : O(N)O(N).
A map of size N is used.

string solve(string S) {
    int N = S.length();
    map<char, int> frequency;
    for (char ch : S) {
        frequency[ch]++;
    }

    string answer = "";
    for (auto &pair : frequency) {
        char ch = pair.first;
        int count = pair.second;
        if (count == 1) {
            answer += ch;
        }
    }

    if (answer == "") {
        answer = "-1";
    }

    return answer;
}

Approach 5: Optimal [Accepted]
Intuition

The problem is equivalent to finding a string T that appears in S exactly twice.

If S is of odd length, the string T is not empty.
If S is of even length, the string T can be empty.

Algorithm

Iterate through all the characters of string S and use a map to store the frequency of each character.

If S is of odd length and at least one character occurs twice, return the string formed by that character.

If S is of even length, return the string formed by characters that occur exactly twice.

Complexity Analysis

Time complexity : O(N)O(N).
A single iteration over all the characters of the string S of length N is done.
Space complexity : O(N)O(N).
A map of size N is used.

string solve(string S) {
    int N = S.length();
    map<char, int> frequency;
    for (char ch : S) {
        frequency[ch]++;
    }

    string answer = "";
    for (char ch = 'A'; ch <= 'B'; ch++) {
        int count = frequency[ch];
        if (count == 2) {
            answer += ch;
        } else if (count > 2) {
            if (N % 2 == 1 && count % 2 == 1) {
                answer += ch;
            } else if (N % 2 == 0) {
                answer += ch;
            }
        }
    }

    if (answer == "") {
        answer = "-1";
    }

    return answer;
}

Analysis written by: @vinod23

'''