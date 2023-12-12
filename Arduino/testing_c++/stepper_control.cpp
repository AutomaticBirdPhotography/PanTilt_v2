#include "stepper_control.h"
#include <Arduino.h>

StepperControl::StepperControl()
  : currentPosition(0), currentSpeed(0), restSteps(0), stepPin(0), dirPin(0), MAX_SPEED(100), ABSOLUTE_MAX_SPEED(500), acceleration(10), speedIncrement(0), INTERVAL(60), currentUpdateTime(millis()), lastUpdateTime(millis()) {}

void StepperControl::init(int stepPin, int dirPin) {
  this->stepPin = stepPin;
  this->dirPin = dirPin;
  pinMode(stepPin, OUTPUT);
  pinMode(dirPin, OUTPUT);
  currentPosition = 0;
  speedIncrement = acceleration * (INTERVAL / 1000);
}

void StepperControl::setMaxSpeed(float maxSpeed) {
  MAX_SPEED = maxSpeed;
}

void StepperControl::setAcceleration(float acceleration) {
  this->acceleration = acceleration;
  speedIncrement = acceleration * (INTERVAL / 1000);
}

void StepperControl::speedUpdate(float targetSpeed) {
  currentUpdateTime = millis();
  if (currentUpdateTime - lastUpdateTime >= INTERVAL) {
    targetSpeed = constrain(targetSpeed, -MAX_SPEED, MAX_SPEED);

    if (currentSpeed < targetSpeed) {
      currentSpeed += speedIncrement;
      currentSpeed = min(currentSpeed, targetSpeed);

    } else if (currentSpeed > targetSpeed) {
      currentSpeed -= speedIncrement;
      currentSpeed = max(currentSpeed, targetSpeed);

    } else {
      currentSpeed = targetSpeed;
    }
    runSpeed(currentSpeed);
    lastUpdateTime = currentUpdateTime;
  }

}

void StepperControl::positionUpdate(float targetPosition) {
  currentUpdateTime = millis();
    if (calculateStoppingPosition(currentSpeed) < targetPosition) {
      
      if (abs(currentSpeed) < speedIncrement && abs(targetPosition - currentPosition) < speedIncrement*INTERVAL){
        currentSpeed = 0;
      } else currentSpeed += speedIncrement;

    } else if (calculateStoppingPosition(currentSpeed) > targetPosition) {
      
      if (abs(currentSpeed) < speedIncrement && abs(targetPosition - currentPosition) < speedIncrement*INTERVAL){
        currentSpeed = 0;
      } else currentSpeed -= speedIncrement;
    }

    runSpeed(currentSpeed);
    lastUpdateTime = currentUpdateTime;
  }

long StepperControl::distanceToGo() {
  return targetPosition - currentPosition;
}

float StepperControl::calculateStoppingPosition(float speed) {
  int direction;
  if (speed >= 0) direction = 1;
  else direction = -1;
  long stepsToStop = (long)((speed * speed) / (2.0 * acceleration));
  return currentPosition + stepsToStop * direction;
}


void StepperControl::runSpeed(float speed) {
  float stepsFloat = speed * (INTERVAL / 1000);

  restSteps += stepsFloat - (int)stepsFloat;

  int steps = (int)stepsFloat + (int)restSteps;
  step(steps);
  currentPosition += steps;

  restSteps -= (int)restSteps;

  Serial.print("steps: ");
  Serial.print(steps);
  Serial.print("\tspeed: ");
  Serial.print(speed);
  Serial.print("\tstop: ");
  Serial.print(calculateStoppingPosition(speed));
  Serial.print("\tposition: ");
  Serial.println(currentPosition);
}

void StepperControl::step(int steps) {
  int microsecondsDelay = (1000000 / abs(ABSOLUTE_MAX_SPEED)) / 2;
  if (steps > 0) {
    digitalWrite(dirPin, HIGH);
  } else {
    digitalWrite(dirPin, LOW);
  }

  int stepCount = abs(steps);

  for (int i = 0; i < stepCount; i++) {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(microsecondsDelay);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(microsecondsDelay);
  }
}


int StepperControl::getPosition() {
  return currentPosition;
}
