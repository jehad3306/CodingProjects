With MicroBit.IOsForTasking; use MicroBit.IOsForTasking;
with MicroBit.TimeHighspeed; use MicroBit.TimeHighspeed;
with MicroBit.IOsForTasking; use MicroBit.IOsForTasking;
with NRF_SVD.GPIO; use NRF_SVD.GPIO;
with MicroBit; use MicroBit;
with HAL; use HAL;

package Ultrasonic is

   type Distance_cm is range 0 .. 400; -- if < 2 it is invalid
   
   function Read return Distance_cm;
   
   procedure SendTriggerPulse;
   
   procedure Setup (trigger_pin : Pin_Id; echo_pin : Pin_Id);
   
   function WaitForEcho return Integer;
   
   function ConvertEchoToDistance (echo_time_us : Integer) return Distance_cm;
end Ultrasonic;
