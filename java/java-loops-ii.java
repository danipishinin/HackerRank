import java.io.*;
import java.util.*;
import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        for(int i = 1; i <= q; i++){
            int a = scan.nextInt();
            int b = scan.nextInt();
            int n = scan.nextInt();
            int count = 1;
            int aux = a;
            int aux2 = 1;
            while(count <= n){
                aux += aux2 * b;
                if(count != n)
                    System.out.print(aux + " ");
                else
                    System.out.print(aux);
                count++;
                aux2 *= 2;
            }
            System.out.println();
        }
         scan.close();
    }
}