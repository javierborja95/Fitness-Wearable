#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
//#include <Time.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define PIN 4
unsigned int second=0;   //Current seconds
unsigned int offSecond=0;//Seconds off
bool flag=true;
bool isOn=true;


void setup() {
  Serial.begin(9600);
  pinMode(PIN,INPUT_PULLUP);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.clearDisplay();
  display.display();

  display.setTextSize(4);
  display.setTextColor(WHITE);
  //display.setCursor(10, 0);
}

void loop() {
  if(!digitalRead(PIN)){
    isOn=isOn==0?1:0;
    delay(300);
  }
  if(!isOn)
    if(millis()/1000>(second+offSecond))
      offSecond++;
  if(millis()/1000>(second+offSecond)&&isOn){
    display.setCursor(10,2);
    display.clearDisplay();
    display.println(second);
    display.display();
    second++;
    flag=1;
  }
  if(flag&&isOn){
    Serial.print(second);
    Serial.print(" ");
    Serial.print(millis());
    Serial.print("\n");
    flag=0;
  }
}
