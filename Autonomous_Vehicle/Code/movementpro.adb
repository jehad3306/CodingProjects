package body movementpro is

   procedure front is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end front;
   
   procedure back is
      Forward : constant Boolean := False; -- forward is true, backward is false
   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end back;
   procedure left is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, not Forward); --IN1
      MicroBit.IOsForTasking.Set(7, Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, not Forward); --IN3
      MicroBit.IOsForTasking.Set(15, Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end left;
   procedure right is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, not Forward); --IN3
      MicroBit.IOsForTasking.Set(3, Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, not Forward); --IN1
      MicroBit.IOsForTasking.Set(13, Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end right;
   procedure rotRight is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, not Forward); --IN1
      MicroBit.IOsForTasking.Set(13, Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, not Forward); --IN3
      MicroBit.IOsForTasking.Set(15, Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end rotRight;
   procedure stop is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, not Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, not Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, not Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, not Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (0, Speed); --right speed control ENA ENB
   end stop;
   procedure forwardLeft is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, not Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, not Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end forwardLeft;
   procedure forwardRight is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, Forward); --IN1
      MicroBit.IOsForTasking.Set(7, not Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, not Forward); --IN3
      MicroBit.IOsForTasking.Set(3, not Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, not Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end forwardRight;
   procedure rotLeft is

   begin
      --  We set the frequency by setting the period (remember f=1/t).
      MicroBit.IOsForTasking.Set_Analog_Period_Us(20000); -- 50 Hz = 1/50 = 0.02s = 20 ms = 20000us 
   
      --LEFT
      --front   
      MicroBit.IOsForTasking.Set(6, not Forward); --IN1
      MicroBit.IOsForTasking.Set(7, Forward); --IN2
   
      --back
      MicroBit.IOsForTasking.Set(2, not Forward); --IN3
      MicroBit.IOsForTasking.Set(3, Forward); --IN4
   
      --RIGHT
      --front
      MicroBit.IOsForTasking.Set(12, Forward); --IN1
      MicroBit.IOsForTasking.Set(13, not Forward); --IN2

      --back
      MicroBit.IOsForTasking.Set(14, Forward); --IN3
      MicroBit.IOsForTasking.Set(15, not Forward); --IN4
   
      MicroBit.IOsForTasking.Write (0, Speed); --left speed control ENA ENB
      MicroBit.IOsForTasking.Write (1, Speed); --right speed control ENA ENB
   end rotLeft;
end movementpro;
