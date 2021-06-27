@rem g++ -c ./client/source/client.cpp -o ./client/build/client.o
g++ ./client/build/client.o ./client/build/lib/iserver.o ./client/build/lib/server.o    -o ./client/build/client.exe

"client/build/client.exe"

pause