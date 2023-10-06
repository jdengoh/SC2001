package proj2;

public class LinkList {
	public Node head;
	public int size;
	public LinkList(Node h) {
		head = h;
		size = 0;
	}
	
	public boolean isEmpty(LinkList a) {
		if(size==0)
			return true;
		return false;
	}
	
	public void insertNode(Node n) {
		if(head==null) {
			head = n;
			return;
		}
		Node tmp = head;
		Node pre = tmp;
		do {
			pre = tmp;
			tmp = tmp.next;
		}while(tmp!=null);
		pre.next = n;
		size++;
		return;
	}
	
	public void removeNode(Node n) {
		Node tmp = head;
		Node pre = tmp;
		while(tmp!=null) {
			if(n.data == tmp.data) break;
			pre = tmp;
			tmp = tmp.next;	
		}
		
		if(pre == head) {
			head = pre.next;
			head = null;
			return;
		}
		pre.next = tmp.next;
		tmp = null;
		size--;
	}
	
	public void printLL() {
		Node tmp = head;
		while(tmp!=null) {
			System.out.printf("%d ",tmp.data);
			tmp = tmp.next;
		}
		System.out.println("");
	}
}
