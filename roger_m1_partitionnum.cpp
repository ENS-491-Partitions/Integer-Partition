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

	// calculate the number of partitions

	if (m == 1) {
		cout << "The number n has total 1 partition when m = 1." << endl;
	}
	else if (m > 1) {

		// total number of partitions when m > 1

	}

	return 0;
}