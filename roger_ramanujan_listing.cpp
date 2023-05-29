#include <iostream>
#include <vector>
#include "bigint.h"
#include <cmath>
using namespace std;

int nextPart(int n, int m, int max) {
	int square = pow(m - 1, 2);
	int result = n - square;
	if (result > max) {
		return max;
	}
	return result;
}


void ListRRPartitions(int n, int m) {
	int rootN = sqrt(n);
	if (rootN < m) {
		cout << "There are no such partitions" << endl;
		return;
	}
	Dodecahedron::Bigint count = 1;
	vector<int> partition (m + 1, 0);
	int pastSum = 0;
	int previousTerm = 0;
	for (int i = 1; i <= m; i++) {
		int result = 0;
		if (i == 1) {
			result = nextPart(n, (m + 1) - i, n);
		}
		else {
			result = nextPart(n-pastSum, (m + 1) - i, previousTerm-2);
		}
		partition[i] = result;
		previousTerm = result;
		pastSum += result;
	}
	for (int i = 1; i <= m; i++) {
		cout << partition[i] << " ";
	}
	cout << endl;
	while ((partition[1] - partition[m]) > ((2 * (m - 1)) + 1)) {
		count = count + 1;
		int sum = partition[m];
		int i = 1;
		int difference = partition[m - i] - partition[m];
		sum += partition[m - i];
		while (difference <= ((2 * i) + 1)) {
			i++;
			sum += partition[m - i];
			difference = partition[m - i] - partition[m];
		}
		int max = partition[m-i]-1;
		while (i >= 0) {
			partition[m - i] = nextPart(sum, i + 1, max);
			sum -= partition[m-i];
			max = partition[m - i] - 2;
			i--;
		}
		for (int j = 1; j <= m; j++) {
			cout << partition[j] << " ";
		}
		cout << endl;

	}
	cout << "There are " << count << " 2-distinct partitions of " << n << " into " << m << " parts" << endl;
}

void ListAllRRPartitions(int n) {
	int maxM = sqrt(n);
	for (int i = maxM; i > 0; i--) {
		ListRRPartitions(n, i);
	}
}


int main() {
	int n, m;
	cout << "Please enter the integer whose partitions you want to generate: ";
	cin >> n;
	cout << "Please enter the number of parts: ";
	cin >> m;
	ListRRPartitions(n,m);
	cout << "Done" << endl;
	return 0;
}