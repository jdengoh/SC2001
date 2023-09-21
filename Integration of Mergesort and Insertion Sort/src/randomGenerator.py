import random

def randgen(numlist,end,size):
    random.seed()
    
    for i in range (size):
        numlist.append(random.randint(1,end))

    #print(numlist)

    #return numlist