import serial, sys
from time import sleep

def read_BLE( ser ):
    msg = ""
    if( ser.in_waiting > 0 ):
        msg = ser.readline( ser.in_waiting ).decode('utf-8')
    return msg

def write_BLE( command, ser ):
    ser.write( command.encode('utf-8') )
    return

with serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1) as ser:
 
    while(True) :
        command = input("Either (1) hit ENTER to read BLE, (2) send an AT command, (3) or press q to exit: ")

        if( command == "") :
            print( "> " + read_BLE(ser) )
        
        elif (command == 'q' or command == 'Q'):
            print("Goodbye")
            sys.exit(0)

        else:
            write_BLE( command, ser )
            sleep(0.5) # wait for a response
            print( "> " + read_BLE(ser) )