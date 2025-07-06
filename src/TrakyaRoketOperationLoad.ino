#include "Arduino.h"
#include <Adafruit_BNO055.h>
#include <Adafruit_BME280.h>
#include <LoRa_E32.h>
#include <TinyGPS++.h>
#include <SD.h>
#include <SPI.h>
#include <SimpleKalmanFilter.h>
#include <stdlib.h>

#define STAGE1_PIN   1
#define STAGE2_PIN   0

#define GPS_BAUD    9600
#define LORA_BAUD   9600
#define SERIAL_BAUD 9600


bool stage1 = false ;
bool stage2 = false ;
int max_altitude ;
int altitude ;
int pitch ;
int yaw ;
int roll ;
int rocketState = 1 ;
int stage1_altitude ;
int stage2_altitude ;




/* Gereklilikler */
/* 
Veri yapılarını ayarla 
Paketleri ayarla
Sensör okuma prosedürlerini tamamla
Ana algoritmayı eksiksizleştir
Loglama işini hallet
Yorum Satırlarını unutma(okunabilirlik)
*/

struct packet_signal {
  
  byte pitch[4];
  byte roll[4];
  byte yaw[4];
  byte altitude[4];
  byte stage1[1];
  byte stage2[1];


} data;




SimpleKalmanFilter rollKalmanFilter(0.5, 0.5, 0.01);
SimpleKalmanFilter yawKalmanFilter(0.5, 0.5, 0.01);
SimpleKalmanFilter pitchKalmanFilter(0.5, 0.5, 0.01);






void setup() {


/* Serial communication confirmation */
Serial.begin(SERIAL_BAUD);
	while (!Serial) {
	   printf() ; // wait for serial port to connect. Needed for native USB
    }
	delay(100);



}

void loop() {
  
  
  
  /* Max altitude mechanism */
  if (max_altitude < altitude){
    max_altitude = altitude;
  }
                


  /* Main Operation Algorithm */
  if (rocketState == 1){
    if ((max_altitude - altitude > 15) && (pitch < 85)){
        stage1_sep();
    }
    else{
      digitalWrite(STAGE1_PIN, LOW);
    }
  if(rocketState == 2){
    if(altitude < 600){
      stage2_sep();
    }
    else{
      digitalWrite(STAGE2_PIN, LOW);
    }

  } 
  
  
  
  
};
  
  
  
  
  /* About Rockets Instant Status */
  if(stage1 && !stage2)
    rocketState = 2;
  else if(!stage1 && stage2)
    rocketState = 3;
  else if(stage1 && stage2)
    rocketState = 4;
  
}


/* Seperating Algorithms */
void stage1_sep(){

  digitalWrite(STAGE1_PIN,HIGH);
  delay(500);
  Serial.println("Stage 1 Separation Completed");
  stage1_altitude = altitude ;
  Serial.println("Stage 2 completed at " + String(stage2_altitude) + " meters");
  digitalWrite(STAGE2_PIN, LOW);
  stage1 = true; 



}
void stage2_sep(){
  
  digitalWrite(STAGE2_PIN,HIGH);
  delay(500);
  Serial.println("Stage 2 Separation Completed");
  stage2_altitude = altitude;
  Serial.println("Stage 2 completed at " + String(stage2_altitude) + " meters");
  digitalWrite(STAGE2_PIN, LOW);  
  stage2 = true;

}


