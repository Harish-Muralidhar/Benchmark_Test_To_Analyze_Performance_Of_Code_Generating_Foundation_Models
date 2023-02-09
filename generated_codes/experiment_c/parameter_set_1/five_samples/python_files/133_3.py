'''
 pairs.
Case 4 : N = 6. No matter which pair Arjuna makes first, Bhima can always make one more pair, and Arjuna can make one more pair ( without crossing the pair made by Bhima ).
'''
'''
#include <iostream>
#include <string>
using namespace std;

void main() {
	int T, N;
	cin >> T;
	string winner[10000];
	for (int i = 0; i < T; i++) {
		cin >> N;
		if (N % 2 == 0) {
			winner[i] = "Bhima";
		}
		else {
			winner[i] = "Arjuna";
		}
	}

	for (int i = 0; i < T; i++) {
		cout << winner[i] << endl;
	}
}
'''