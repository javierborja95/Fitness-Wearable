Javier Borja

A15721796

# Lab 3

## Introduction
The objective of lab 2 is to learn a new communication protocol of BLE. Will use BLE to link two HM-10s. Our computer will communicate to a first bluetooth device using serial, that first bluetooth device will communicate with another second device, that second bluetooth device will comunicate via serial to an Arduino, and that Arduino will commuicate to an OLED display via I2C.

## Objective 1
*We used an HM-10 bluetooth module with our Arduino and tested out commands. We communicated to it and it communicated to our Serial monitor using sample code. We connected the module using a voltage divider circuit.*

* Create a voltage divider circuit.
    * We created a voltage divider circuit to step down our 5V to the HM-10's logic level of 3.3V.
* Wired the module to its respective pin on the arduino and voltage divider using the included schematic.
* Understand the included sample code and run it on the Arduino IDE.
    * The code allows text to be sent and recieved over BLE and Serial. We used it to send commands to the module and it responded to the Serial monitor.
* Try out and understand what all the AT commands do. The included picture includes the commands and their outputs.

![Objective1](/Lab3/Images/Objective1.png)

## Objective 2
*We connected two bluetooth modules and had them both communicate via BLE. Once we confirmed working modules, we soldered a connector to the protoboard.*

* Get a partner with their own module.
* Set one module using the code from Objective 1 as a Central device and set the connection mode to manual.
* Set the other module as a Peripheral device and get the device's MAC address.
* Connect the Central device to the Peripheral device with the MAC address.
* Send strings to each other saying what each device's role is (peripheral or central).
* Switch roles and repeat the last step. The two pictures show these steps.
* Solder a button and HM-10 connector pins onto the protoboard using the soldering guide.

![Objective2a](/Lab3/Images/Objective2a.png)
![Objective2b](/Lab3/Images/Objective2b.png)

## Objective 3
*In this objective we used python and the Spyder IDE to communicate via a serial console cable.*

* Install Serial console cable drivers if required.
* Connect the Serial console cable and the HM-10 BLE module to the computer.
* Understand and use the included python code. Modify it to include your Serial port.
    * This code has functions to accept inputs from Serial to python and sends inputs from python to the module using Serial, and then to BLE.

## Objective 4
*Integrate objectives 1, 2, and 3 and connect two HM-10 modules via bluetooth to communicate a computer with python to an Arduino with an OLED display.*

* Modify the sample Arduino code from Objective 1.
    * I modified it by displaying strings recieved via Serial and displaying strings sent by the HM-10 device via bluetooth to the OLED display. I did this because the Arduino will not be connected to a computer with a Serial monitor; the OLED will be the Serial montitor. I also incorperated the button on the protoboard to get the device to sleep and wake up. The device uses a lot of current so we turn it on only when we expect incoming signals.
* Connect an HM-10 just like Objective 3. I modified the python code to auto connect to the peripheral device using the MAC address from objective 2.
* Upload the Arduino code and disconnect the Arduino from a computer. Power it with an external 9V battery.
* The included video shows a working objective 4.

[Youtube video of objective 4](https://youtu.be/etBr47oJQxY)

## Conclusion
*This difficult lab was not without its problems. This was due to a new communication protocol of bluthooth and new experience with the HM-10 modules. The most difficult aspect of this lab was to connect two modules when only one is connected to a computer with a Serial monitor. I also had a problem that I could not fix by the submittion of this lab. The USB Serial connector did not work with my module/Python IDE (possibly due to drivers). My solution to this problem was to connect the HM-10 module to an external Arduino MEGA2560 and using [this reference](https://www.pjrc.com/teensy/td_libs_AltSoftSerial.html) to connect the module to the MEGA2560 while I connected the other module to the UNO and a battery.*
