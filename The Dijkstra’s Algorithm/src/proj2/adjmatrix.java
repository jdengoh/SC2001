package proj2;

import java.util.Random;
import java.io.IOException;
import java.io.PrintWriter;

public class adjmatrix {
	private static int count1;
	private static int count2;
	private static int E;
	public static int [][] createRandomGraph(int numsNode, int numsEdge){
		E=0;
		int [][] g = new int[numsNode][numsNode];
		Random random = new Random();
		for(int m=0;m<numsNode;m++) {
			for(int n=0;n<numsNode;n++) {
				g[m][n]= -1;
			}
		}
		for(int i=0;i<numsNode;i++) {
			if(E >= numsEdge) break;
			for(int j=0;j<numsNode;j++) {
				if(E>=numsEdge)break;
				if(i==j) {
					continue;
				}
				// random = max - (min) + min
				g[i][j]=random.nextInt(numsNode - (-1))+(-1);
				if(g[i][j]>0) E++;
			}
		}
		return g;
	}
	
	public static LinkList[] ArrayLL(int matrix[][]) {
		return createLL.createArrayLL(matrix);
	}
	
	public static int[] D_Array(int [][] matrixE, int source) {
		int V = matrixE[0].length;
		int []d = new int[V];
		int []S = new int[V];
		int []pi = new int[V];
		for(int a=0;a<V;a++) {
			d[a]=999999999;
			pi[a] = -1;
			S[a] = 0;
		}
		d[source]=0;
		Node [] pq = new Node[V];
		for(int i=0;i<V;i++) {     
			Node tmp = new Node();
			tmp.data = i;
			pq[i] = tmp;
		}
		//System.outprintln("");
		for(int j=0;j<V;j++) {   
			int min = findMin(pq,d,S); 
			if(min == -1) continue;
			S[min]=1;
			//System.out.printf("%d ",min);
			for(int i=0;i<matrixE[min].length;i++) {
				if(matrixE[min][i]<=0) continue;
				if(S[i]!=1 && d[i]>d[min]+matrixE[min][i]) {
					//remove node
					pq[i] = null;
					d[i]=d[min]+matrixE[min][i];
					pi[i]=min;
					
					//add back
					Node tmp = new Node();
					tmp.data = i;
					pq[i] = tmp;
				}
			}
		}
		return d;
		
	}
	
	public static int findMin(Node []pq, int []d, int []S) {
		int min = 9999999;
		int ans = -1;
		for(int i=0;i<pq.length;i++) {
			count1++;
			if(S[i]!=1 && d[pq[i].data] <= min && d[pq[i].data]!= -1) {
				min = d[pq[i].data];
				ans = i;
			}
		}
		return ans;
	}
	
	public static int[] D_LinkList(LinkList [] arrLL, int source) {
		int V = arrLL.length;
		int []d = new int[V];
		int []pi = new int[V];
		int []S = new int[V];
		for(int a=0;a<V;a++) {
			d[a] = 9999999;
			pi[a] = -1;
			S[a]=0;
		}
		d[source]=0;
		PrioQ pq = new PrioQ(arrLL,d);
		for(int i=0;i<arrLL.length;i++) {
			pq.add(arrLL[i].head, d);
		}
		
		while(!pq.isEmpty()) {
//			for(int i=0;i<V;i++) {
//				if(S[i]!=1)
//					System.out.printf("%d=%d ",i,d[i]);
//			}
//			System.out.println("");
//			pq.printQ();
			Node u = pq.poll(d);
			S[u.data]=1;
			Node tmp = arrLL[u.data].head.next;
			while(tmp!=null) {
				if(S[tmp.data]!=1 && d[tmp.data]>d[u.data]+tmp.weight) {
					pq.remove(tmp, d);
					d[tmp.data]=d[u.data]+tmp.weight;
					pi[tmp.data] = u.data;
					pq.add(tmp, d);
				}
				tmp = tmp.next;
			}
		}
		count2 = pq.count2;
		return d;
	}
	
	public static void printGraph(int [][]matrix) {
		int g = matrix.length;
		int i,j;
		String txt ="i,j  |";
		txt = String.join("\u0332",txt.split("",-1));
		System.out.print(txt);
		System.out.printf("");
		
		for(j=0;j<g;j++) {
			System.out.printf("\u0332%3d\u0332 \u0332 \u0332|",j);
		}
		System.out.println("");
		
		for(i=0;i<g;i++) {
			System.out.printf("\u0332%3d\u0332 \u0332 \u0332|",i);
			for(j=0;j<g;j++)
				System.out.printf("\u0332%3d\u0332 \u0332 \u0332|",matrix[i][j]);
			System.out.println("");
		}
	}
	
	public static void printLL(LinkList [] arr) {
		for(int i=0;i<arr.length;i++) {
			Node tmp = arr[i].head;
			while(tmp!=null){
				System.out.printf("%d ",tmp.data);
				tmp = tmp.next;
			}
			System.out.println("");
		}
	}
	
	public static void printTree(int []arr) {
		for(int i=0;i<arr.length;i++) {
			System.out.printf("%3d ", i);
		}
		System.out.println();
		for(int i=0;i<arr.length;i++) {
			System.out.printf("%3d ",arr[i]);
		}
		System.out.println();
	}
	
	
	public static void main(String[] args) {
		E=0;
		int i=5;
		int j=10;
		int source =0;
		int [][] matrix = createRandomGraph(i,j);
		printGraph(matrix);
		
		LinkList []ll = ArrayLL(matrix);
		printLL(ll);
		
		count1=0;
		long D_arrS=System.nanoTime();
		int [] ans = D_Array(matrix,source);
		long D_arrE = System.nanoTime();
		long D1_t = D_arrE - D_arrS;
		printTree(ans);
		
		LinkList [] arrLL = ArrayLL(matrix);
		long D_LLS = System.nanoTime();
		int [] ans2 = D_LinkList(arrLL,source);
		long D_LLE = System.nanoTime();
		long D2_t = D_LLE - D_LLS;
		printTree(ans2);
		
		System.out.printf("V = %d, E = %d\n", i, E);
		
		System.out.printf("ADJ_Matrix with Array Queue (FindMin Unordered) (Operations = %d, Time = %d ns)\n",count1,D1_t);
		System.out.printf("ADJ_LinkList with Min_Heap Queue                (Operations = %d, Time = %d ns)\n",count2, D2_t);
		

	}
}
