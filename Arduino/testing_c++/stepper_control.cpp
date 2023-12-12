#include "stepper_control.h"
#include <Arduino.h>

StepperControl::StepperControl()
  : currentPosition(0), currentSpeed(0), restSteps(0), stepPin(0), dirPin(0), MAX_SPEED(100), ABSOLUTE_MAX_SPEED(500), acceleration(10), speedIncrement(0), INTERVAL(50), currentUpdateTime(millis()), lastUpdateTime(millis()) {}

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

void StepperControl::positionUpdate(int targetPosition) {
  currentUpdateTime = millis();
  if (currentUpdateTime - lastUpdateTime >= INTERVAL) {

    int distanceToGo = abs(targetPosition - currentPosition);

    if (currentPosition < targetPosition){ // has to run up to the target

      if (calculateStoppingPosition(currentSpeed+speedIncrement) < targetPosition) { // so if it can stop before the target with its new speed, it will accelerate
        
         currentSpeed += speedIncrement;        // else we increase the speed

      } else if (calculateStoppingPosition(currentSpeed) >= targetPosition) { // if it can stop at the target or will run past we need to decelerate
        
        currentSpeed -= speedIncrement;
      }
    }

    else if (currentPosition > targetPosition){ // has to run down to the target
      if (calculateStoppingPosition(currentSpeed-speedIncrement) > targetPosition){ // it can stop before target
        currentSpeed -= speedIncrement;                             // decrease the speed more
      } else if (calculateStoppingPosition(currentSpeed) <= targetPosition){ // it will stop at the position, or run past!
        currentSpeed += speedIncrement;                                     // increase the speed, the speed is negative so increase to make it closer to 0
      }
      
    }

    if (stepsToStop(currentSpeed) <= 1 && distanceToGo == 0){   // if it is at the target, and has a so low speed that it can stop at 1 step or less
        currentSpeed = 0;
      }

    runSpeed(currentSpeed);
    lastUpdateTime = currentUpdateTime;
  }
}

int StepperControl::stepsToStop(float speed){
  int stopSteps = round((speed * speed) / (2.0 * acceleration));
  return stopSteps;
}

float StepperControl::calculateStoppingPosition(float speed) {
  int direction;
  if (speed >= 0) direction = 1;
  else direction = -1;
  return currentPosition + stepsToStop(speed) * direction;
}


void StepperControl::runSpeed(float speed) {
  float stepsFloat = speed * (INTERVAL / 1000);

  restSteps += stepsFloat - (int)stepsFloat;

  int steps = (int)stepsFloat + (int)restSteps;
  step(steps);
  currentPosition += steps;

  restSteps -= (int)restSteps;

  Serial.print("\tsteps: ");
  Serial.print(steps);
  Serial.print("\tspeed: ");
  Serial.print(speed);
  Serial.print("\tstopPos: ");
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
