#include <AltSoftSerial.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
AltSoftSerial BTserial;

char c=' ';
bool isOn=true;
int lastButtonState = LOW;
int buttonState = LOW;
bool NL = true;
long lastButtonPress = 0;
const int buttonPin = 4;
bool didDisplay=false;
String message="";

void setup() {
  Serial.begin(9600);
  BTserial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.clearDisplay();

  display.setTextSize(2);
  display.setTextColor(WHITE);
  Serial.write("TEST");
  display.println(F("BTserial\nstarted"));
  display.display();
  Serial.print("BTserial started\n");
  delay(2000);
}

void loop() {
  // Read from the Bluetooth module and send to the Arduino Serial Monitor
  if (BTserial.available())
  {
        c = BTserial.read();
        message+=c;
        Serial.write(c);
        
  }
  
  // Read from the Serial Monitor and send to the Bluetooth module
  else if (Serial.available())
  {
        c = Serial.read();
        message+=c;
        
        // do not send line end characters to the HM-10
        if (c!=10 & c!=13 )
        {  
            BTserial.write(c);
        }

 
        // Copy the user input to the main window, as well as the Bluetooth module
        // If there is a new line print the ">" character.
        if (NL) 
        {
            Serial.print("\r\n>");
            delay(200);
            display.clearDisplay();
            display.setCursor(10, 0);
            display.println((">"));
            display.display();
            delay(2000);
            NL = false;
        }
        Serial.write(c);
        if (c==10) 
        {
            NL = true;
        }
  }else{
        display.clearDisplay();
        display.setCursor(10, 0);
        display.println((message));
        display.display();
        delay(2000);
        message="";
  }
  if(!digitalRead(buttonPin)){
    delay(100);
    isOn=isOn==0?1:0;
        if(isOn){
          Serial.println("Waking up!\n");
          display.clearDisplay();
          display.setCursor(10, 0);
          display.println(F("Waking"));
          display.display();
          delay(2000);
          BTserial.print("AT+hailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsinhailramsin");
          delay(350);
          BTserial.print("AT+ADTY0");
          delay(50);
          BTserial.print("AT+RESET");
        }else{
          Serial.print("Going to sleep\n");
          display.clearDisplay();
          display.setCursor(10, 0);
          display.println(F("Sleeping"));
          display.display();
          delay(2000);
          BTserial.print("AT");
          delay(150);
          BTserial.print("AT+ADTY3");
          delay(50);
          BTserial.print("AT+SLEEP");
        }
  }
}
