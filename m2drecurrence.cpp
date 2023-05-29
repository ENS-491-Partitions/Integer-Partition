#include <iostream>
#include "bigint.h"
#include <string>
using namespace std;

const Dodecahedron::Bigint ZERO = 0;
const Dodecahedron::Bigint SENTINEL = -1;

Dodecahedron::Bigint rec(int n, int m, vector<vector<Dodecahedron::Bigint>>& bases, const vector<vector<int>>& constants, int degree_n, int degree_m) {
	if (!(bases[n][m] == SENTINEL)) {
		return bases[n][m];
	}
	Dodecahedron::Bigint result = 0;
	for (int i = degree_n; i >= 0; i--) {
		for (int j = degree_m; j >= 0; j--) {
			if (!(i == 0 && j == 0)) {
				Dodecahedron::Bigint previous = rec(n - i, m - j, bases, constants, degree_n, degree_m);
				Dodecahedron::Bigint constant = constants[i][j];
				result += constant * previous;
			}
		}
	}
	bases[n][m] = result;
	return bases[n][m];
}

Dodecahedron::Bigint m2d_recurrence(int n, int m, int degree_n, int degree_m) {
	vector <vector<Dodecahedron::Bigint>> bases(n + 1, vector<Dodecahedron::Bigint>(m + 1, SENTINEL));
	vector <vector<int>> constants(degree_n + 1, vector<int>(degree_m + 1, 0));
	cout << "Please enter the constants" << endl;
	for (int i = 0; i <= degree_n; i++) {
		for (int j = 0; j <= degree_m; j++) {
			if (!(i == 0 && j == 0)) {
				int constant = 0;
				cout << "C(" << i << "," << j << "): ";
				cin >> constant;
				constants[i][j] = constant;
			}
		}
	}
	int num_base = ((n + 1) * degree_m) + ((m + 1) * degree_n) - (degree_n * degree_m);
	cout << "Please enter the base cases of your recurrence!" << endl;
	cout << "Note you need to enter " << num_base << " terms" << endl;
	for (int i = 0; i <= n; i++) {
		if (i < degree_n) {
			for (int j = 0; j <= m; j++) {
				int term = 0;
				cout << "R(" << i << "," << j << "): ";
				cin >> term;
				bases[i][j] = term;
			}
		}
		else {
			for (int j = 0; j < degree_m; j++) {
				int term = 0;
				cout << "R(" << i << "," << j << "): ";
				cin >> term;
				bases[i][j] = term;
			}
		}
	}
	rec(n, m, bases, constants, degree_n, degree_m);
	for (int i = 0; i <= n; i++) {
		for (int j = 0; j <= m; j++) {
			cout << "R(" << i << "," << j << "): " << bases[i][j] << endl;
		}
	}
	return bases[n][m];
}


int main() {
	int degree_n, degree_m;
	cout << "Please enter the degrees of your recurrence, in the format n_degree m_degree: ";
	cin >> degree_n >> degree_m;
	int cases = 0;
	int n, m;
	cout << "Please enter n and m: ";
	cin >> n >> m;
	m2d_recurrence(n, m, degree_n, degree_m);
	return 0;
}