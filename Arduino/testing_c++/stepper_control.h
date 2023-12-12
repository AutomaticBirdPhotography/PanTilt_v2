#ifndef STEPPER_CONTROL_H
#define STEPPER_CONTROL_H

#include <Arduino.h>

class StepperControl {
  private:
    int currentPosition;
    float currentSpeed;
    float restSteps;
    int stepPin;
    int dirPin;
    float MAX_SPEED;
    const int ABSOLUTE_MAX_SPEED;
    float acceleration;
    float speedIncrement;
    float INTERVAL;
    unsigned long currentUpdateTime;
    unsigned long lastUpdateTime;

  public:
    StepperControl();
    void init(int stepPin, int dirPin);
    void setMaxSpeed(float maxSpeed);
    void setAcceleration(float acceleration);
    void speedUpdate(float targetSpeed);
    void positionUpdate(int targetPosition);
    float calculateStoppingPosition(float speed);
    int stepsToStop(float speed);
    float calculateSpeedIncrease(float target);
    void runSpeed(float speed);
    void step(int steps);
    int getPosition();
};

#endif
