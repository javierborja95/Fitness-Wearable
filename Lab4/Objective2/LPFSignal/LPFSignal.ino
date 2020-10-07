#include <Filters.h>

#define PIN A1
float freq=3.0;
float val,filtVal;

//FilterOnePole lpf(LOWPASS, freq);
FilterTwoPole lpf(LOWPASS, freq);

void setup() {
 Serial.begin(9600);
}

void loop() {
  val=analogRead(PIN);
  filtVal=lpf.input(val);

 Serial.print(val);
 Serial.print(" ");
 Serial.println(filtVal);
}
