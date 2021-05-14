# Put your code here
def myRange(stop, start = None, step = None):
    if start==None:
        start = 0
        if step == None:
            step=1

        i=start
        l=[]
        return myRange(10)
    while i <= stop:
            l.append(i)
    i=i+step
        
print(myRange(10))
