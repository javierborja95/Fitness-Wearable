import serial
import random
import time

with serial.Serial('/dev/ttyACM0',9600) as ser:
    '''Necessary delay for program'''
    cTime=time.time()
    while (cTime+5>time.time()): 
        pass
    
    while(True):
        cTime=time.time() #Get Current time
        sent=str(random.randrange(9)+1) # sent= random number from 1-9
        print(sent)
        ser.write(sent.encode('utf-8')) # Send random number to arduino
        
        '''Do nothing for 30 seconds'''
        while (cTime+30>time.time()): 
            pass