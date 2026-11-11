import time
import serial

# Configuração da comunicação serial USB com a placa do SoBot
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1, dsrdtr=False)
time.sleep(2)  # Tempo para estabilização da conexão serial


def enviar_comando(comando):
    """Envia a string de comando formatada para o SoBot."""
    ser.write(comando.encode("ascii"))
    time.sleep(0.5)


# --- CONFIGURAÇÃO E PARÂMETROS DO PERCURSO ---
AT = 500  # Tempo de aceleração (ms)
DT = 500  # Tempo de desaceleração (ms)
V = 10    # Velocidade cruzeiro (cm/s)

# --- EXECUÇÃO DO DESAFIO (SEM SENSOR DE LINHA) ---

# 1. Habilita o sistema e GARANTE que o elevador comece totalmente abaixado
enviar_comando("MT0 E1")
enviar_comando("EL DN")   # Garante que desce no início
enviar_comando("DL4900")  # Espera o elevador descer totalmente
enviar_comando("EL ST")   # Para o motor do elevador

# 2. Avança do ponto inicial (Start) até o Ponto de Coleta
enviar_comando(f"MT0 D380 AT500 DT500 V15")
enviar_comando("DL2000")

# 3. Giro de 90° para alinhar com o pallet
enviar_comando(f"MT0 D90 L AT500 DT500 V15")
enviar_comando("DL2000")

# 4. Avança até o pallet
enviar_comando(f"MT0 D680 AT500 DT500 V15")
enviar_comando("DL2000")


# 6. Coleta do Pallet: eleva o garfo e PARA o elevador antes de mover o robô
enviar_comando("EL UP")
enviar_comando("DL4000")   # Tempo para o elevador subir completamente
enviar_comando("EL ST")   # <--- ESSENCIAL: Para o elevador para ele não subir junto com a ré!

# 7. Agora sim, avança de ré com o pallet já levantado e seguro
enviar_comando(f"MT0 D-730 AT500 DT500 V15")
enviar_comando("DL2000")

# 8. Gira 90°
enviar_comando(f"MT0 D90 R AT500 DT500 V15")
enviar_comando("DL2000")

# 9. Andar para frente
enviar_comando(f"MT0 D1250 AT500 DT500 V15")
enviar_comando("DL2000")

# 10. Giro de 90°
enviar_comando(f"MT0 D90 L AT500 DT500 V15")
enviar_comando("DL2000")

# 11. Avança até deixar o pallet
enviar_comando(f"MT0 D730 AT500 DT500 V15")
enviar_comando("DL2000")

# 12. Depósito do Pallet: abaixa o elevador e PARA ele antes de recuar
enviar_comando("EL DN")
enviar_comando("DL4000")   # Aguarda a descida completa
enviar_comando("EL ST")   # <--- ESSENCIAL: Para o elevador antes do robô desengatar

# 13. Recua ligeiramente para desengatar o garfo do pallet
enviar_comando(f"MT0 D-190 AT500 DT500 V15")
enviar_comando("DL2000")

# 14. Coleta do Pallet: eleva o garfo e PARA o elevador antes de mover o robô
enviar_comando("EL UP")
enviar_comando("DL4000")   # Tempo para o elevador subir completamente
enviar_comando("EL ST")   # <--- ESSENCIAL: Para o elevador para ele não subir junto com a ré!


# Finalização: Desabilita motores
enviar_comando("MT0 E0")

ser.close()
