with Ada.Real_Time; use Ada.Real_Time;
with MicroBit.IOsForTasking; use MicroBit.IOsForTasking;
with Ultrasonic; use Ultrasonic;
with MicroBit.Console; use MicroBit.Console;
with MicroBit.Music; use MicroBit.Music;
package movementpro is
   Speed : constant MicroBit.IOsForTasking.Analog_Value := 1023; --between 0 and 1023
   Forward : constant Boolean := True; -- forward is true, backward is false
   procedure front;
   procedure back;
   procedure right;
   procedure left;
   procedure rotRight;
   procedure stop;
   procedure forwardRight;
   procedure forwardLeft;
   procedure rotLeft;
end movementpro;
