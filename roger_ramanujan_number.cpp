#include <iostream>
#include <vector>
#include <iomanip>
#include "bigint.h"


using namespace std;

Dodecahedron::Bigint RogerR(int n, int m, vector<vector<Dodecahedron::Bigint>>& RRterms) {
	if (n == 0 && m == 0) {
		return 1;
	}
	if (n < 0 || m < 0) {
		return 0;
	}
	if (n == 0 || m == 0) {
		return 0;
	}
	if (m == 1) {
		return 1;
	}
	if (RRterms[n][m] != -1) {
		return RRterms[n][m];
	}
	int previous = n - (2 * m) + 1;
	Dodecahedron::Bigint result = RogerR(previous, m - 1, RRterms) + RogerR(n - m, m, RRterms);
	RRterms[n][m] = result;
	return result;
}

Dodecahedron::Bigint mRogerR(int n, int m) {
	vector<vector<Dodecahedron::Bigint>> RRterms;
	for (int i = 0; i <= n; i++) {
		Dodecahedron::Bigint sentinel = -1;
		vector<Dodecahedron::Bigint> temp(m + 1, sentinel);
		RRterms.push_back(temp);
	}
	Dodecahedron::Bigint result = RogerR(n, m, RRterms);
	return result;
}

void PrintRR(int n, int m) {
	vector<vector<Dodecahedron::Bigint>> RRterms;
	for (int i = 0; i <= n; i++) {
		Dodecahedron::Bigint sentinel = -1;
		vector<Dodecahedron::Bigint> temp(m + 1, sentinel);
		RRterms.push_back(temp);
	}
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= m; j++) {
			Dodecahedron::Bigint num = RogerR(i, j, RRterms);
			cout << "RR(" << i << "," << j << "): " << num << endl;
		}
	}

}

int main() {
	int n, m;
	cout << "Please enter the integer, n, and the number of parts, m: ";
	cin >> n >> m;
	cout << "The integer " << n << " has " << mRogerR(n,m) << " Roger Ramanujan partitions of the first kind into " << m << " parts" << endl;
	PrintRR(n, m);
	return 0;
}