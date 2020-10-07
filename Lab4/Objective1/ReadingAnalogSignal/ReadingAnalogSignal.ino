int iR;

void setup() {
 Serial.begin(9600);

}

void loop() {
  iR=analogRead(A1);
  Serial.println(iR);
  Serial.print('\n');
  
}
