package server;
 

public class ServerFactory {

 public static IServer CreateInstance() {
    return new Server();
 } 
 
}
