n = int(input("Integer: "))
m = int(input("Number of Parts: "))
Capparelli_partitions = [[[0 for i in range(7)] for j in range(n+1)] for k in range(m+1)]  
Capparelli_partitions[1][2][2] = 1
Capparelli_partitions[1][3][3] = 1
Capparelli_partitions[1][4][4] = 1
for i in range(1, m+1):
    for j in range(2, n+1):
        for k in range(2, 7):
            if k < 4:
                if (j + 3 * i <= n):
                    Capparelli_partitions[i][j+(3*i)][k+3] = Capparelli_partitions[i][j+(3*i)][k+3] + Capparelli_partitions[i][j][k]
            elif k == 4:
                if (i + 1 <= m and j + 2 <= n):
                    Capparelli_partitions[i+1][j+2][2] = Capparelli_partitions[i+1][j+2][2] + Capparelli_partitions[i][j][k]
                    if (j + 3 * i <= n):
                        Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][k]
                elif(j + 3 * i <= n):
                    Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][k]
            elif k == 5:
                if (j+(3*i)<=n):
                    Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][k]
                    if (i+1<=m and j+(3*i)+4<=n):
                        Capparelli_partitions[i+1][j+(3*i)+4][4] = Capparelli_partitions[i+1][j+(3*i)+4][4] + Capparelli_partitions[i][j][k]
            elif k == 6:
                if (i + 1 <= m and j + 2 <= n):
                    Capparelli_partitions[i+1][j+2][2] = Capparelli_partitions[i+1][j+2][2] + Capparelli_partitions[i][j][k]
                    if (j + 3 <= n):
                        Capparelli_partitions[i+1][j+3][3] = Capparelli_partitions[i+1][j+3][3] + Capparelli_partitions[i][j][k]
                        if (j + (3 * i) <= n):
                            Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][k] 
                            if (j + (3*i)+4 <= n):
                                Capparelli_partitions[i+1][j+(3*i)+4][4] = Capparelli_partitions[i+1][j+(3*i)+4][4] + Capparelli_partitions[i][j][k]

count = 0
for k in range(6, 1, -1):
    print("Capparelli partitions of", n, " with parts greater than" , k, "=",  Capparelli_partitions[m][n][k])
    count = count + Capparelli_partitions[m][n][k]

print(n, "has", count, "Capparelli partitions into 5 parts")

debug = 1