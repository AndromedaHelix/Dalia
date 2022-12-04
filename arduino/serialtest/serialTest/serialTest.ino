
#define ledBlue 12
#define ledRed 11

int incomingByte = 0;  // for incoming serial data
char buf[100];

void setup() {
  Serial.begin(9600);

  while (!Serial) {
    // wait for serial port to connect. Needed for native USB
  }

  pinMode(ledBlue, OUTPUT);
  pinMode(ledRed, OUTPUT);
}

void loop() {
  // send data only when you receive data:

  if (Serial.available() > 0) {
    // read the incoming bytes:
    int rlen = Serial.readBytesUntil('\n', buf, 100);

    // prints the received data
    Serial.print("I received: ");
    for (int i = 0; i < rlen; i++)
      Serial.print(buf[i]);
  }
}
