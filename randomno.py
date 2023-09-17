
import random

def randgen(start,end,size):
    numlist = []
    random.seed()

    for i in range (size):
        numlist.append(random.randint(start,end))

    #print(numlist)

    return numlist


# def MergeInsertSort (numlist, first, last, S):
#     size = last-first+1

#     if (size<S):
        


# def InsertionSort(numlist, first, last):

#     for i in range(first-1,last):
#         for j in range (i, first, -1):
#             if numlist[j]<numlist[j-1]:
#                 numlist = swap(numlist, j, j-1)
#             else:
#                 break

def InsertionSort(numlist, size):

    for i in range(size):
        for j in range (i, -1, -1):
            if (numlist[j]<numlist[j-1]):
                numlist = swap(numlist, j, j-1)
            else:
                break
            

def swap(numlist, num1, num2):
    temp = numlist[num1]
    numlist[num1] = numlist[num2]
    numlist[num2] = temp
    return numlist


def main():
    arr = []
    arr = randgen(1, 100, 100)
    print (arr)
    print(len(arr))
    InsertionSort(arr, 100)

    print(arr)
  
  
# Using the special variable 
# __name__
if __name__=="__main__":
    main()