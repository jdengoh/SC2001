package lab2;

import java.util.LinkedList;
import java.util.Random;

public class Graph {
	
	int V;
	int E;
	LinkedList<Edge>[] ll;
	int adjM[][];
	
	public Graph(int V) {
		
		this.V = V;
		ll = new LinkedList[V];
		adjM = new int[V][V];

		//initialise
		for(int i = 0; i< V; i++) {
			
			ll[i] = new LinkedList<Edge>();
			
			for (int j=0; j<V; j++) {
				adjM[i][j] = -1;
			}
		}
	}
	
	public Graph(int maxV, int maxW, int sparse) {
		
		if (sparse == 0) {
			
			Random rand = new Random();
			
			do {
				this.V = rand.nextInt(maxV);
			}while (this.V<2);
			
			
		}
		
		
	}
	
	
	
	
	
	
}
