/* FFT reference: https://www.norwegiancreations.com/2017/08/what-is-fft-and-how-can-you-implement-it-on-an-arduino/ */

#include <arduinoFFT.h>
#include <Filters.h>
#define samples 128

int PIN =1;
float freq=3.0;
float val,filtVal;
float lowestVal=1000.0;

unsigned int ct=0;
unsigned int period=10;
unsigned int nt;

int samplingFreq=1000;
unsigned int samplingPer,microseconds;
double vReal[samples];
double vImag[samples];

//FilterOnePole lpf(LOWPASS, freq);
FilterTwoPole lpf(LOWPASS, freq);
FilterDerivative fd;
arduinoFFT FFT=arduinoFFT();

void setup() {
 Serial.begin(9600);
 nt=ct+period;
 samplingPer=round(1000000*(1.0/samplingFreq));
}

void loop() {
  //while(1)
  //fft();
  val=analogRead(PIN);
  filtVal=transformation2(val);
  
 Serial.print(val);
 Serial.print(" ");
 Serial.println((filtVal<lowestVal)?lowestVal:filtVal);
 //Serial.println(filtVal);

 ct=millis()/1000;
}

float transformation1(float v){
  
  //if(v<lowestVal)
  //  lowestVal=v;
  if(ct>nt){
    lowestVal=v;
    nt=ct+period;
  }
  return fd.input(lpf.input(v))+500;
}

float transformation2(float v){
  if(ct>nt){
    lowestVal=v;
    nt=ct+period;
  }
  return lpf.input(fd.input(lpf.input(v)));
}

void fft(){
  for(int i=0;i<samples;i++){
    microseconds=micros();
    vReal[i]=analogRead(PIN);
    vImag[i]=0;

    while(micros()<(microseconds+samplingPer)){
      
    }

    FFT.Windowing(vReal,samples,FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(vReal,vImag,samples,FFT_FORWARD);
    FFT.ComplexToMagnitude(vReal,vImag,samples);
    double peak=FFT.MajorPeak(vReal, samples, samplingFreq);

    for(int i=0;i<(samples/2);i++){
      Serial.println(vReal[i],1);
    }
  }
  delay(1000000);
}
