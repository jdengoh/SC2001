
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
    n=first
    m=mid+1

    if (last-first <= 0 ):
        return
    
    while (n<=mid and m<=last): # while both halfs are not empty

        # case 1: 2nd half's first element smaller
        if numlist[n]>numlist[m]:
            temp=numlist[m]
            m += 1      # move 2nd half's pointer forward
            mid += 1    # move 1st half's end zone forward

            # shift entire 1st half forward
            for i in range (mid, n, -1):
                numlist[i] = numlist[i-1]

            # insert smaller element before 1st half boundaries
            numlist[n] = temp
            n += 1      # move 1st half's pointer forward

        # case 2: 1st half's first element smaller
        elif (numlist[n]<numlist[m]):
            n += 1      # move 1st half's pointer forward
        
        # case 3: 1st half and 2nd half's first element are EQUAL
        else:
            # both are last 2 elements, so nothing to be done
            if (n==mid) and (m==last):
                break

            # in case 3, n will move forward we are putting same element "side by side"
            temp=numlist[m]
            m += 1      # move 2nd half's pointer forward
            mid += 1    # move 1st half's end zone forward

            n += 1      # move 1st half's pointer forward (first time)
                        # this is because that element will remain there,
                        # it will not "shift" with the entire first half

            for i in range (mid, n, -1):
                numlist[i] = numlist[i-1]

            numlist[n] = temp
            n += 1      # move 1st half's pointer forward (second time)

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

    arr = []
    arr = randgen(1, 1000000, 1000000)
    print (arr)
    print(len(arr))

    ##### Insertion sort #####
    # InsertionSort(arr, 100)

    ##### Merge Sort #####
    MergeSort(arr, 0, len(arr)-1)

    print(arr)

  

if __name__=="__main__":
    main()
