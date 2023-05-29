n = int(input("Integer: "))
m = int(input("Number of parts: "))
Capparelli_partitions = [[[[] for i in range(7)] for j in range(n+1)] for k in range(m+1)]  
Capparelli_partitions[1][2][2].append([2])
Capparelli_partitions[1][3][3].append([3])
Capparelli_partitions[1][4][4].append([4])
for i in range(1, m+1):
    for j in range(2, n+1):
        for k in range(2, 7):
            if k < 4:
                if (j + 3 * i <= n):
                    for partition in Capparelli_partitions[i][j][k]:
                        new_partition = []
                        for part in partition:
                            temp = part + 3
                            new_partition.append(temp)
                        Capparelli_partitions[i][j+(3*i)][k+3].append(new_partition)
            elif k == 4:
                if (i + 1 <= m and j + 2 <= n):
                    for partition in Capparelli_partitions[i][j][k]:
                        two_partition = [2]
                        two_partition.extend(partition)
                        Capparelli_partitions[i+1][j+2][2].append(two_partition)
                        if (j + 3 * i <= n):
                            new_partition = []
                            for part in partition:
                                temp = part + 3
                                new_partition.append(temp)
                            Capparelli_partitions[i][j+(3*i)][6].append(new_partition)
                elif(j + 3 * i <= n):
                    for partition in Capparelli_partitions[i][j][k]:
                        new_partition = []
                        for part in partition:
                            temp = part + 3
                            new_partition.append(temp)
                        Capparelli_partitions[i][j+(3*i)][6].append(new_partition)
            elif k == 5:
                if (j+(3*i)<=n):
                    for partition in Capparelli_partitions[i][j][k]:
                        new_partition = []
                        for part in partition:
                            temp = part + 3
                            new_partition.append(temp)
                        Capparelli_partitions[i][j+(3*i)][6].append(new_partition)
                        if (i+1<=m and j+(3*i)+4<=n):
                            four_partition = [4]
                            four_partition.extend(new_partition)
                            Capparelli_partitions[i+1][j+(3*i)+4][4].append(four_partition)
            elif k == 6:
                if (i + 1 <= m and j + 2 <= n):
                    for partition in Capparelli_partitions[i][j][k]:
                        two_partition = [2]
                        two_partition.extend(partition)
                        Capparelli_partitions[i+1][j+2][2].append(two_partition)
                        if (j + 3 <= n):
                            three_partition = [3]
                            three_partition.extend(partition)
                            Capparelli_partitions[i+1][j+3][3].append(three_partition)
                            if (j + (3 * i) <= n):
                                new_partition = []
                                for part in partition:
                                    temp = part + 3
                                    new_partition.append(temp)
                                Capparelli_partitions[i][j+(3*i)][6].append(new_partition)
                                if (j + (3*i)+4 <= n):
                                    four_partition = [4]
                                    four_partition.extend(new_partition)
                                    Capparelli_partitions[i+1][j+(3*i)+4][4].append(four_partition)

count = 0
for k in range(2, 7):
    for partition in Capparelli_partitions[m][n][k]:
        print(partition)
        count = count + 1

print(count)

debug = 1