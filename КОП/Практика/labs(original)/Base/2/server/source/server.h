#ifndef SERVER_H_INCLUDED
#define SERVER_H_INCLUDED

#include "iserver.h"

class Server: public IX, public IY {
	private:
	 int a;
	 int b;
	public:
	 Server();
	 ~Server();

	 virtual HRESULT_ __stdcall QueryInterface(const IID_& iid, void** ppv);

	 virtual HRESULT_ __stdcall Fx1();
	 virtual HRESULT_ __stdcall Fx2();

	 virtual HRESULT_ __stdcall Fy1();
	 virtual HRESULT_ __stdcall Fy2();
};

#endif // SERVER_H_INCLUDED