def calculateMin(num_parts, dist):
    min = [0 for m in range(num_parts+1)]
    sum = 0
    buff = 1
    resetCount = 0
    for i in range(1, num_parts+1):
        if resetCount == dist - 1:
            resetCount = 0
            buff += 2
        sum += buff
        min[i] = sum
        resetCount =  resetCount + 1
    return min

def nextPart(num, num_parts, max, min):
    result = num - min[num_parts - 1]
    if result > max:
        return max
    return result

def getMaxNext(partitions, dist, pos):
    if dist == 2:
        return partitions[pos] - 2
    previous = dist - 2
    if pos - previous < 1:
        return partitions[pos]
    previousTerm = partitions[pos-previous]
    currentTerm = partitions[pos]
    if previousTerm - currentTerm == 0:
        return currentTerm - 2
    elif previousTerm - currentTerm == 1:
        return currentTerm - 1
    return currentTerm

def ListRRGpartitions(num, num_parts, dist, max_ones):
    max_ones = max_ones - 1
    if num_parts > num:
        return []
    if dist < 2:
        return []
    if num_parts == 1:
        return [[num]]
    if max_ones < 0:
        return []
    if max_ones >= dist:
        return []
    min = calculateMin(num_parts, dist)
    if num < min[num_parts]:
        return [[num]]
    partitions = []
    partition = [0 for m in range(num_parts+1)]
    pastSum = 0
    for  i in range(1, num_parts+1):
        result = 0
        if i == 1:
            result = nextPart(num, num_parts, num, min)
        else:
            result = nextPart(num-pastSum, (num_parts+1)-i, getMaxNext(partition, dist, i-1), min)
        partition[i] = result
        pastSum = pastSum + result
    new_ptn = partition.copy()
    if new_ptn[num_parts-max_ones] >= 2:
        partitions.append(new_ptn[1:])
    count = 1
    pos = 0
    allfailed = False
    while (allfailed != True):
        ispartition = False
        for pos in range(num_parts-1, 0, -1):
            remainder = 0
            pastSum = 0
            partition[pos] = partition[pos] - 1
            if pos > num_parts/2:
                for i in range(0, num_parts - pos):
                    remainder = remainder + partition[num_parts-i]
                remainder = remainder + 1
                pastSum = num - remainder
            else:
                for i in range(1, pos+1):
                    pastSum += partition[i]
                remainder = num - pastSum
            postChange = 0
            for i in range(pos+1, num_parts+1):
                result = nextPart(remainder, (num_parts+1) - i, getMaxNext(partition, dist, i-1), min)
                partition[i] = result
                remainder -= result
                postChange += result
            if pastSum + postChange == num:
                ispartition = True
                break
        if ispartition != True:
            allfailed = True
        else:
            if partition.copy()[num_parts-max_ones] >= 2:
                partitions.append(partition.copy()[1:])
            count = count + 1
    return partitions

def rogerRG(num, num_parts, dist, max_ones, RRGterms):
    if max_ones == 0:
        return 0
    if num == 0 and num_parts == 0:
        return 1
    if num < 0 or num_parts < 0:
        return 0
    if num == 0 or num_parts == 0:
        return 0
    if RRGterms[max_ones][num][num_parts] != -1:
        return RRGterms[max_ones][num][num_parts]
    
    result = rogerRG(num, num_parts, dist, max_ones-1, RRGterms)
    result = result + rogerRG(num - num_parts, num_parts - max_ones + 1, dist, dist - max_ones + 1, RRGterms)
    RRGterms[max_ones][num][num_parts] = result
    return result

def mRogerRG(num, num_parts, dist, max_ones):
    if dist < 2:
        return 0
    if max_ones > dist:
        return 0
    RRGterms = [[[-1 for m in range(num_parts+1)] for n in range(num+1)] for k in range(dist+1)]
    result = rogerRG(num, num_parts, dist, max_ones, RRGterms)
    return result

def capcounter(num, num_parts):
    Capparelli_partitions = [[[0 for i in range(7)] for n in range(num+1)] for k in range(num_parts+1)]  
    Capparelli_partitions[1][2][2] = 1
    Capparelli_partitions[1][3][3] = 1
    Capparelli_partitions[1][4][4] = 1
    for i in range(1, num_parts+1):
        for j in range(2, num+1):
            for smallest_part in range(2, 7):
                if smallest_part < 4:
                    if (j + 3 * i <= num):
                        Capparelli_partitions[i][j+(3*i)][smallest_part+3] = Capparelli_partitions[i][j+(3*i)][smallest_part+3] + Capparelli_partitions[i][j][smallest_part]
                elif smallest_part == 4:
                    if (i + 1 <= num_parts and j + 2 <= num):
                        Capparelli_partitions[i+1][j+2][2] = Capparelli_partitions[i+1][j+2][2] + Capparelli_partitions[i][j][smallest_part]
                        if (j + 3 * i <= num):
                            Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][smallest_part]
                    elif(j + 3 * i <= num):
                        Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][smallest_part]
                elif smallest_part == 5:
                    if (j+(3*i)<=num):
                        Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][smallest_part]
                        if (i+1<=num_parts and j+(3*i)+4<=num):
                            Capparelli_partitions[i+1][j+(3*i)+4][4] = Capparelli_partitions[i+1][j+(3*i)+4][4] + Capparelli_partitions[i][j][smallest_part]
                elif smallest_part == 6:
                    if (i + 1 <= num_parts and j + 2 <= num):
                        Capparelli_partitions[i+1][j+2][2] = Capparelli_partitions[i+1][j+2][2] + Capparelli_partitions[i][j][smallest_part]
                        if (j + 3 <= num):
                            Capparelli_partitions[i+1][j+3][3] = Capparelli_partitions[i+1][j+3][3] + Capparelli_partitions[i][j][smallest_part]
                            if (j + (3 * i) <= num):
                                Capparelli_partitions[i][j+(3*i)][6] = Capparelli_partitions[i][j+(3*i)][6] + Capparelli_partitions[i][j][smallest_part] 
                                if (j + (3*i)+4 <= num):
                                    Capparelli_partitions[i+1][j+(3*i)+4][4] = Capparelli_partitions[i+1][j+(3*i)+4][4] + Capparelli_partitions[i][j][smallest_part]

    result = 0
    for k in range(2, 7):
        result = result + Capparelli_partitions[num_parts][num][k]
    return result

def capgenerator(n, m):
    Capparelli_partitions = [[[[] for _ in range(7)] for _ in range(n + 1)] for _ in range(m + 1)]

    # Preallocate frequently accessed lists

    # Base cases
    Capparelli_partitions[1][2][2] = [[2]]
    Capparelli_partitions[1][3][3] = [[3]]
    Capparelli_partitions[1][4][4] = [[4]]

    # Dynamic programming loop
    for i in range(1, m + 1):
        for j in range(2, n + 1):
            for k in range(2, 7):
                partition_list = Capparelli_partitions[i][j][k]  # Local variable for faster access

                if k < 4 and j + 3 * i <= n:
                    new_partition_list = []
                    for partition in partition_list:
                        new_partition = [part + 3 for part in partition]
                        new_partition_list.append(new_partition)
                    Capparelli_partitions[i][j + 3 * i][k + 3].extend(new_partition_list)

                elif k == 4:
                    if i + 1 <= m and j + 2 <= n:
                        two_partition_list = [[2] + partition for partition in partition_list]
                        Capparelli_partitions[i + 1][j + 2][2].extend(two_partition_list)
                        if j + 3 * i <= n:
                            new_partition_list = []
                            for partition in partition_list:
                                new_partition = [part + 3 for part in partition]
                                new_partition_list.append(new_partition)
                            Capparelli_partitions[i][j + 3 * i][6].extend(new_partition_list)
                    elif j + 3 * i <= n:
                        new_partition_list = []
                        for partition in partition_list:
                            new_partition = [part + 3 for part in partition]
                            new_partition_list.append(new_partition)
                        Capparelli_partitions[i][j + 3 * i][6].extend(new_partition_list)

                elif k == 5:
                    if j + 3 * i <= n:
                        new_partition_list = []
                        for partition in partition_list:
                            new_partition = [part + 3 for part in partition]
                            new_partition_list.append(new_partition)
                        Capparelli_partitions[i][j + 3 * i][6].extend(new_partition_list)
                        if i + 1 <= m and j + 3 * i + 4 <= n:
                            four_partition_list = [[4] + new_partition for new_partition in new_partition_list]
                            Capparelli_partitions[i + 1][j + 3 * i + 4][4].extend(four_partition_list)

                elif k == 6:
                    if i + 1 <= m and j + 2 <= n:
                        two_partition_list = [[2] + partition for partition in partition_list]
                        Capparelli_partitions[i + 1][j + 2][2].extend(two_partition_list)
                        if j + 3 <= n:
                            three_partition_list = [[3] + partition for partition in partition_list]
                            Capparelli_partitions[i + 1][j + 3][3].extend(three_partition_list)
                            if j + 3 * i <= n:
                                new_partition_list = []
                                for partition in partition_list:
                                    new_partition = [part + 3 for part in partition]
                                    new_partition_list.append(new_partition)
                                Capparelli_partitions[i][j + 3 * i][6].extend(new_partition_list)
                                if j + 3 * i + 4 <= n:
                                    four_partition_list = [[4] + new_partition for new_partition in new_partition_list]
                                    Capparelli_partitions[i + 1][j + 3 * i + 4][4].extend(four_partition_list)
                    elif j + 3 * i <= n:
                        new_partition_list = []
                        for partition in partition_list:
                            new_partition = [part + 3 for part in partition]
                            new_partition_list.append(new_partition)
                        Capparelli_partitions[i][j + 3 * i][6].extend(new_partition_list)
                        if i + 1 <= m and j + 3 * i + 4 <= n:
                            four_partition_list = [[4] + new_partition for new_partition in new_partition_list]
                            Capparelli_partitions[i + 1][j + 3 * i + 4][4].extend(four_partition_list)

    # Flatten and return the result
    result = [partition for k in range(2, 7) for partition in Capparelli_partitions[m][n][k]]
    return result

def cappgenerator(n, m):
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
                  elif (j + (3 * i) <= n):
                      for partition in Capparelli_partitions[i][j][k]:
                        new_partition = []
                        for part in partition:
                            temp = part + 3
                            new_partition.append(temp)
                        Capparelli_partitions[i][j+(3*i)][6].append(new_partition)
                        if (i + 1 <= m and j + (3*i)+4 <= n):
                            four_partition = [4]
                            four_partition.extend(new_partition)
                            Capparelli_partitions[i+1][j+(3*i)+4][4].append(four_partition)

  result =[]
  for k in range(2, 7):
      for partition in Capparelli_partitions[m][n][k]:
          result.append(partition)

  return result