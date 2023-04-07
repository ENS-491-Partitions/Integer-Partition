#include <iostream>
#include <vector>
#include "bigint.h"
using namespace std;

vector<int> calculateMin(int m, int k) {
	vector<int> min(m + 1, 0);
	int sum = 0;
	int buff = 1; //Integer with which to increase the sum on each iteration
	int resetCount = 0; //Count on when to increment the buffer
	for (int i = 1; i <= m; i++) {
		if (resetCount == k - 1) {
			resetCount = 0;
			buff += 2;
		}
		sum += buff;
		min[i] = sum;
		resetCount++;
	}
	return min;
}

void printpartitions(int n, int m, int k, int a, vector<vector<vector<int>>> Partitions) {
	for (int i = 1; i <= a; i++) {
		for (int j = 0; j < Partitions[i].size(); j++) {
			for (int k = 0; k < Partitions[i][j].size(); k++) {
				cout << Partitions[i][j][k] << " ";
			}
			cout << endl;
		}
	}
}

void rogerRG(int n, int m, int k, int a, vector<int> min) {
	vector<vector<vector<int>>> A_partitions(k+1);
	vector<vector<vector<vector<vector<int>>>>> RRGPartitions (n+1);
	int currentMaxParts = 0;
	for (int i = 1; i <= n; i++) {
		if (currentMaxParts < m) {
			if (n >= min[currentMaxParts + 1]) {
				currentMaxParts++;
			}
		}
		vector<vector<vector<vector<int>>>> M_partitions(currentMaxParts+1, A_partitions);
		RRGPartitions[i] = M_partitions;
	}
	int stop = n - m;
	int num = 0;
	int num_parts = 0;
	int one_constraint = 1;
	vector<int> partition;
	for (int i = 1; i < k; i++) {
		partition.push_back(1);
		num++;
		num_parts++;
		one_constraint++;
		RRGPartitions[num][num_parts][one_constraint].push_back(partition);
	}
	for (int i = 1; i <= stop; i++) {
		int max_parts = RRGPartitions[i].size();
		for (int j = 1; j < max_parts; j++) {
			for (int p = 1; p <= k; p++) {
				//int max_ones = k - p;
				for (int q = 0; q < RRGPartitions[i][j][p].size(); q++) {
					vector<int> partition = RRGPartitions[i][j][p][q];
					for (int r = 0; r < partition.size(); r++) {
						partition[r]++;
					}
					RRGPartitions[i + j][j][1].push_back(partition);
					int max = k-p+1;
					if (m - j + 1 < k - p + 1) {
						max = m - j + 1;
					}
					for (int r = 1; r < max; r++) {
						partition.push_back(1);
						RRGPartitions[i + j + r][j + r][r+1].push_back(partition);
					}
				}
			}
		}
	}
	//printpartitions(n, m, k, a, RRGPartitions[n][m]);
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
	vector <int> min = calculateMin(m, k);
	rogerRG(n, m, k, a, min);
	return 1;
}