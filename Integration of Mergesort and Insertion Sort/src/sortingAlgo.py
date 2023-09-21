from randomGenerator import randgen


def InsertionSort(numlist, first, last):
    keyComp = 0
    for i in range(first, last+1):
        for j in range (i, 0, -1):
            keyComp += 1
            if (numlist[j]<numlist[j-1]):
                temp = numlist[j]
                numlist[j] = numlist[j-1]
                numlist[j-1] = temp
            else:
                break
    return keyComp
                
# def swap(numlist, num1, num2):
#     temp = numlist[num1]
#     numlist[num1] = numlist[num2]
#     numlist[num2] = temp
#     return

def MergeSort(numlist, first, last):
    keyComp = 0
    mid = (last+first) // 2

    if (last-first <= 0):
            return keyComp 

    elif (last-first > 1):
        keyComp  = MergeSort(numlist, first, mid) + MergeSort(numlist, mid+1, last)
    
    return (Merge(numlist, first, last) + keyComp)


def Merge(numlist, first, last):
    
    keyComp = 0
    mid = (first+last)//2
    n = first
    m = mid+1

    if (last-first <= 0 ):
        return 0

    # sub-array size
    size1 = m-first
    size2 = last-(m-1)

    arr1 = []
    arr2 = []

    for i in range(size1):
        arr1.append(numlist[n+i])

    for j in range(size2):
        arr2.append(numlist[m+j])
    

    ind1 = ind2 = 0


    while (ind1<size1 and ind2<size2): # while both halfs are not empty
        
        # case 1: 2nd half's first element smaller
        if arr1[ind1]>arr2[ind2]:
            numlist[n]=arr2[ind2]
            ind2 += 1      # move 2nd half's pointer forward
            #print(numlist)
        # case 2: 1st half's first element smaller
        elif (arr1[ind1]<=arr2[ind2]):
            numlist[n]=arr1[ind1]
            ind1 += 1      # move 1st half's pointer forward

        n += 1
        keyComp += 1

        
    while (ind1<size1):
        numlist[n]=arr1[ind1]
        n += 1
        ind1 += 1

    while (ind2<size2):
        numlist[n]=arr2[ind2]
        n += 1
        ind2 += 1
     
    return keyComp

def MergeInsertSort (numlist, first, last, S):

    comp = 0
    size = last-first+1
    
    if (size<=S):
        comp += InsertionSort(numlist, first, last)
        return comp
    
    else:
        
        mid = (last+first) // 2
        if (last-first <= 0):
                return comp

        elif (last-first > 1):
            comp = MergeInsertSort(numlist, first, mid, S) + MergeInsertSort(numlist, mid+1, last, S)

        return (Merge(numlist, first, last) + comp)


def main():

    #arr = [14, 40, 31, 28, 3, 15, 17, 51]
    arr = randgen(1, 10000000, 10000000)
    #arr = randgen(1, 100, 10)
    print('hi')
    
    #arrcopy = list(arr)
    #print (arrcopy)
    #print(len(arr))

    ##### Insertion sort #####
    count = MergeInsertSort(arr, 0, len(arr)-1, 5)

    ##### Merge Sort #####
    #arrcopy.sort()
    #print(arrcopy)
    #print(arr)
    print("number of comp for Insertion Sort= " + str(count))
    
    print(arr)
    numOfComp=MergeSort(arr, 0, len(arr)-1)
    print("number of comp Merge Sort= " + str(numOfComp))
    print(len(arr))

if __name__=="__main__":
    main()