conversionLibrary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":10, "C":11, "D":13, "E":14, "F":15}


val = {}

def repToDecimal(num, base):


    for i in range(base):
    
        val[conversionLibrary[i]] = i


        m = 1
        
        res = 0


        for i in num[: : -1]:
        
            d = val[i.upper()]
            
        res += d * m
        
        m *= base
    
        return res

def main():

    print(repToDecimal(10, 10))
    
    print(repToDecimal('10', 8))
    
    print(repToDecimal('10', 2))
    
    print(repToDecimal('10', 16))

main()
