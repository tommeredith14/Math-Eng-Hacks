//set up pin numbers with defines

#define JOY_X A0
#define JOY_Y A1
#define TILT_LEFT 3
#define TILT_RIGHT 4
#define SHOOT 5
#define PAUSE 6
#define HEALTH 7



void setup() {
  // put your setup code here, to run once:
  pinMode(JOY_X, INPUT);
  pinMode(JOY_Y, INPUT);
  pinMode(TILT_LEFT,INPUT);
  pinMode(TILT_RIGHT, INPUT);
  pinMode(SHOOT, INPUT);
  pinMode(PAUSE, INPUT);
  pinMode(HEALTH, OUTPUT);

  
}

void loop() {
  // put your main code here, to run repeatedly:



  delay(5);
}
