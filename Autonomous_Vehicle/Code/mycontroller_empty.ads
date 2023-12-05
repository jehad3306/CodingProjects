with Ultrasonic; use Ultrasonic;
with movementpro;
with Ada.Real_Time; use Ada.Real_Time;
with MicroBit.Console; use MicroBit.Console;
with Ultrasonic; use Ultrasonic;
with myMusic; use myMusic;
with MicroBit.Servos; use MicroBit.Servos;
with Ada.Execution_Time; use Ada.Execution_Time;
package mycontroller_empty is
   
   type Direction is (ahead, backward, leftSide, rightSide,rotRight,stop,forwardLeft,forwardRight,rotLeft);
   type availableAngle is (Angle);
   procedure directionControl(carDirection : Direction);
   task Sense with Priority => 2;
  
   task Think with Priority=> 3; -- what happens for the set direction if think and sense have the same prio and period?
   -- what happens if think has a higher priority? Why is think' set direction overwritten by sense' set direction?
   
   task Act with Priority=> 1;

   protected MotorController is
      function GetDirection return Direction;
      procedure SetDirection (carDirection : Direction);

      procedure SetRotationState (State : Boolean);
      function GetRotationState return Boolean;
   private
      DriveDirection : Direction;
      rotationState : Boolean;
   end MotorController;
   protected ServoController is 
      procedure SetServoAngle (servoAngle : Servo_Set_Point);
      function GetAngle return Servo_Set_Point;
      procedure SetDistanceWall(distanceW : Boolean);
      function GetDistanceWall return Boolean;
      
   private
      angleToRotate : Servo_Set_Point := 60;
      distanceWall : Boolean;
   end ServoController;
   protected UltrasonicController is
      procedure SetDistance (Distance : Distance_cm);
      function GetDistance return Distance_cm;
   private
      DistanceAhead : Distance_cm;
   end UltrasonicController;
   end mycontroller_empty;
