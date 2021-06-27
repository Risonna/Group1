package server;
 

class Server implements IServer, IServer2 {

 private int a; 
 private int b; 


 public Server() {
	a=5; 
	b=10;
 }
 
 public void print() {
   int res = a;	 
   System.out.println("Result: " + res);	 
 }

 public void print2() {
   int res = b;	 
   System.out.println("Result2: " + res);	 
 } 

 
}
