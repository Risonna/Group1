#include "server.h"

#include <iostream>
using namespace std;


IServer* CreateServer() {
  cout << "Function::CreateServer" << endl;
  return new Server();
}