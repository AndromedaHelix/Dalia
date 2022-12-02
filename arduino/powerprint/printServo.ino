#include <Servo.h>

int servoPin = 10;

Servo powerServo;

void setup() {
  powerServo.attach(servoPin);
  powerServo.write(0);
}

void loop() {
  if(true){
    setServo(180);
  }
}

void setServo(int angle){
  powerServo.write(angle);
}
