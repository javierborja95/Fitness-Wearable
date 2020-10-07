import serial, sys
import time
import numpy as np
import matplotlib.pyplot as plt

def read_writefrom_BLE( ser ):
    i=0;
    f=open("raw_data.npy","w+")
    msg = ""
    cTime=time.time()
    while (cTime+20>time.time()):
        if( ser.in_waiting > 0 ):
            msg = ser.readline( ser.in_waiting ).decode('utf-8')
            f.write(msg+"\r")
    f.close()
    
    with open("raw_data.npy") as f:
        lines=f.readlines()
        x=[line.split()[0] for line in lines]
        y=[line.split()[1] for line in lines]
    
        plt.plot(x,y)
        plt.show()
    
def read_BLE( ser ):
    msg = ""
    if( ser.in_waiting > 0 ):
        msg = ser.readline( ser.in_waiting ).decode('utf-8')
    return msg

def write_BLE( command, ser ):
    ser.write( command.encode('utf-8') )
    return

def flush( ser ):
    while(ser.in_waiting):
        ser.reset_input_buffer()

with serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=1) as ser:
 
    while(True) :
        command = input("Either (1) hit ENTER to read BLE (4) w to write (5) c to connect (2) q to exit (3) f to reset input buffer\n")

        if( command == "") :
            print( "> " + read_BLE(ser) )
        elif ( command == "w" or command=="W") :
            print("Writing to file\n")
            read_writefrom_BLE(ser)
        elif (command== "f" or command=="F"):
            flush(ser)
            print("Flushing serial\n")
        elif (command == 'c' or command == 'C'):
            write_BLE( 'AT+CONA810871B48DE', ser)
        elif (command == 'q' or command == 'Q'):
            print("Goodbye")
            sys.exit(0)
        else:
            write_BLE( command, ser )
            sleep(0.5) # wait for a response
            print( "> " + read_BLE(ser) )