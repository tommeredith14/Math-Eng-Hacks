//set up pin numbers with defines
//YAY GIT
const int led = 13;

//#define ARDUINODEGUB //if defined, values written to serial monitor (Tom's old code)
#define PYTHONMODE

#define JOY_X A0
#define JOY_Y A1
#define TILT_LEFT 6
#define TILT_RIGHT 8
#define SHOOT 3
#define PAUSE 4
#define HEALTH 7
#define OTHER 2

void setup() {
  // put your setup code here, to run once:
  pinMode(JOY_X, INPUT);
  pinMode(JOY_Y, INPUT);
  pinMode(TILT_LEFT,INPUT);
  pinMode(TILT_RIGHT, INPUT);
  pinMode(SHOOT, INPUT);
  pinMode(PAUSE, INPUT);
  pinMode(HEALTH, OUTPUT);
  pinMode(OTHER, INPUT);
  Serial.begin(9600);
  
  pinMode(led, OUTPUT); 
}

void loop() {
  // put your main code here, to run repeatedly:
  
  while (!Serial.available()) {}
  char incomingByte = Serial.read();


  //TURRET ROTATION: L - CCW, R - CW, S - No Rot, E - Error
  bool tiltedLeft = digitalRead(TILT_LEFT);
  bool tiltedRight = digitalRead(TILT_RIGHT);

  char steer;
  if (tiltedLeft && !tiltedRight)
    steer = 'L';
  else if(tiltedLeft && tiltedRight)
    steer = 'E';
  else if(!tiltedLeft && tiltedRight)
    steer = 'R';
  else
    steer = 'S';
    
  #ifdef ARDUINODEBUG
  Serial.print("Steer: ");
  Serial.print(steer);
  #endif


  //////MOTION - JOYSTICK CONTROL: x and y motion in range [-100,100]

  int joystick_X = -map(analogRead(JOY_X), 0, 1020, -100, 100);
  int joystick_Y = -map(analogRead(JOY_Y), 0, 1020, -100, 100);
  
  #ifdef ARDUINODEBUG
  Serial.print("    X: ");
  Serial.print(joystick_X);
  Serial.print("    Y: ");
  Serial.print(joystick_Y);  
  #endif
  
  //////SHOOT: 1 - Fire, 0 - Nothing
  
  bool shootPressed = !(digitalRead(SHOOT));
  #ifdef ADRDUINODEBUG
  Serial.print("    Shoot: ");
  Serial.print(shootPressed);
  #endif

  //////OTHER: 1 - Active, 0 - Nothing
  
  bool otherPressed = !(digitalRead(OTHER));
  #ifdef ADRDUINODEBUG
  Serial.print("    Other: ");
  Serial.print(otherPressed);
  #endif
  
  //////Pause: 1 - Menu, 0 - Nothing

  bool pausePressed = !(digitalRead(PAUSE));
  #ifdef ADRDUINODEBUG 
  Serial.print("    Pause: ");
  Serial.println(pausePressed);
  #endif

  //joystick_X
  //joystick_Y
  //steer
  //shootPressed
  //otherPressed
  //pausePressed
  //Geoff's Output
  
  #ifdef PYTHONMODE
  
  //just test values
  joystick_X = -30;
  joystick_Y = 200;
  steer = 'T';
  shootPressed = 0;
  otherPressed = 0;
  pausePressed = 0;
  
  /*
  digitalWrite(led, HIGH);
  delay(1100);
  digitalWrite(led, LOW);
  */
  Serial.print(joystick_X);
  Serial.print(' ');
  Serial.print(joystick_Y);
  Serial.print(' ');
  Serial.print(shootPressed);
  Serial.print(' ');
  Serial.print(steer);
  Serial.print(' ');
  Serial.print(otherPressed);
  Serial.print(' ');
  Serial.print(pausePressed);
  Serial.println(' ');
  
  #endif

  

}


/*
const int ledPin = 13;
void setup(){
  Serial.begin(9600);
}

void loop(){
  Serial.println(5);
}

void blink(int numberOfTimes){
  for (int i = 0; i < numberOfTimes; i++) 
  {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
   }
}const int ledPin = 13;
void setup(){
  Serial.begin(9600);
}

void loop(){
  Serial.println(5);
}

void blink(int numberOfTimes){
  for (int i = 0; i < numberOfTimes; i++) 
  {
    digitalWrite(ledPin, HIGH);
    delay(500);
    digitalWrite(ledPin, LOW);
    delay(500);
   }
}
*/

