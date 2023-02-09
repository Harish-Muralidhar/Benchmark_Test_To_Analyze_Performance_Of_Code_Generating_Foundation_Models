/*
*/

import java.util.*;
import java.io.*;


class HarryPotter{

	public static void main(String[] args) throws Exception{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PrintWriter out = new PrintWriter(System.out);
		
		String[] input = br.readLine().split(" ");
		int n = Integer.parseInt(input[0]);
		//int k = Integer.parseInt(input[1]);
		
		Pair pair = null;
		Stack<Pair> stack = new Stack<Pair>();
		String[] num;
		String name;
		for(int i = 0; i < n; i++){
			input = br.readLine().split(" ");
			if(input[0].equals("-1")){
				pair = stack.peek();
				out.println(pair.num);
				out.println(pair.name);
				stack.pop();
			}else{
				num = input[0].split("");
				name = input[1];
				Pair p = new Pair(num.length, name);
				stack.push(p);
			}
		}

		out.flush();
	}

	static class Pair implements Comparable<Pair>{
		int num;
		String name;

		public Pair (int num, String name){
			this.num = num;
			this.name = name;
		}
		public int compareTo(Pair p){
			int result = this.name.compareTo(p.name);
			if(result != 0){
				return result;
			}else{
				return this.num - p.num;
			}
		}

	}
}