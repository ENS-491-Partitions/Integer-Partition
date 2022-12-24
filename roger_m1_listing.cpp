#include <iostream>
#include <string>
#include "bigint.h"
#include <vector>
#include <unordered_set>

using namespace std;

// Function to generate all the partitions of n such that all parts differ by at least 2 and each partition is unique
void generatePartitions(int n, int last, vector<int>& partition, vector<vector<int>>& partitions, unordered_set<string>& used)
{
	// Base case: If n is 0, add the current partition to the list of partitions
	if (n == 0)
	{
		// Convert the partition to a string
		string str;
		for (int i = 0; i < partition.size(); i++)
		{
			str += to_string(partition[i]) + " ";
		}
		// Check if the partition has already been used
		if (used.count(str) > 0)
		{
			return;
		}

		// Mark the partition as used
		used.insert(str);

		// Add the partition to the list
		partitions.push_back(partition);
		return;
	}

	// Recursive case: Try adding each valid part to the current partition
	for (int i = last + 2; i <= n; i++)
	{
		// Add the part to the partition
		partition.push_back(i);

		// Generate all the partitions of the remaining number (n - i)
		generatePartitions(n - i, i, partition, partitions, used);

		// Remove the part from the partition
		partition.pop_back();
	}
}

int main()
{
	// List all the partitions of 4 such that all parts differ by at least 2 and each partition is unique
	vector<int> partition;
	vector<vector<int>> partitions;
	unordered_set<string> used;
	generatePartitions(13, 0, partition, partitions, used);
	// Print the partitions
	for (int i = 0; i < partitions.size(); i++)
	{
		cout << "Partition " << i + 1 << ": ";
		for (int j = 0; j < partitions[i].size(); j++)
		{
			cout << partitions[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}