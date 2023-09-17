
import random


def randgen(start,end,size):
    numlist = []
    random.seed()
    
    for i in range (size):
        numlist.append(random.randint(start,end))

    #print(numlist)

    return numlist


def InsertionSort(numlist, size):
    for i in range(size):
        for j in range (i, 0, -1):
            if (numlist[j]<numlist[j-1]):
                numlist = swap(numlist, j, j-1)
            else:
                break
            
def swap(numlist, num1, num2):
    temp = numlist[num1]
    numlist[num1] = numlist[num2]
    numlist[num2] = temp
    return numlist



def MergeSort(numlist, first, last):
    mid = (last+first) // 2
    if (last-first <= 0):
            return

    elif (last-first > 1):
        MergeSort(numlist, first, mid)
        MergeSort(numlist, mid+1, last)

    numlist = Merge(numlist, first, last)


def Merge(numlist, first, last):

    mid = (first+last)//2
    n = first
    m = mid+1


    if (last-first <= 0 ):
        return

    # sub-array size
    size1 = m-first
    size2 = last-(m-1)

    arr1 = []
    arr2 = []

    for i in range(size1):
        arr1.append(numlist[n+i])

    for j in range(size2):
        arr2.append(numlist[m+j])
    
    # print("arr1: ")
    # print(arr1)
    # print("arr2: ")
    # print(arr2)
    # print("\n")

    ind1 = ind2 = 0


    while (ind1<size1 and ind2<size2): # while both halfs are not empty

        # case 1: 2nd half's first element smaller
        if arr1[ind1]>arr2[ind2]:
            numlist[n]=arr2[ind2]
            n += 1
            ind2 += 1      # move 2nd half's pointer forward
            #print(numlist)
        # case 2: 1st half's first element smaller
        elif (arr1[ind1]<=arr2[ind2]):
            numlist[n]=arr1[ind1]
            n += 1
            ind1 += 1      # move 1st half's pointer forward
            #print(numlist)
        # case 3: 1st half and 2nd half's first element are EQUAL
        # else:
        #     numlist[n]=arr1[ind1]
        #     n += 1
        #     numlist[n]=arr2[ind2]
        #     n += 1
        #     ind1 += 1
        #     ind2 += 1
    
    while (ind1<size1):
        numlist[n]=arr1[ind1]
        n += 1
        ind1 += 1

    while (ind2<size2):
        numlist[n]=arr2[ind2]
        n += 1
        ind2 += 1
    #print(numlist)   
    return

# def MergeInsertSort (numlist, first, last, S):

#     size = last-first+1

#     if (size<S):
#         InsertionSort(numlist, size)
                      
#     else:
    
#         if (last-first <= 0):
#             return numlist

#         elif (last-first > 1):
            
#             mid = last+first // 2

#             MergeInsertSort(numlist, first,mid)
#             MergeInsertSort(numlist, mid+1, last)

#         Merge(numlist, first, last)
#         return numlist
        


def main():

    #arr = [10, 4, 9, 5, 9, 6, 3, 3, 1, 7]
    arr = randgen(1, 20, 20)

    arrcopy = list(arr)
    #print (arr)
    #print(len(arr))

    ##### Insertion sort #####
    # InsertionSort(arr, 100)

    ##### Merge Sort #####
    arrcopy.sort()
    print(arrcopy)
    print(arr)
    MergeSort(arr, 0, len(arr)-1)
    print(arr)
    print(len(arr))

  

if __name__=="__main__":
    main()
