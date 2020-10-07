PK
     0�3N               Lab2/PK
     0�3N               Lab2/Objective1/PK
     0�3N               Lab2/Objective1/MyBlink/PK
     0�3N��>�    #   Lab2/Objective1/MyBlink/MyBlink.inoint counter=0;    //Indicates the amount of times loop() is called
bool isOn=true;   //Flag for play/pause
String stringRec; //String recieved

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  if(isOn){
  //Counter
    counter++;
    Serial.print("Loop has been called ");
    Serial.print(counter);
    counter>1?Serial.print(" times.\n"):Serial.print(" time.\n");
  
  //Blink
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(2000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(500);                        // wait for a second
  }
  
  // Play/Pause
  if(Serial.available() > 0){
    stringRec=Serial.readStringUntil('\n');
    if(isOn){
      if(stringRec=="STOP")
        isOn=false;
    }
    else
      if(stringRec=="START")
        isOn=true;
      
  }
}PK
     0�3N�w��z   z   #   Lab2/Objective1/MyBlink/sketch.json{"cpu":{"name":"Arduino/Genuino Uno","com_name":"/dev/ttyACM0","fqbn":"arduino:avr:uno","flavour":"default"},"secrets":[]}PK 
     0�3N                            Lab2/PK 
     0�3N                        #   Lab2/Objective1/PK 
     0�3N                        Q   Lab2/Objective1/MyBlink/PK 
     0�3N��>�    #             �   Lab2/Objective1/MyBlink/MyBlink.inoPK 
     0�3N�w��z   z   #             �  Lab2/Objective1/MyBlink/sketch.jsonPK      Y  �    