/*
  Simple heart-rate and spo2 and temperature collector program;

*/
int heart_rate = 0;
int spo2_level = 0;
float temperature = 0;

int ir_data = 0;
int red_data = 0;

void send_data(void){
  /*
    Send data over the Serial;
  */

  Serial.print(heart_rate);
  Serial.print(",");
  Serial.print(spo2_level);
  Serial.print(",");
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(ir_data);
  Serial.print(",");
  Serial.print(red_data);
  Serial.println();
}

void setup(){
  Serial.begin(9600);
}

void loop(){

  heart_rate = random(100);
  spo2_level = random(150);
  temperature = random(50);
  ir_data = random(10000);
  red_data = random(10000);
  send_data();

}