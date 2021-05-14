def printAll(seq):
    print(seq)
    if seq:
        print(seq[0])
        printAll(seq[1:])

if __name__ =="__main__":

 printAll([1,3,5,2,6,9])

print("Running for empty sequence")

printAll([])
