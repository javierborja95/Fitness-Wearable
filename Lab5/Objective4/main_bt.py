# Imports
import ece16ble as bt
import serial, sys
from time import sleep

# Global variables
serial_port = "/dev/ttyACM3"
peripheral_MAC = "A810871B48DE"
#peripheral_MAC = "6CC374FCAD6F"
# centralMAC = "A810871B347B"

if ( __name__ == "__main__" ) :
  try:
    bt.ble_setup( serial_port, peripheral_MAC )

    bt.ble_connect()

    # ---------------------------------------------------------------------------
    # JUST AN EXAMPLE TO READ A LINE FROM BLE SEPARATED A SPACE AND PRINT IT OUT
    # DEFINITELY CHECK THE CONTENTS OF WHAT WAS RECEIVED WHEN PROCESSING!!! 
    while( True ):
      new_val = bt.ble_read_line(" ")
      if (len(new_val)) :
        print(" >> " + new_val)
    # ---------------------------------------------------------------------------

  except Exception as e:
    print("Error: " + str(e))
    bt.ble_close()