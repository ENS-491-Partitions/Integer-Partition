#n = int(input("Please enter the integer: "))
#m = int(input("Please enter the number of parts: "))
#k = int(input("Please enter the constraint k: "))
#a = int(input("Please enter the constraint a: "))

n = 30
m = 7
k = 3
a = 3 

rrg_partitions = [[[[] for i in range(0,k+1)] for j in range(0,m+1)] for l in range(0, n+1)]
partition = []
for i in range(1,k):
    partition.append(1)
    new_partition = partition.copy()
    rrg_partitions[i][i][i+1].append(new_partition)

for i in range(1, n-m+1):
    for j in range(1, m + 1):
        for p in range(1, k+1):
            for ptn in rrg_partitions[i][j][p]:
                new_partition = ptn.copy()
                for q in range(0, len(new_partition)):
                    new_partition[q] = new_partition[q] + 1
                rrg_partitions[i+j][j][1].append(new_partition)
                max = k - p + 1
                if (m - j + 1 < max):
                    max = m - j + 1
                temp_ptn = new_partition.copy()
                for r in range(1, max):
                    temp_ptn.append(1)
                    new_ptn = temp_ptn.copy()
                    rrg_partitions[i+j+r][j+r][r+1].append(new_ptn)

count = 0
for x in range(1,k+1):
    count += len(rrg_partitions[30][7][x])
    print("roger ramanujan gordon partitions of", n ,"into", m, "parts with k =", k, "and at most", x - 1, "ones is",  count)
