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

def capgenerator(num, num_parts):
    partitions = [[[1, 2, 2], [2]],[[1, 3, 3], [3]],[[1, 4, 4], [4]]]
    result = []
    while len(partitions) != 0:
        partition = partitions[0]
        details = partition[0]
        ptn = partition[1]
        n = details[1]
        m = details[0]
        k = details[2]
        if (k < 4):
            if (n + 3 * m <= num):
                new_ptn = [(x + 3) for x in ptn]
                if m == num_parts and n + 3 * m == num:
                    result.append(new_ptn.copy())
                else:
                    partitions.append([[m, n+(3*m), k+3], new_ptn.copy()])
        elif k == 4:
            if (m + 1 <=  num_parts and n + 2 <= num):
                two_partition = [2]
                two_partition.extend(ptn)
                if m + 1 == num_parts and n + 2 == num:
                    result.append(two_partition.copy())
                else:
                    partitions.append([[m + 1, n+ 2, 2], two_partition.copy()]) 
                if (n + 3 * m <= num):
                    new_ptn = [( x + 3 ) for x in ptn]
                    if m == num_parts and n + 3 * m == num:
                        result.append(new_ptn.copy())
                    else:
                        partitions.append([[m, n+(3*m), 6], new_ptn.copy()])
            elif (n + 3 * m <= num):
                new_ptn = [( x + 3 ) for x in ptn]
                if m == num_parts and n + 3 * m == num:
                    result.append(new_ptn.copy())
                else:
                    partitions.append([[m, n+(3*m), 6], new_ptn.copy()])
        elif k == 5:
            if (n + 3 * m <= num):
                new_ptn = [(x + 3) for x in ptn]
                if m == num_parts and n + 3 * m == num:
                    result.append(new_ptn.copy())
                else:
                    partitions.append([[m, n+(3*m), 6], new_ptn.copy()])
                if (m + 1 <= num_parts and n + (3 * m) + 4 <= num):
                    four_partition = [4]
                    four_partition.extend(new_ptn)
                    if m + 1 == num_parts and n + (3 * m) + 4 == num:
                        result.append(four_partition.copy())
                    else:
                        partitions.append([[m + 1, n+(3*m) + 4, 4], four_partition.copy()])
        elif k == 6:
            if (m + 1 <= num_parts and n + 2 <= num):
                two_partition = [2]
                two_partition.extend(ptn)
                if m + 1 == num_parts and n + 2 == num:
                    result.append(two_partition.copy())
                else:
                    partitions.append([[m + 1, n+ 2, 2], two_partition.copy()]) 
                if n + 3 <= num:
                    three_partition = [3]
                    three_partition.extend(ptn)
                    if m + 1 == num_parts and n + 3 == num:
                        result.append(three_partition.copy())
                    else:
                        partitions.append([[m + 1, n+ 3, 3], three_partition.copy()]) 
                    if n + (3 * m) <= num:
                        new_ptn = [(x+3) for x in ptn]
                        if m == num_parts and n + 3 * m == num:
                            result.append(new_ptn.copy())
                        else:
                            partitions.append([[m, n+(3*m), 6], new_ptn.copy()])
                        if (m + 1 <= num_parts and n + (3 * m) + 4 <= num):
                            four_partition = [4]
                            four_partition.extend(new_ptn)
                            if m + 1 == num_parts and n + (3 * m) + 4 == num:
                                result.append(four_partition.copy())
                            else:
                                partitions.append([[m + 1, n+(3*m) + 4, 4], four_partition.copy()])
            elif (n + (3 * m) <= num):
                new_ptn = [(x+3) for x in ptn]
                if m == num_parts and n + 3 * m == num:
                    result.append(new_ptn.copy())
                else:
                    partitions.append([[m, n+(3*m), 6], new_ptn.copy()])
                if (m + 1 <= num_parts and n + (3 * m) + 4 <= num):
                    four_partition = [4]
                    four_partition.extend(new_ptn)
                    if m + 1 == num_parts and n + (3 * m) + 4 == num:
                        result.append(four_partition.copy())
                    else:
                        partitions.append([[m + 1, n+(3*m) + 4, 4], four_partition.copy()])

        partitions = partitions[1:]
    return result