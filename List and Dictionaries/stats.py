lyst = [3, 1, 7, 1, 4, 10]

def median(lyst):
    sortedLst = sorted(lyst)
    lstLen = len(lyst)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def mean(lyst):
    if len(lyst) == 0:
        return 0
    list.sort(lyst)
    total = 0
    for number in lyst:
        total += number
    return total / len(lyst)

def mode(lyst):
   mode = max(lyst, key = lyst.count)
   return mode

def main():
    print(lyst)
    print(mode(lyst))
    print(median(lyst))
    print(mean(lyst))
main()
