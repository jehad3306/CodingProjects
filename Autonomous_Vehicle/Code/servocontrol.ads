with MicroBit.IOsForTasking; use MicroBit.IOsForTasking;
with MicroBit.Servos;  use MicroBit.Servos;
with MicroBit.Buttons; use MicroBit.Buttons;
package servoControl is

   procedure turnStart;
   procedure turn0;
   procedure turn180;
   procedure servoDegree (angleToRotate : Servo_Set_Point);

end servoControl;
