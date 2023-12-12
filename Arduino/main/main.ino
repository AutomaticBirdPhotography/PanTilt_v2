#include <Stepper.h>
#include <Servo.h>

const int motor1StepPin = 2;
const int motor1DirPin = 3;
const int motor2StepPin = 4;
const int motor2DirPin = 5;
const int servo1Pin = 6;
const int servo2Pin = 7;

const int stepsPerRevolution = 200;
const int servoMinAngle = 0;
const int servoMaxAngle = 180;

bool isStepperEnabled = false;

Stepper motor1(stepsPerRevolution, motor1StepPin, motor1DirPin);
Stepper motor2(stepsPerRevolution, motor2StepPin, motor2DirPin);
Servo servo1;
Servo servo2;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(15);
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  servo1.attach(servo1Pin);
  servo2.attach(servo2Pin);
}

void disableSteppers() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  isStepperEnabled = false;
}

void enableSteppers() {
  motor1.setSpeed(0);
  motor2.setSpeed(0);
  isStepperEnabled = true;
}

void controlSteppers(String input) {
  int speedMotor1 = input.substring(1, 4).toInt();
  int speedMotor2 = input.substring(4, 7).toInt();
  if (isStepperEnabled) {
    motor1.setSpeed(speedMotor1); // TODO: Lag en funksjon for step per sekund
    motor2.setSpeed(speedMotor2);
  }
}



void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    if (input[0] == 's') disableSteppers();
    else if (input[0] == 'e') enableSteppers();
    else if (input[0] == 'd') disableServos();
    else if (input[0] == 'a') alignServos();
    else if (input[0] == 'h') homeSteppers();
    else if (input[0] == 'c') controlSteppers(input);
    else if (input[0] == 'p') pointServos(input);
  }
}

