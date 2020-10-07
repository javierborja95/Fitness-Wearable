#include <AltSoftSerial.h>
AltSoftSerial BTserial; 

const int buttonPin = 2; //NOTE: Change to the pin where your button is connected
boolean asleep = false;
int buttonState = HIGH;
boolean confirmedCentral = false;

void setup()
{
  pinMode(buttonPin, INPUT_PULLUP);

  BTserial.begin(9600);
//  Serial.begin(9600);
//  while(!Serial){};
}

void loop()
{
  // If Central BLE is sending data or connection commands
  if (BTserial.available()) {
    String message = "";
    delay(100); // wait for full message
    while (BTserial.available()) {
      message = message + char(BTserial.read());
    }

    // Python sending AT commands
    // NOTE: if we wanted, we could also receive data
    if(message.indexOf("AT") != -1) {
      BTserial.write("PeripheralConnected");
      confirmedCentral = true;
    }
  }

  // Send data to the Central BLE if we are not asleep
  else if (confirmedCentral && !asleep) {
    //----------------------------------------
    // JUST AN EXAMPLE SENDING ANALOG READINGS SEPARATED BY SPACE!!!
    int val = analogRead(A1);
    String thestr = String(val) + " ";
    BTserial.print(thestr.c_str());
//    Serial.print(thestr.c_str());
    //----------------------------------------
  }

  //Upon button press, disconnect/reconnect BLE
  //Debounce the button for more stable code
  if(digitalRead(buttonPin) != buttonState) {
    buttonState = !buttonState;
    
    //Disconnect and put to sleep
    if(buttonState == HIGH && asleep == false) {
      // Serial.print("Going to sleep");
      confirmedCentral = false;
      BTserial.print("AT");
      delay(150);
      BTserial.print("AT+ADTY3");
      delay(50);
      BTserial.print("AT+SLEEP");
      delay(50);
      asleep = true;
    }
    //Wake up and re-establish connection 
    else if(buttonState == HIGH && asleep == true) {
      // Serial.println("Waking up!");
      BTserial.print("AT+hailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsin");
      delay(350);
      BTserial.print("AT+ADTY0");
      delay(50);
      BTserial.print("AT+RESET");
      delay(50);
      asleep = false;
    }
  }
}
