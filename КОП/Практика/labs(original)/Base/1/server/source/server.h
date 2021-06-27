#include "iserver.h"

class Server: public IServer {
	private:
	 int a;
	public:
	 Server();
	 ~Server();
	 void Func();			 
};