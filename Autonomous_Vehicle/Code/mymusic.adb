package body myMusic is
   procedure rock is 
      MarioMainThemeMelody : constant MicroBit.Music.Melody :=
        ((E7,83),(E7,83),(Rest,83),(E7, 83),
         (Rest,83),(C7,83),(E7,83),(Rest,83),
         (G7,83),(Rest,83),(Rest,83),(Rest,48),
         (G6,83),(Rest,83),(Rest,83),(Rest,83),
      
         (C7,83),(Rest,83),(Rest,83),(G6,83),
         (Rest,83),(Rest,83),(E6,83),(Rest,83),
         (Rest,83),(A6,83),(Rest,83),(B6,83),
         (Rest,83),(AS6,83),(A6,83),(Rest,83),
      
         (G6,83),(E7,111),(G7,111),
         (A7,111),(Rest,83),(F7,83),(G7,83),
         (Rest,83),(E7,83),(Rest,83),(C7,83),
         (D7,83),(B6,83),(Rest,83),(Rest,83),
      
         (C7,83),(Rest,83),(Rest,83),(G6,83),
         (Rest,83),(Rest,83),(E6,83),(Rest,83),
         (Rest,83),(A6,83),(Rest,83),(B6,83),
         (Rest,83),(AS6,83),(A6,83),(Rest,111),
      
         (G6,111),(E7,111),(G7,83),(Rest,83),
         (A7,111),(Rest,111),(F7,83),(G7,83),
         (Rest,83),(E7,111),(Rest,111),(C7,111),
         (D7,83),(B6,111),(Rest,111),(Rest,111));
   begin
      MicroBit.Music.Play(27, MarioMainThemeMelody);
   end rock;
   procedure silence is
   begin
      Set(27, False); --stop
   end silence;

end myMusic;
