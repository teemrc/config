int num;
int st;
int nums[11] = {0b11111100,0b00110000,0b11011010,0b01111010,0b00110110,0b01101110,0b11101110,0b00111000,0b11111110,0b01111110, 0};
void setup() {

  for (int i=2;i<6;i++){
    pinMode(i, INPUT);
  }

  for (int i=8;i<11;i++){
    pinMode(i, OUTPUT);
  }

}

void loop() {

    num = 0;
    for (int i = 5;i!=1;i--){
      st = 1;
      for (int n = i-2;n!=0;n--){
        st *= 2;
      }
      num += digitalRead(i)*st;
    }

    if (num > 9) {
      num = 10;
    }
    
    digitalWrite(10, LOW);
    shiftOut(8,9,LSBFIRST,nums[num]);
    digitalWrite(10, HIGH);
}
