//set up pin numbers with defines

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
  
}

void loop() {
  // put your main code here, to run repeatedly:


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
  Serial.print("Steer: ");
  Serial.print(steer);



  //////MOTION - JOYSTICK CONTROL: x and y motion in range [-100,100]

  int joystick_X = -map(analogRead(JOY_X), 0, 1020, -100, 100);
  int joystick_Y = -map(analogRead(JOY_Y), 0, 1020, -100, 100);
  Serial.print("    X: ");
  Serial.print(joystick_X);
  Serial.print("    Y: ");
  Serial.print(joystick_Y);  

  
  //////SHOOT: 1 - Fire, 0 - Nothing
  
  bool shootPressed = !(digitalRead(SHOOT));
  Serial.print("    Shoot: ");
  Serial.print(shootPressed);

  //////OTHER: 1 - Active, 0 - Nothing
  
  bool otherPressed = !(digitalRead(OTHER));
  Serial.print("    Other: ");
  Serial.print(otherPressed);

  //////Pause: 1 - Menu, 0 - Nothing

  bool pausePressed = !(digitalRead(PAUSE));
  Serial.print("    Pause: ");
  Serial.println(pausePressed);

  
  delay(5);
}
