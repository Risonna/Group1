#include "lib/iserver.h"

#include <iostream>
using namespace std;

int main() {	    		
	cout << "Client::Main" << endl;			
	
	IServer* s = CreateServer();
	s->Func();
	//delete s;
	
	return 0;
}