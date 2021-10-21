// Declarar variables
int signal_r = A1;
double val = 0;
int signal_list[] = {0, 0, 0,0};
int signal_out = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(signal_r);
  //Serial.println(val);

  // Promedio movil 
  for (int i = 4; i > 0; i--) {
    if (i == 1) {
      signal_list[i] = val;
    } else {
      signal_list[i] = signal_list[i - 1];
    }
  }
  
//  signal_list[2] = signal_list[1];
//  signal_list[3] = signal_list[2];
//  signal_list[4] = signal_list[3]; 
//  signal_list[5] = signal_list[4];
//  signal_list[1] = val;

  signal_out = (signal_list[1] + signal_list[2] + signal_list[3]) / 5 ;
//  Serial.println(signal_list[1]);  
//  Serial.println(signal_list[2]); 
//  Serial.println(signal_list[3]);
  Serial.println(signal_out);
}
