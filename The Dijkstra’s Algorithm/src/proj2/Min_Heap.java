package proj2;

public class Min_Heap {
	//create heap
	private int[] Heap;
	public Min_Heap(LinkList [] ll, int []d) {
		Heap = new int[ll.length];
		for(int i=0;i<ll.length;i++) {
			Heap[i] = ll[i].head.data;
		}
	}
	
	public static void heapify(int []H, int root)
	{
		int a = (root+1)*2;
		if(a > H.length) {
			return;
		}
	
		heapify(H,a-1);
		heapify(H,a);
	
		fixHeap(H,H.length-1,root,H[root]);
	}
	
	public static void heapSort(int []arr) {
		heapify(arr,0);
		for(int i=arr.length-1;i>=1;i--) {
			int max = arr[0];
			deleteMax(arr,i);
			arr[i]=max;
		}
	}
	
	public static void deleteMax(int [] arr, int n) {
		//delete the rightmost in the array
		int k = arr[n];
		fixHeap(arr,n-1,0,k);
	}
	
	public static void fixHeap(int []H, int high, int E, int k) {
		int e = E+1;
		if(e*2 > high+1) {
			H[e] = k;
			return;
		}
		
		// case 1: E has two child
		int c1 = e*2 -1;
		int c2 = e*2;
		int small,l_idx;
		
		if(c1<=high && c2<=high) {
			if(H[c1]<=H[c2]) {
				small = H[c1];
				l_idx = c1;
			}
			else {
				small = H[c2];
				l_idx = c2;
			}
		}
		// case 2: E has only one child
		else {
			small = H[c1];
			l_idx = c1;
		}
		
		if(k<=small) {
			H[E]=k;
			return;
		}
		
		H[E] = small;
		fixHeap(H,high,l_idx,k);
		
	}
}
