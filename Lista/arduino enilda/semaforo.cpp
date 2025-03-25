int ledverde = 6;
int ledamarelo = 9;
int ledvermelho = 10;

void setup() {               
  pinMode(ledverde, OUTPUT);
  pinMode(ledamarelo, OUTPUT);
  pinMode(ledvermelho, OUTPUT); 
  }

void loop() {

  digitalWrite(ledverde, HIGH);    
  delay(1000);                    
  digitalWrite(ledverde, LOW);   
  delay(1000);                     

  digitalWrite(ledamarelo, HIGH);  
  delay(1000);                     
  digitalWrite(ledamarelo, LOW);  
  delay(1000);                     

  digitalWrite(ledvermelho, HIGH);  
  delay(1000);                      
  digitalWrite(ledvermelho, LOW);   
  delay(1000);                     

  }