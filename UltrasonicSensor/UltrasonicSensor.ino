const int trigger = 11;
const int echo = 12;

int time;
double distance;

void setup() {
  Serial.begin(9600);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
}

void loop() {
  digitalWrite(trigger, LOW);
  delay(150);
  
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  time = pulseIn(echo, HIGH);

  //distance in micrometers
  distance = (time * .034) / 2;

  Serial.println(distance);
}
