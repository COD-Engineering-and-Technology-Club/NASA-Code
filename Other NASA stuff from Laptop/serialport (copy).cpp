#include "SerialPort.h"

int main()
{
	SerialPort sp("/dev/ttyACM0", 115200);
	for (int i = 0; i< 500; i++)
		sp.write("!G1 500/r", 10);



	return 0;


}
