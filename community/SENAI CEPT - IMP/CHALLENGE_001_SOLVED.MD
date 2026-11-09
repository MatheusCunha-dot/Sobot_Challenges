import serial
from time import sleep

s = serial.Serial('/dev/ttyUSB0', 9600)

def set_led(r, g, b):
    s.write(f"LT E1 RD{r} GR{g} BL{b}".encode())

def pause(seconds):
    sleep(seconds)

# LEVEL 1: BASIC (Fixed Commands Mode)
s.write(b"MT0 E1")

# 1. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")

# 2. Left | Blue
set_led(0, 0, 255)
s.write(b"MT0 D90 L AT500 DT500 V10")

# 3. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")

# 4. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")

# 5. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")

# 6. Backward | Red
set_led(255, 0, 0)
s.write(b"MT0 D-1000 AT500 DT500 V10")

# 7. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")

# 8. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")

# 9. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")

# 10. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")

# 11. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")

s.write(b"MT0 E0")
s.write(b"LT E0")
pause(2)

# LEVEL 2: INTERMEDIATE (Continuous Movement Mode)
s.write(b"MT0 ME1")
s.write(b"MT0 MC MD1 RI100 AT100 DT100 V10")

# 1. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)

# 2. Left | Blue
set_led(0, 0, 255)
s.write(b"MT0 ML")
pause(1.5)

# 3. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)

# 4. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)

# 5. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)

# 6. Backward | Red
set_led(255, 0, 0)
s.write(b"MT0 MB")
pause(3)

# 7. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)

# 8. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)

# 9. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)

# 10. Forward | Green
set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)

# 11. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)

s.write(b"MT0 MP")
s.write(b"MT0 ME0")
s.write(b"LT E0")
pause(2)

# LEVEL 3: ADVANCED (Pulses-Per-Second Mode)
def stop_motors():
    s.write(b"MT1 E0 MT2 E0")

# 1. Forward | Green
set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)

# 2. Left | Blue
set_led(0, 0, 255)
s.write(b"MT1 E1 PS-500 MT2 E1 PS500")
pause(1)

# 3. Forward | Green
set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)

# 4. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)

# 5. Forward | Green
set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)

# 6. Backward | Red
set_led(255, 0, 0)
s.write(b"MT1 E1 PS-500 MT2 E1 PS-500")
pause(3)

# 7. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)

# 8. Forward | Green
set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)

# 9. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)

# 10. Forward | Green
set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)

# 11. Right | Yellow
set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)

stop_motors()
s.write(b"LT E0")

```
