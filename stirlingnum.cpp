#include <iostream>
#include <vector>
#include "bigint.h"


using namespace Dodecahedron;

Bigint stirling(int n, int m, std::vector  <std::vector<Bigint>> &terms) {
	Bigint zero;
	Bigint one;
	Bigint random;
	random = 10;
	one = 1;
	zero = 0;
	if (n == 0 || m == 0) {
		return zero;
	}
	else if (n == m || m == 1) {
		return one;
	}
	else if (m > n) {
		return zero;
	}
	else if (!(terms[n][m] == zero)) {
		return terms[n][m];
	}
	
	else {
		Bigint result;
		Bigint em;
		em = m;
		result = em * stirling(n - 1, m, terms) + stirling(n - 1, m - 1, terms);
		terms[n][m] = result;
		return result;
	}
	return random;
}

Bigint mstirling(int n, int m) {
	Bigint zero;
	zero = 0;
	std::vector <std::vector<Bigint>> terms(n+1, std::vector<Bigint>(m+1, zero));
	Bigint term = stirling(n, m, terms);
	return term;
}

int main(){
	int n = 0, m = 0;
	std::cout << mstirling(n, m) << std::endl;
	std::cout << mstirling(1, 10) << std::endl;
	std::cout << mstirling(10, 10) << std::endl;
	std::cout << mstirling(100, 50) << std::endl;
}