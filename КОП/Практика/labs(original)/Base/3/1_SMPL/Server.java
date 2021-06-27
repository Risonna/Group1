public class Server {

 private int a=5;
 private int b=10;
 private int c=25;

 public Server() {
	a=13; 
 }

 public Server(int la) {
	a=la; 
 }
 
 public void print() {
   int res = a+b+c;	 
   System.out.println("a+b+c=" + res);	 
 }	 
	
}
