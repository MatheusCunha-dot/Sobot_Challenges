import serial
from time import sleep

s = serial.Serial('/dev/ttyACM0', 9600, Ttimeout=0, dsrdtr=False)

def set_led(r, g, b):
    s.write(f"LT E1 RD{r} GR{g} BL{b}".encode())

def pause(seconds):
    sleep(seconds)

s.write(b"MT0 E1")


set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")


set_led(0, 0, 255)
s.write(b"MT0 D90 L AT500 DT500 V10")


set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")


set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")


set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")


set_led(255, 0, 0)
s.write(b"MT0 D-1000 AT500 DT500 V10")


set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")


set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")


set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")


set_led(0, 255, 0)
s.write(b"MT0 D1000 AT500 DT500 V10")


set_led(255, 255, 0)
s.write(b"MT0 D90 R AT500 DT500 V10")

s.write(b"MT0 E0")
s.write(b"LT E0")
pause(2)


s.write(b"MT0 ME1")
s.write(b"MT0 MC MD1 RI100 AT100 DT100 V10")


set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)


set_led(0, 0, 255)
s.write(b"MT0 ML")
pause(1.5)


set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)


set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)


set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)


set_led(255, 0, 0)
s.write(b"MT0 MB")
pause(3)


set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)


set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)


set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)


set_led(0, 255, 0)
s.write(b"MT0 MF")
pause(3)


set_led(255, 255, 0)
s.write(b"MT0 MR")
pause(1.5)

s.write(b"MT0 MP")
s.write(b"MT0 ME0")
s.write(b"LT E0")
pause(2)


def stop_motors():
    s.write(b"MT1 E0 MT2 E0")


set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)


set_led(0, 0, 255)
s.write(b"MT1 E1 PS-500 MT2 E1 PS500")
pause(1)


set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)


set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)


set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)


set_led(255, 0, 0)
s.write(b"MT1 E1 PS-500 MT2 E1 PS-500")
pause(3)


set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)


set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)


set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)


set_led(0, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS500")
pause(3)


set_led(255, 255, 0)
s.write(b"MT1 E1 PS500 MT2 E1 PS-500")
pause(1)

stop_motors()
s.write(b"LT E0")
