from time import sleep
import serial

# Configuração da porta serial
usb = serial.Serial('/dev/ttyACM0', 9600, timeout=0, dsrdtr=False)
usb.flush()

# Habilita os motores das rodas
usb.write(b"MT0 E1")
sleep(0.5)

print("Iniciando percurso...")

# -------------------------------------------------------------
# INICIO
# -------------------------------------------------------------

# 1. Para frente (Verde) - ANDAR MEIO METRO
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)  # Aguarda a conclusão física do movimento

# 2. Esquerda (Azul) - CURVA 90° 
usb.write(b"LT E1 RD0 GR0 BL255")
usb.write(b"MT0 E1 D90 L AT1000 DT1000 V15")
sleep(2.0)

# 3. Para frente (Verde) - ANDAR MEIO METRO
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)

# 4. Direita (Amarelo) - CURVA 90° 
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT1000 DT1000 V15")
sleep(2.0)

# 5. Para frente (Verde) - ANDAR MEIO METRO(ATÉ O LOCAL DE VOLTA)
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)

# -------------------------------------------------------------
# GIRO 180° E VOLTAR PERCURSO
# -------------------------------------------------------------

# Giro 180° na Barra Preta (Vermelho) - GIRO PRA O RETORNO AO LOCAL DE INICIO
usb.write(b"LT E1 RD255 GR0 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V15")
sleep(2.0)

# 6. Para frente (Verde) - ANDAR MEIO METRO
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)

# 7. Esquerda (Amarelo) - CURVA 90° 
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 L AT1000 DT1000 V15")
sleep(2.0)

# 8. Para frente (Verde) - ANDAR MEIO METRO
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)

# 9. Direita (Amarelo) - CURVA 90° 
usb.write(b"LT E1 RD255 GR255 BL0")
usb.write(b"MT0 E1 D90 R AT1000 DT1000 V15")
sleep(2.0)

# 10. Para frente (Verde) - ANDAR MEIO METRO
usb.write(b"LT E1 RD0 GR255 BL0")
usb.write(b"MT0 E1 D500 AT1000 DT1000 V15")
sleep(2.0)
 
# Giro 180° (Vermelho) - GIRO AO LOCAL DE INICIO
usb.write(b"LT E1 RD255 GR0 BL0")
usb.write(b"MT0 E1 D180 R AT1000 DT1000 V15")
sleep(2.0)

# Finalização: Desliga LEDs e motores
usb.write(b"LT E0")
usb.write(b"MT0 E0")
print("Percurso concluído!")
