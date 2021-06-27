#include "server.h"

#include <iostream>
using namespace std;


IUnknown_* __stdcall CreateServer()
{
  cout << "Function::CreateServer" << endl;
  Server* s = new Server();
  return (IUnknown_*)(IX*)s;
}