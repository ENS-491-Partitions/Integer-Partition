#include "bigint.h"
#include <iostream>
#include <vector>

using namespace std;



/*********************************************************************
params: 
m (integer) => Number of parts
k (integer) => Maximum count of occurence of two consecutive integers
returns: minimum integer that has
a partition into m parts given integer k 
***********************************************************************/
vector<int> calculateMin(int m, int k) {
	vector<int> min(m + 1, 0);
	int sum = 0;
	int buff = 1; //Integer with which to increase the sum on each iteration
	int resetCount = 0; //Count on when to increment the buffer
	for (int i = 1; i <= m; i++) {
		if (resetCount == k-1) {
			resetCount = 0;
			buff += 2;
		}
		sum += buff;
		min[i] = sum;
		resetCount++;
	}
	return min;
}


/***********************************************************************************************************
params:
n (integer) => Integer to be partitioned
m (integer) => Number of parts
max (integer) => Maximum size of the part to be returned
min (vector<int>) => Array of the minimum integer that can be divided into i E [1,m] parts
returns: Size of the first part of integer n into m parts given max possible and minimum for remaining parts
************************************************************************************************************/
int nextPart(int n, int m, int max, vector<int> min) {
	int result = n - min[m - 1];
	if (result > max) {
		return max;
	}
	return result;
}


/***********************************************************************************************************
params:
k (integer) => Maximum count of occurence of two consecutive integers
pos (integer) => Index
partitions (vector<int>) => current Partition
returns: Maximum possible size for the part next to pos, i.e, partitions[pos+1]
************************************************************************************************************/
int getMaxNext(vector<int> partitions, int k, int pos) {
	if (k == 2) {
		return partitions[pos] - 2;
	}
	int previous = k - 2;
	if (pos - previous < 1) {
		return partitions[pos];
	}
	int previousTerm = partitions[pos - previous];
	int currentTerm = partitions[pos];
	if (previousTerm - currentTerm == 0) {
		return currentTerm - 2;
	}
	else if (previousTerm - currentTerm == 1) {
		return currentTerm - 1;
	}
	return currentTerm;
}

void printPartition(vector<int> partitions, int m) {
	for (int i = 1; i <= m; i++) {
		cout << partitions[i] << " ";
	}
	cout << endl;
}

void ListRRGpartitions(int n, int m, int k) {
	if (m > n) {
		cout << n << " has 0 partitions into " << m << " parts satisfying the provided constraints" << endl;
		return;
	}
	if (k < 2) {
		cout << "K has to be atleast 2 "<< endl;
		return;
	}
	if (m == 1) {
		cout << n << endl;
		cout << "There is 1 partition of " << n << " into " << m << " part for k = " << k << endl;
	}
	vector<int> min = calculateMin(m, k);
	if (n < min[m]) {
		cout << n << " has 0 partitions into " << m << " parts satisfying the provided constraints" << endl;
		return;
	}
	vector<int> partitions(m + 1, 0);
	int pastSum = 0;
	for (int i = 1; i <= m; i++) {
		int result = 0;
		if (i == 1) {
			result = nextPart(n, m, n, min);
		}
		else {
			result = nextPart(n - pastSum, (m + 1) - i, getMaxNext(partitions, k, i - 1), min);
		}
		partitions[i] = result;
		pastSum += result;
	}
	printPartition(partitions, m);
	Dodecahedron::Bigint count = 1;
	int pos = 0;
	bool allfailed = false;
	while (allfailed != true)
	{
		bool ispartition = false;
		for (int pos = m - 1; pos > 0; pos--) {
			vector<int> partition = partitions;
			int remainder = 0;
			pastSum = 0;
			partition[pos] = partition[pos] - 1;
			if (pos > m / 2) {
				for (int i = 0; i < m - pos; i++) {
					remainder += partition[m - i];
				}
				remainder++;
				pastSum = n - remainder;
			}
			else {
				for (int i = 1; i <= pos; i++) {
					pastSum += partition[i];
				}
				remainder = n - pastSum;
			}
			int postChange = 0;
			for (int i = pos + 1; i <= m; i++) {
				int result = nextPart(remainder, (m + 1) - i, getMaxNext(partition, k, i - 1), min);
				partition[i] = result;
				remainder -= result;
				postChange += result;
			}
			if (pastSum + postChange == n) {
				ispartition = true;
				partitions = partition;
				break;
			}
		}
		if (ispartition != true) {
			allfailed = true;
		}
		else {
			printPartition(partitions, m);
			count = count + 1;
		}
	}
	cout << "There are " << count << " partitions of " << n << " into " << m << " parts for k = " << k << endl;
}


int main() {
	//vector<int> test = calculateMin(3, 2);
	int n, m, k;
	cout << "Please enter the integer whose partitions you want to generate: ";
	cin >> n;
	cout << "Please enter the number of parts: ";
	cin >> m;
	cout << "Please enter the constraint k: ";
	cin >> k;
	ListRRGpartitions(n, m, k);
	

	return 1;
}