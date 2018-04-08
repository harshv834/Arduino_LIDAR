#include <Servo.h>
#include<NewPing.h>

#define trigPin 13
#define echoPin 12
#define servopin 9

Servo myservo;  // create servo object to control a servo
NewPing sonar(trigPin,echoPin,200);// a maximum of eight servo objects can be created
int pos = 0;    // variable to store the servo position
int count =0;
int flag=0;
//int  p=0, q=0;
void setup() {
  myservo.attach(servopin);  // attaches the servo on pin 9 to the servo object
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}
void loop() {
  long duration, distance[10],avg_dist=0;
  int k = 0,len=0; 
  if( flag==0){
    pos=pos+1;
  }
  else{
    pos = pos-1;
  }
  if(pos ==180){
    flag = 1;
    //p+=1;
  }
  if(pos ==0){
    flag = 0;
    //p+=1;
  }
  myservo.write(pos);
//Serial.print (p/2);
  
while (k<5){
   delay(50);
   distance[k] = sonar.ping_cm();// ---------> 29.1 ie?
  if((distance[k] != 0)&&(distance[k]<200)){
    avg_dist = avg_dist +distance[k];
    len = len +1  ;
  }
  k=k+1;
}
  k=0;
  if(len!=0){    
  Serial.print(avg_dist/len);
  Serial.print(',');
  Serial.println(pos);
  }
  else{
    Serial.println("No nonzero value");
    //q+=1;
    //Serial.print(',');
    //Serial.print(q);
  }
}
  
