#include "server.h"

#include <iostream>
using namespace std;


Server::Server() {
  cout << "Server::Constructor" << endl;
  a = 456;
  cout << "a=" << a << endl;
}

void Server::Func() {	 	    		
  cout << "Server::Func" << endl;
  a = a + 1;
  cout << "a=" << a << endl;
}

Server::~Server() {
  cout << "Server::Destructor" << endl;  
  a = a - 2;
  cout << "a=" << a << endl;
}       		