PK
     J�3N               Lab2/PK
     J�3N               Lab2/Objective2/PK
     J�3N               Lab2/Objective2/PySerial/PK
     J�3N?�N�  �  %   Lab2/Objective2/PySerial/PySerial.ino#include <Time.h>

char stringRec;     //String recieved
unsigned int cTime; // Current time

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN,LOW);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if(Serial.available() > 0){
    stringRec=Serial.read()-48;//Inputs are sent as characters, subtract 48 because of ascii
    cTime=now(); //Get current time and turn on led
    digitalWrite(LED_BUILTIN,HIGH);
  }
  if(cTime+stringRec<now()) //If time recieved has passed turn off led
    digitalWrite(LED_BUILTIN,LOW);
}PK
     J�3N�w��z   z   $   Lab2/Objective2/PySerial/sketch.json{"cpu":{"name":"Arduino/Genuino Uno","com_name":"/dev/ttyACM0","fqbn":"arduino:avr:uno","flavour":"default"},"secrets":[]}PK 
     J�3N                            Lab2/PK 
     J�3N                        #   Lab2/Objective2/PK 
     J�3N                        Q   Lab2/Objective2/PySerial/PK 
     J�3N?�N�  �  %             �   Lab2/Objective2/PySerial/PySerial.inoPK 
     J�3N�w��z   z   $             N  Lab2/Objective2/PySerial/sketch.jsonPK      ]  
    