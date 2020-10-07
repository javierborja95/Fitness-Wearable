# Imports
import ece16bt as bt
import serial, sys
from time import sleep

# Global variables
MAC = "A810871B48DE"
#MAC=6CC374FCAD6F
with serial.Serial(port="/dev/ttyACM1", baudrate=9600, timeout=1) as ser:
    bt.setup_BLE(ser, MAC)

    while(True):

            command = input("Either (1) hit ENTER to read BLE, (2) send an AT command, or (3) press q to exit: ")

            if( command == "") :
                   msg = bt.read_BLE(ser)
                   #checks if a connection has been broken recently, and calls reconnect_BLE()
                   if(msg == "OK+LOST"):
                       bt.reconnect_BLE(ser, MAC)
                   else:
                       print( "> " + msg )
            
            elif(command == 'q' or command == 'Q'):
                    print("Goodbye")
                    sys.exit(0)

            else:
                    bt.write_BLE( command, ser )
                    sleep(0.5) # wait for a response
                    print( "> " + bt.read_BLE(ser) )
