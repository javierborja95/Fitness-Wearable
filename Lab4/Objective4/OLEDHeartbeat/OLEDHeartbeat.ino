#include <AltSoftSerial.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Filters.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
AltSoftSerial BTserial; 
char c=' ';
bool isOn=true;
char message[10]="";
bool NL = true;
const int buttonPin = 4;
int flag=0;
int j=0;


int PIN =1;
float freq=3.0;
float val,filtVal;
int cast;
float lowestVal=0;
float highestVal=0;

unsigned int ct=0;
unsigned int period=10;
unsigned int nt,r;

//FilterOnePole lpf(LOWPASS, freq);
FilterTwoPole lpf(LOWPASS, freq);
FilterDerivative fd;

void setup() {
   Serial.begin(9600);
   while(!Serial){};
   BTserial.begin(9600);
   if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
      Serial.println(F("SSD1306 allocation failed"));
      for(;;); // Don't proceed, loop forever
   }
   display.setTextSize(2);
   display.setTextColor(WHITE);
   r=15; //Radius
   nt=ct+period;
   calibrate();
   //connct();
}

void loop() {
  val=analogRead(PIN);
  filtVal=transformation2(val);
  //dtostrf(filtVal,8,4,message);
  filtVal=(filtVal<lowestVal)?lowestVal:(filtVal>highestVal)?highestVal:filtVal;
  circle(filtVal);
  Serial.println(filtVal);

  BTserial.print(j);
  BTserial.print(" ");
  BTserial.print(val);
  BTserial.print("\r");
  j++;
}

float transformation1(float v){
  return fd.input(lpf.input(v));
}

float transformation2(float v){
  return lpf.input(fd.input(lpf.input(v)));
}


void circle(int val) {
  display.clearDisplay();
  display.drawCircle(display.width() / 2, display.height() / 2, r, WHITE);
  display.fillCircle(display.width() / 2, display.height() / 2, r*(val-lowestVal)/period, WHITE);
  display.display(); // Update screen with each newly-drawn circle

  delay(200);
}

void calibrate(){
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.print("CALIBRATING\nHOLD STILL");
  display.display();
  getLow();
  getHigh();

  period=highestVal-lowestVal;
  lowestVal+=period*.7;
  highestVal-=period*.2;
  period=highestVal-lowestVal;
  delay(1000);
}

void getLow(){
  float temp,v;
  for(int i=0;i<5;i++){
    temp=transformation2(analogRead(PIN));
    Serial.println(temp);
    ct=millis()/1000;
    while((ct+3)>(millis()/1000)){
      
      v=transformation2(analogRead(PIN));
      Serial.println(v);
      if(v<temp)
        temp=v;
    }
    lowestVal+=temp;
  }
  Serial.println(lowestVal);
  lowestVal=lowestVal/5.0;
  Serial.println(lowestVal);
}

void getHigh(){
  float temp,v;
  for(int i=0;i<5;i++){
    temp=transformation2(analogRead(PIN));
    Serial.println(temp);
    ct=millis()/1000;
    while((ct+3)>(millis()/1000)){
      v=transformation2(analogRead(PIN));
      Serial.println(v);
      if(v>temp)
        temp=v;
    }
    highestVal+=temp;
  }
  Serial.println(highestVal);
  highestVal=highestVal/5.0;
  Serial.println(highestVal);
}

void connct(){
  do{
    if(flag<5){
      flag++;
      BTserial.write("AT");
      delay(100);
    }
    if (flag>4) flag++;
    if(flag==1000){
      BTserial.write("AT+NAME?");
      delay(1000);
    }
    if(flag==2000){
      BTserial.write("AT+CON6CC374FCAD6F");
      delay(1000);
    }
    // Read from the Bluetooth module and send to the Arduino Serial Monitor
    //BTserial.write('A');
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
  }while(flag<10000);
  delay(1000);
}
