// Motor Driver Pins
int motor1Pin1 = 3; // Left motor forward
int motor1Pin2 = 4; // Left motor backward
int motor2Pin1 = 5; // Right motor forward
int motor2Pin2 = 6; // Right motor backward

// IR Sensor Pins
int leftmostSensor = A0;  // Outer left sensor
int leftSensor = A1;      // Inner left sensor
int rightSensor = A2;     // Inner right sensor
int rightmostSensor = A3; // Outer right sensor

void setup() {
  // Initialize motor pins as output
  pinMode(motor1Pin1, OUTPUT);
  pinMode(motor1Pin2, OUTPUT);
  pinMode(motor2Pin1, OUTPUT);
  pinMode(motor2Pin2, OUTPUT);

  // Initialize sensor pins as input
  pinMode(leftmostSensor, INPUT);
  pinMode(leftSensor, INPUT);
  pinMode(rightSensor, INPUT);
  pinMode(rightmostSensor, INPUT);

  Serial.begin(9600);
}

void loop() {
  // Read sensor values
  int leftmostValue = digitalRead(leftmostSensor);
  int leftValue = digitalRead(leftSensor);
  int rightValue = digitalRead(rightSensor);
  int rightmostValue = digitalRead(rightmostSensor);

  // Debugging - Print sensor values
  Serial.print("Leftmost: ");
  Serial.print(leftmostValue);
  Serial.print(" | Left: ");
  Serial.print(leftValue);
  Serial.print(" | Right: ");
  Serial.print(rightValue);
  Serial.print(" | Rightmost: ");
  Serial.println(rightmostValue);

  // Robot behavior based on sensor values
  if (leftValue == 1 && rightValue == 1) {
    moveForward(); // Centered on the line
  } else if (leftValue == 0 && rightValue == 1) {
    turnLeft(); // Slight left correction
  } else if (leftValue == 1 && rightValue == 0) {
    turnRight(); // Slight right correction
  } else if (leftmostValue == 0) {
    sharpTurnLeft(); // Far off to the left
  } else if (rightmostValue == 0) {
    sharpTurnRight(); // Far off to the right
  } else {
    stopMotors(); // Lost the line
  }
}

void moveForward() {
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);
}

void turnLeft() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH); // Left motor reverse
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, LOW);  // Right motor forward
}

void turnRight() {
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);  // Left motor forward
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH); // Right motor reverse
}

void sharpTurnLeft() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, HIGH); // Left motor reverse
  digitalWrite(motor2Pin1, HIGH);
  digitalWrite(motor2Pin2, HIGH); // Right motor forward at high speed
}

void sharpTurnRight() {
  digitalWrite(motor1Pin1, HIGH);
  digitalWrite(motor1Pin2, LOW);  // Left motor forward at high speed
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, HIGH); // Right motor reverse
}

void stopMotors() {
  digitalWrite(motor1Pin1, LOW);
  digitalWrite(motor1Pin2, LOW);
  digitalWrite(motor2Pin1, LOW);
  digitalWrite(motor2Pin2, LOW);
}
