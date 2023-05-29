#include <iostream>
#include "bigint.h"
#include <vector>

using namespace std;

Dodecahedron::Bigint RogerRG(int n, int m, int k, int a, vector<vector<vector<Dodecahedron::Bigint>>>& RRGterms) {
	if (a == 0) {
		return 0;
	}
	if (n == 0 && m == 0) {
		return 1;
	}
	if (n < 0 || m < 0) {
		return 0;
	}
	if (n == 0 || m == 0) {
		return 0;
	}
	if (RRGterms[a][n][m] != -1) {
		return RRGterms[a][n][m];
	}
	Dodecahedron::Bigint result = RogerRG(n, m, k, a-1, RRGterms);
	result += RogerRG(n - m, m - a + 1, k, k-a+1, RRGterms);
	RRGterms[a][n][m] = result;
	return result;
}

Dodecahedron::Bigint mRogerRG(int n, int m, int k, int a) {
	if (k < 2) {
		return -1;
	}
	vector<vector<vector<Dodecahedron::Bigint>>> RRGterms;
	vector<vector<Dodecahedron::Bigint>> proto;
	for (int i = 0; i <= n; i++) {
		Dodecahedron::Bigint sentinel = -1;
		vector<Dodecahedron::Bigint> temp(m + 1, sentinel);
		proto.push_back(temp);
	}
	for (int i = 0; i <= k; i++) {
		vector<vector<Dodecahedron::Bigint>> temp;
		temp = proto;
		RRGterms.push_back(temp);
	}
	Dodecahedron::Bigint result = RogerRG(n, m, k, a, RRGterms);
	return result;
}

int main() {
	int n, m, k, a;
	cout << "Please enter the integer whose partitions you want to generate: ";
	cin >> n;
	cout << "Please enter the number of parts: ";
	cin >> m;
	cout << "Please enter the constraint k: ";
	cin >> k;
	cout << "Please enter the constraint a: ";
	cin >> a;
	cout << "There are " << mRogerRG(n, m, k, a) << " partitions of " << n << " into " << m << " parts for k = " << k << " and a = " << a << endl;
	return 1;
}