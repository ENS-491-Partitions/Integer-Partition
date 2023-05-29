#include <iostream>
#include "bigint.h"
using namespace std;


Dodecahedron::Bigint rec(int n, vector <Dodecahedron::Bigint> & base,const vector <Dodecahedron::Bigint> & constants, int d) {
	if (n <= d) {
		return base[n];
	}
	Dodecahedron::Bigint zero;
	zero = 0;
	Dodecahedron::Bigint result;
	result = 0;
	int count = 0;
	if (!(base[n] == 0)) {
		return base[n];
	}
	for (int i = d; i > 0; i--) {
		Dodecahedron::Bigint previous = rec(n - i, base, constants, d);
		Dodecahedron::Bigint constant = constants[d - count];
		result += (constant * previous);
		count++;
	}
	base[n] = result;
	return result;
}

int main() {
	int degree_n, degree_m;
	cout << "Please enter the degree of your recurrence: ";
	cin >> degree_n >> degree_m;
    Dodecahedron::Bigint zero = 0;
	std::vector <std::vector<Dodecahedron::Bigint>> bases(degree_n+1, std::vector<Dodecahedron::Bigint>(degree_m+1, zero));
	std::vector <std::vector<Dodecahedron::Bigint>> constants(degree_n+1, std::vector<Dodecahedron::Bigint>(degree_m+1, zero));
	constants[0][0] = 0;
	cout << "Please enter the constants: ";
	for (int i = 0; i < degree; i++) {
		Dodecahedron::Bigint temp;
		cin >> temp;
		constants.push_back(temp);
	}
	int cases = 0;
	Dodecahedron::Bigint zeroth;
	cout << "Please enter the zeroth term, i.e, result when n = 0: ";
	cin >> zeroth;
	base.push_back(zeroth);
	cout << "Please enter the first " << degree << " terms in order excluding the zeroth term : ";
	for (int i = 0; i < degree; i++) {
		Dodecahedron::Bigint temp;
		cin >> temp;
		base.push_back(temp);
	}
	int n;
	cout << "Please enter n: ";
	cin >> n;
	base.resize(n+1, 0);
	cout << "The " << n << "th term of the recurrence is: " << rec(n, base, constants, degree) << endl;
	return 0;
}