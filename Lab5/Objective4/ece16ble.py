# Imports
import serial
from time import sleep

ble_peripheral_MAC = ""
ble_conn = None

# Function to setup BLE for the first time
# Inputs:
#   conn - Serial connection with BLE module
#   mac - MAC address of the receiver BLE module (the Peripheral)
# Return: None
def ble_setup( serial_port, mac ) :
  global ble_conn, ble_peripheral_MAC
  ble_conn = serial.Serial(port=serial_port, baudrate=9600, timeout=1)
  ble_peripheral_MAC = mac

  ble_set_central()
  return

# Function to establish the module as a Central device
# Inputs: None
# Return: None
def ble_set_central( ) : 
  finished = False
  step = 0
  ble_write("AT")

  while (not finished) :
    status = ble_read_buffer()

    if (status.find("PeripheralConnected") >= 0) :
      print("Connection already established, bypassing setup")
      break

    if (status.find("OK+Set:1") >= 0) :
      step += 1

    if (step == 0) :
      ble_write("AT+IMME1")
      print("Setting connection mode")
      sleep(0.5)
    elif (step == 1) :
      ble_write("AT+NOTI1")
      print("Setting notification mode")
      sleep(0.5)
    elif (step == 2) :
      ble_write("AT+ROLE1")
      print("Setting BLE role")
      sleep(0.5)
    else :
      print("Setup completed successfully")
      finished = True
  return

# Function to connect the BLE to the Peripheral
# Inputs: None
# Return: None
def ble_connect() :
  finished = False
  step = 0
  while(not finished) :
    status = ble_read_buffer()
    
    if (status.find("PeripheralConnected") >= 0) :
      print("Connection established and confirmed")
      break

    if (status.find("OK+CONNAOK+CONN") >= 0) :
      step += 1
    
    if (step == 0) :
      ble_write("AT+CON" + ble_peripheral_MAC)
      print("Connecting to peripheral: ", ble_peripheral_MAC)
      sleep(0.5)
    else :
      ble_write("AT+NAME?")
      print("Confirming connection handshake")
      finished=True
      sleep(0.5)
  return

# Function to read the buffer from the BLE module and return it as a string
# Return: The String message that has been read (or an empty string if nothing was read)
def ble_read_buffer() :
  msg = ""
  if( ble_conn.in_waiting > 0 ) :
    msg = ble_conn.readline( ble_conn.in_waiting ).decode("utf-8")

  #checks if a connection has been broken and tries to automatically reconnect
  if(msg.find("OK+LOST") >= 0) :
    ble_connect()
  return msg

# Read a line one character at a time until a delimiter
# Inputs: eol - the delimiter to use (default is '\n')
# Note: Assumes that there is a '\n' termination or else this function will hang until timeout
def ble_read_line(eol='\n') :
  line = ""
  while( True ) :
    c = ble_conn.read(1).decode("utf-8")
    if (c == eol ):
      break
    line += c

  return line

# Function to write a string to the BLE module
# Inputs: message - String to be written to BLE
# Return: None
def ble_write( message ) :
  ble_conn.write( message.encode("utf-8") )
  return

# Function to close the BLE Serial connection since we are not using "with" functionality
# Inputs: none
# Return: None
def ble_close() :
  ble_conn.close()
  return