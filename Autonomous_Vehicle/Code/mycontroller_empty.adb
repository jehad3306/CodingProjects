with Ada.Real_Time; use Ada.Real_Time;
with MicroBit.Console; use MicroBit.Console;
with servoControl;


package body mycontroller_empty is
   procedure directionControl(carDirection : Direction) is
   begin
      case carDirection is
      when ahead => movementPro.front;
         Put_Line("forward");
      when backward => movementPro.back;
         Put_Line("backward");
      when leftSide => movementPro.left;
         Put_Line("left");
      when rightSide => movementPro.right;
         Put_Line("right");
      when rotRight => movementpro.rotRight;
         Put_Line("RotatingRight");
      when stop => movementpro.Stop;
         Put_Line("Stop");
      when forwardLeft => movementpro.forwardLeft;
         Put_Line("ForwardLeft");
      when forwardRight => movementpro.forwardRight;
         Put_Line("ForwardRight");
      when rotLeft => movementpro.rotLeft;
      end case;
   end directionControl;

   task body sense is

      myClock : Time;
      
   begin
      Ultrasonic.Setup(10,11);      
      loop
         myClock := Clock;
         UltrasonicController.SetDistance(Read);
         Put_Line ("Read" & Distance_cm'Image(UltrasonicController.GetDistance));

           
         delay until myClock + Milliseconds(100);
      end loop;
   end sense;

   task body think is
      myClock : Time;
      isRightChecked : Boolean :=False;
      isLeftChecked : Boolean := False;
      isMiddelChecked : Boolean :=False;
      servoAngle : Servo_Set_Point := 60;
   begin
      loop
         myClock := Clock;
         ServoController.SetServoAngle(30);
         delay until myClock + Milliseconds(100);
         ServoController.SetServoAngle(100);
         delay until myClock + Milliseconds(200);
         
         if UltrasonicController.GetDistance < 30 then
            ServoController.SetDistanceWall(True);
         elsif UltrasonicController.GetDistance > 30 then
            ServoController.SetDistanceWall(False);
         end if;
         
         delay until myClock + Milliseconds(300);
         
      end loop;
   end think;
   
   task body act is
      myClock : Time;
      drive : Boolean := False;
   begin
      loop
         myClock := Clock;
         if ServoController.GetDistanceWall = True then
            directionControl(rotRight);
            Put_Line("rotate");
         elsif ServoController.GetDistanceWall = False then
            directionControl(ahead);
            Put_Line("Forward");
         end if;
         delay until myClock + Milliseconds(300);
         --movementpro.stop;
           
      end loop;
   end act;
   
   protected body MotorController is
      --  procedures can modify the data
      procedure SetDirection (carDirection : Direction) is
      begin
         DriveDirection := carDirection;
         --movementpro.(carDirection);
      end SetDirection;
      procedure SetRotationState (State : Boolean) is
      begin
         rotationState:= State;
      end SetRotationState;
      --  functions cannot modify the data
      function GetDirection return Direction is
      begin
         return DriveDirection;
      end GetDirection;
      function GetRotationState return Boolean is
      begin
         return rotationState;
      end GetRotationState;
   end MotorController;
   protected body ServoController is
      procedure SetDistanceWall (distanceW : Boolean) is
      begin
         distanceWall := distanceW;
         
      end SetDistanceWall;
      function GetDistanceWall return Boolean is
      begin
         return distanceWall;
      end GetDistanceWall;
         
      procedure SetServoAngle (servoAngle : Servo_Set_Point) is
      begin
         servoControl.servoDegree(servoAngle);
         angleToRotate := servoAngle;
      end SetServoAngle;
      function GetAngle return Servo_Set_Point is
      begin
         return angleToRotate;
      end GetAngle;
   end ServoController;
   protected body UltrasonicController is
      procedure SetDistance (Distance : Distance_cm) is
      begin
         DistanceAhead := Distance;
      end SetDistance;
      function GetDistance return Distance_cm is
      begin
         return DistanceAhead;
      end GetDistance;
   end UltrasonicController;
end mycontroller_empty;
