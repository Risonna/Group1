#include "lib/iserver.h"

#include <iostream>
using namespace std;

int main() {	    		
	cout << "Client::Main::Start" << endl;			
	
	
	IUnknown_* s = CreateServer();

	IX* pIX = NULL;
    HRESULT_ res = s->QueryInterface(3,(void**)&pIX);
    if (res==S_OK_)
	{
		cout << "Client::Main::Success IX: " << endl;			
		pIX->Fx1();
		pIX->Fx2();
	}	
	else
    {
	   cout << "Client::Main::Error IX: " << res << endl;			
	}
	
	
	return 0;
}