/*


*/

import java.util.*;
import java.io.*;
import javax.swing.*;

public class Main {
    public static void main (String[] args) throws Exception{
        InputStreamReader in = new InputStreamReader(System.in);
        BufferedReader read = new BufferedReader(in);
        //BufferedReader read = new BufferedReader(new FileReader("Main.txt"));

        int n = Integer.parseInt(read.readLine());
        Stack<String> stack = new Stack<>();
        HashMap<String,Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            String[] s = read.readLine().split(" ");
            if (Integer.parseInt(s[0]) == -1){
                if (stack.isEmpty()){
                    System.out.println("No book");
                }else {
                    String book = stack.pop();
                    System.out.println(stack.size() + " " + book);
                    map.put(book, map.get(book) - 1);
                    if (map.get(book) > 0){
                        stack.push(book);
                    }
                }
            }else {
                map.put(s[1], Integer.parseInt(s[0]));
                stack.push(s[1]);
            }
        }
    }
}