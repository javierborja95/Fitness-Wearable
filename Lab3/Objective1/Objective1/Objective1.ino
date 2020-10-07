#include <AltSoftSerial.h>
AltSoftSerial BTserial; 
 
char c=' ';
boolean NL = true;
 
void setup(){
	Serial.begin(9600);
	while(!Serial){};
	BTserial.begin(9600);  
	Serial.println("BTserial started");
}

void loop(){
	// Read from the Bluetooth module and send to the Arduino Serial Monitor
	if (BTserial.available()){
    		c = BTserial.read();
    		Serial.write(c);
	}
  
	// Read from the Serial Monitor and send to the Bluetooth module
	if (Serial.available()){
    		c = Serial.read();
 
    		// do not send line end characters to the HM-10
    		if (c!=10 & c!=13 ){  
         		BTserial.write(c);
    		}
 
    		// Copy the user input to the main window, as well as the Bluetooth module
    		// If there is a new line print the ">" character.
    		if (NL) {
          Serial.print("\r\n>");
          NL = false;
        }
    		Serial.write(c);
    		if (c==10) {
          NL = true;
        }
	}
}
