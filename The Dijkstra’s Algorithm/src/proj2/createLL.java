package proj2;

public class createLL {
	//return array adjlist representation
	public static LinkList[] createArrayLL(int matrix[][]) {
		LinkList [] arrLL = new LinkList[matrix[0].length];
		for(int i=0;i<matrix[0].length;i++) {
			Node head = new Node();
			head.data = i;
			head.weight = 0;
			head.next = null;
			LinkList l = createLink(head,matrix[i]);
			arrLL[i] = l;
		}
		return arrLL;
	}
	
	
	public static LinkList createLink(Node n, int matrix[]) {
		LinkList ll = new LinkList(n);
		for(int j=0;j<matrix.length;j++) {
			if(matrix[j]<=0) continue;
			Node a = new Node();
			a.data = j;
			a.weight = matrix[j];
			a.next = null;
			ll.insertNode(a);
		}
		return ll;	
	}
}
