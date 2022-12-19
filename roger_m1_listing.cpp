#include <iostream>
#include <string>
#include "bigint.h"

using namespace std;

int main() {
	int n, m;

	cout << "Please enter the number n: " << endl;
	cin >> n;
	cout << "Please enter the number of of parts n should have: " << endl;
	cin >> m;

	// list all the partitions

	if (m == 1) {
		cout << "The partitions of n when m = 1:" << endl;
		cout << n << endl;
	}
	else if (m > 1) {

		// all partitions when m > 1

	}

	return 0;
}