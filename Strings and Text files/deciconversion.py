

alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'



val = {}

def repToDecimal(num, base):
    for i in range(base):
        val[alpha[i]] = i
        m = 1
        res = 0

    for i in num[: : -1]:
        d = val[i.upper()]
        res += d * m
        m *= base
    return res

def main():

    print(repToDecimal('num', base))


main()
