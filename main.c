#include <stdio.h>
#include <stdlib.h>

int main()
{
    srand(time(NULL));

    int arraySize;
    int i;
    int *counter;
    *counter =0;
    printf("input array size: ");
    scanf("%d", &arraySize);

    int arr[arraySize];

    for(i=0;i<arraySize;i++){
        arr[i]=rand()%100 +1;
    }
    for(i=0;i<arraySize;i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    MergeInsertSort(arr, 0, arraySize-1, 5, counter);

    printf("Key comparisons:");
    printf("Sorted: \n");
    for(i=0;i<arraySize;i++){
        printf("%d ",arr[i]);
    }


}

void MergeInsertSort (int *arr, int first, int last, int S, int *counter){
    int size = last-first+1;

    if(size<S){
        InsertionSort(arr, first, last, counter);
    }
    else{
        int mid = (first+last)/2;
        MergeInsertSort(arr, first, mid, S, counter);
        MergeInsertSort(arr, mid+1, last, S, counter);
        Merge(arr, first, last, mid, counter);
    }
}

void InsertionSort (int *arr, int first, int last, int *counter){
    for (int i=first; i<=last; i++){
        for(int j=i; j>first; j--){
            (*counter)++;
            if(arr[j]<arr[j-1]){
                swap(arr,j,j-1);
            }
        }
    }
}

void Merge(int *arr, int first, int last, int mid, int *counter){
    int temp;
    int a,b,i;
    a=first;
    b=mid+1;

    if(last-first <= 0){
        return;
    }
    while(a<=mid && b <= last){
        (*counter)++;
        if(arr[a]>arr[b]){
            temp=arr[b++];
            for(i= ++mid;i>a;i--){
                arr[i]=arr[i-1];
            }
            arr[a++]=temp;
        }
        else if(arr[a]<arr[b]){
            a++;
        }
        else{
            if(a==mid && b==last){
                break;
            }
            temp=arr[b++];
            a++;
            for(i= ++mid;i>a;i--){
                arr[i]=arr[i-1];
            }
            arr[a++]=temp;
        }
    }

}

void swap (int *arr, int i, int j){
    int temp;
    temp = arr[i];
    arr[i]=arr[j];
    arr[j]=temp;
}
