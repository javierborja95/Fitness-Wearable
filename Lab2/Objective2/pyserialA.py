import serial

with serial.Serial('/dev/ttyACM0',9600, timeout=1) as ser:
    print(ser.name)
    while(True):
        message=input()
        if message=="STOP" or message=="START":
            ser.write(message.encode('utf-8'))
        else:
            print("Not valid input")