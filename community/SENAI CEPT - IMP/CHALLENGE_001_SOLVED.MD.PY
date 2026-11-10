import time
import serial

# Configuração da porta serial USB (ajuste '/dev/ttyACM0' ou 'COM3' conforme a porta do seu sistema)
# O SoBot utiliza padrão de transmissão serial via USB.
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
time.sleep(2)  # Aguarda a inicialização da conexão serial


def enviar_comando(comando):
    """Envia o comando formatado em bytes para o SoBot via serial."""
    ser.write(comando.encode("ascii"))
    time.sleep(0.1)


def definir_cor_led(red, green, blue):
    """Configura a cor da fita de LED RGB do SoBot.

    Cores (0 a 255):
    - Green (Verde): red=0, green=255, blue=0
    - Blue (Azul): red=0, green=0, blue=255
    - Yellow (Amarelo): red=255, green=255, blue=0
    - Red (Vermelho): red=255, green=0, blue=0
    """
    cmd = f"LT E1 RD{red} GR{green} BL{blue}"
    enviar_comando(cmd)


# --- INÍCIO DA EXECUÇÃO DO DESAFIO ---

# Habilita os motores principais (MOTOR 01 e MOTOR 02 simultâneos)
enviar_comando("MT0 E1")

# Definição dos parâmetros padrão de movimento (distância/ângulo, rampa e velocidade)
# Distância padrão: 500mm (50cm) | Aceleração: 1000ms | Desaceleração: 1000ms | Velocidade: 10cm/s
AT = 1000
DT = 1000
V = 10
DIST_MOV = 500  # Distância retilínea em mm
ANG_CURVA = 90  # Ângulo de curva no próprio eixo em graus

# 1. Forward - Green
definir_cor_led(0, 255, 0)
enviar_comando(f"MT0 D500 AT500 DT500 V10")
enviar_comando("DL2000")  # Aguarda execução do movimento

# 2. Left - Blue
definir_cor_led(0, 0, 255)
enviar_comando(f"MT0 D90 L AT500 DT500 V10")
enviar_comando("DL2000")

# 3. Forward - Green
definir_cor_led(0, 255, 0)
enviar_comando(f"MT0 D500 AT500 DT500 V10")
enviar_comando("DL2000")

# 4. Right - Yellow
definir_cor_led(255, 255, 0)
enviar_comando(f"MT0 D90 R AT500 DT500 V10")
enviar_comando("DL2000")

# 5. Forward - Green
definir_cor_led(0, 255, 0)
enviar_comando(f"MT0 D500 AT500 DT500 V10")
enviar_comando("DL2000")

# 6. Backward - Red (Movimento em ré utiliza sinal negativo na distância)
definir_cor_led(255, 0, 0)
enviar_comando(f"MT0 D-1000 AT500 DT500 V10")
enviar_comando("DL2000")

# 7. Right - Yellow
definir_cor_led(255, 255, 0)
enviar_comando(f"MT0 D90 R AT500 DT500 V10")
enviar_comando("DL2000")

# 8. Forward - Green
definir_cor_led(0, 255, 0)
enviar_comando(f"MT0 D500 AT500 DT500 V10")
enviar_comando("DL2000")

# 9. Right - Yellow
definir_cor_led(255, 255, 0)
enviar_comando(f"MT0 D90 R AT500 DT500 V10")
enviar_comando("DL2000")

# 10. Forward - Green
definir_cor_led(0, 255, 0)
enviar_comando(f"MT0 D500 AT500 DT500 V10")
enviar_comando("DL2000")

# 11. Right - Yellow
definir_cor_led(255, 255, 0)
enviar_comando(f"MT0 D90 R AT500 DT500 V10")
enviar_comando("DL2000")

# Finalização: Desliga fita LED e desabilita os motores
enviar_comando("LT E0")
enviar_comando("MT0 E0")

ser.close()
