package client;

import server.IServer;
import server.IServer2;
import server.ServerFactory;

public class Client {

 public static void main(String[] args) {    	
 
   IServer s = ServerFactory.CreateInstance();     
   try {	
    IServer2 s2 = (IServer2)s;
	System.out.println("Using new interface...");
	s2.print2();   
   }	
   catch (Exception e) {    
    System.out.println("Using old interface...");
    s.print();     
   } 	 
 }	 
	
}
