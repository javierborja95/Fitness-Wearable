Javier Borja

A15721796

# Lab 2

## Introduction
The objective of lab 2 is to introduce us to communication links and specifically to communicate with python and the arduino by the use of the serial monitor and from the Arduino to a display by the use of I2C. This lab also gave more soldering experience and introduced us to an OLED and a pullup resistor button circuit.

## Objective 1
*We used the Serial monitor to communicate to the Arduino and for the Arduino to give the user information. We controlled an LED by instructing it by the use of Serial.*

* Test and understand the Arduino Blink example code
    * This code works by setting the built-in LED pin as an output pin. An output value of HIGH turns on the LED and an output value of LOW turns it off. The delay(n) function stops all Arduino activity and processing for n milliseconds.
* Modified the example code such that a counter counts the amount of times the LED blinks on and off. We printed the result to the Serial Monitor.
* Modified it once more such that inputting the strings, "START" and "STOP", starts and stops the blinking.

## Objective 2
*We used Serial to communicate to the Arduino by implementing with the Python programming language.*

#### Part A:
* Used the MyBLink.ino sketch from Objective 1 and constructed a Python module that sent "START" or "STOP" via Serial, depending on our input.
    * We endcoded the message as UTF-8 string
#### Part B:
*  Used the random library on Python to create a number from 1-9 and sent it to the Arduino via Serial and we made this repeat every 30 seconds.
*  We created an Arduino sketch that receives the numbers and turns on the built-in LED for that many seconds.

## Objective 3
*This objective introduced us to the I2C communication protocal to communicate through an OLED display. (I did part B before part A)*

#### Part B:
* Soldered headerpins and an OLED display into a protoboard.
![Soldered board](/Lab2/Images/solder.jpg)
#### Part A:
* Installed the libraries required for the I2C communication and the OLED display.
* Understand the example code so that I could create my own custom text with my initials.
![Initials](/Lab2/Images/initials.jpg)

## Objective 4
*Utilize our experience with the Arduino and OLED display to create a stopwatch with user interface. We also learned about pull-up and pull-down circuits.*

* Built a pull-up resistor circuit with a button.
* Created a sketch that displays a second timer on the OLED and pauses the timer with the button input.
* We recreated the above step by removing the pull-up resistor and using the Arduino's built in pull-up pins.

[Youtube video of objective 4](https://youtu.be/8QUxBAe-7mA)

## Conclusion
*This lab went fairly well except that I had trouble communicating with the Arduino via Serial and Python. My problem was that I was not able to send in information quickly, and that there would be a sort of "queue" of information that took time to process. I assume this is why __Objective 2__ had us repeat the process every thirty seconds, to let the Arduino process the numbers sent. This lab will prepare me for user interface and communication.*
