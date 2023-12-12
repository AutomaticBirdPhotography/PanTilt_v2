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
    int MAX_UP;
    int MAX_DOWN;
    const int ABSOLUTE_MAX_SPEED = 500;
    float acceleration;
    float speedIncrement;
    float INTERVAL;
    unsigned long currentUpdateTime;
    unsigned long lastUpdateTime;

  public:
    StepperControl(int stepPin, int dirPin);
    void setMaxSpeed(float maxSpeed);
    void setAcceleration(float acceleration);
    void speedUpdate(float targetSpeed);
    void positionUpdate(int targetPosition);
    float calculateStoppingPosition(float speed);
    int stepsToStop(float speed);
    float calculateSpeedIncrease(float target);
    void runSpeed(float speed);
    void run(float targetSpeed, int targetPosition);
    void step(int steps);
    int getPosition();
    void setMaxUp(int maxUp);
    void setMaxDown(int maxDown);
};

#endif
