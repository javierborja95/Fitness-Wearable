# Imports
import serial, sys
from time import sleep

r_MAC=""

# Function to read from the BLE module and display to serial
# Inputs: Serial handler
# Return: The String message that has been read
def read_BLE( ser ):
    msg=""
    if(ser.in_waiting>0):
        msg=ser.readline(ser.in_waiting).decode('utf-8')
    return msg


# Function to read from serial and send to BLE module
# Inputs: Command/Text to be written to BLE, Serial handler
# Return: None
def write_BLE( command, ser ):
    ser.write(command.encode('utf-8'))



# Function to setup BLE for the first time. 
# Inputs: Serial handler, Peripheral MAC Address
# Return: None
def setup_BLE( ser, receiver_MAC ):
    r_MAC=receiver_MAC
    write_BLE('AT', ser)
    sleep(1)
    write_BLE('AT', ser)
    sleep(1)
    write_BLE('AT', ser)
    sleep(1)
    write_BLE('AT+CON' + receiver_MAC, ser)
    


# Function to re-establish connection when broken
# Inputs: Serial handler, Peripheral MAC Address
# Return: None
def reconnect_BLE (ser):
    write_BLE('AT', ser)
    sleep(1)
    write_BLE('AT+CON' + r_MAC, ser)