An arduino controls power to the speakers and LED strip. The user [has to be part of the `uucp` group](https://wiki.archlinux.org/index.php/Arduino)


```bash
# gpasswd -a user uucp
```

A quick/dirty arduino script for controlling light/speaker GPIOs over serial:

```c
int SPK = 12;
int R = 10;
int G = 9;
int B = 11;

int COLOURTASK = 'c';
int SPEAKERTASK = 's';

int currentColour[3] = {0, 0, 0};
int targetColour[3] = {0, 0, 0};

int speakerState = LOW;
int targetSpeakerState = HIGH;


void setup() {
  pinMode(SPK, OUTPUT);
  pinMode(R, OUTPUT);
  pinMode(G, OUTPUT);
  pinMode(B, OUTPUT);
  
  digitalWrite(SPK, LOW);
  analogWrite(R, 0);
  analogWrite(G, 0);
  analogWrite(B, 0);
  
  Serial.begin(9600);
}

void updateColour () {
  currentColour[0] = targetColour[0];
  currentColour[1] = targetColour[1];
  currentColour[2] = targetColour[2];
  analogWrite(R, currentColour[0]);
  analogWrite(G, currentColour[1]);
  analogWrite(B, currentColour[2]);
}

void updateSpeaker() {
  speakerState = targetSpeakerState;
  digitalWrite(SPK, speakerState);
}

void loop() {
  if (Serial.available()) {
    byte task;
    task = Serial.read();
    Serial.write(task);
    Serial.println();

    if (task == SPEAKERTASK) {
      Serial.println("setting speaker...");
      targetSpeakerState = Serial.parseInt() != 0;
      Serial.read(); // garbage byte
      Serial.print("set speaker to ");
      Serial.println(targetSpeakerState, DEC);
      
    } else if (task == COLOURTASK) {
      Serial.println("setting colour...");
      
      Serial.print("r:");
      targetColour[0] = Serial.parseInt();
      Serial.read(); // garbage byte
      Serial.println(targetColour[0], HEX);
      
      Serial.print("g:");
      targetColour[1] = Serial.parseInt();
      Serial.read(); // garbage byte
      Serial.println(targetColour[1], HEX);

      Serial.print("b:");
      targetColour[2] = Serial.parseInt();
      Serial.read(); // garbage byte
      Serial.println(targetColour[2], HEX);
      
    } else {
      Serial.println("uh...");
      // err!
      targetColour[0] = 255;
      targetColour[1] = 0;
      targetColour[2] = 0;
    }
  }
  if (currentColour[0] != targetColour[0] ||
      currentColour[1] != targetColour[1] ||
      currentColour[2] != targetColour[2]) {
    Serial.println("updating colour...");
    updateColour();
  }
  if (speakerState != targetSpeakerState) {
    updateSpeaker();
    Serial.println("updating speaker state...");
  }
}
```

The `PySerial` library is used to talk to the arduino

```bash
# pacman -Syu python2-pip
# pip install pyserial
```

The arduino is likely at `/dev/ttyUSB0` (see arch wiki on Arduino linked at the beginning)

```python
import serial
s = serial.Serial(port='/dev/ttyUSB0', baudrate=9600)
# turn on the speakers
s.write('s1.')
# turn them off...
s.write('s0.')
# turn on the lights...
s.write('c255,255,255.')
```

see the xbmc plugin for doing this in response to playback events in xbmc.
