package proj2;

public class PrioQ {
	private Node []pq;
	private int []position;
	private int size;
	public int count2;
	public PrioQ(LinkList [] ll, int []d) {
		pq = new Node[ll.length +1];
		pq[0]=null;
		position = new int[ll.length];
		size=0;
		count2=0;
	}
	
	public boolean isEmpty() {
		if(size==0) return true;
		return false;
	}
	
	public void add(Node n, int []d) {
		//printQ();
		size++;
		pq[size] = n;
		position[n.data] = size;
		fixUp(pq,size,d);
	}
	
	public Node poll(int []d) {
		Node r = pq[1];
		remove(r,d);
		return r;
	}
	
	public void fixUp(Node []H, int pos, int []d) {
		if(pos==1) return;
		int parent_idx = pos/2;
		count2++;
		if(d[H[parent_idx].data] <= d[H[pos].data]) {
			return;
		}
		swap(H,parent_idx,pos);
		fixUp(H,parent_idx,d);
	}
	
	public void fixDown(Node []H, int pos, int []d) {
		if(pos*2 > size) return;
		
		int c1 = pos*2;
		int c2 = pos*2 +1;
		
		int l_idx;
		if(c1 <= size && c2 <= size) {
			if(d[H[c1].data] <= d[H[c2].data]) {
				l_idx = c1;
			}
			else {
				l_idx = c2;
			}
		}
		else {
			l_idx = c1;
		}
		count2++;
		if(d[H[pos].data] <= d[H[l_idx].data]) {
			return;
		}
		swap(H,pos,l_idx);
		fixDown(H,l_idx,d);
	}
	
	public void swap(Node []H, int a, int b) {
		position[H[a].data] = b;
		position[H[b].data] = a;
		Node tmp = H[a];
		H[a] = H[b];
		H[b] = tmp;
	}
	
	public void remove(Node n, int []d) {
		int pos = position[n.data];
		swap(pq,pos,size);
		size--;
		fixDown(pq,pos,d);
	}
	
//	public void fixHeap(Node n, int []d2) {
//		int pos = position[n.data];
//		int parent = pos/2;
//		if(pos!=1 && d2[pq[parent].data] > d2[pq[pos].data]) {
//			fixUp(pq,pos,d2);
//		}
//		else {
//			fixDown(pq,pos,d2);
//		}
//	}
}
