import time
import serial

# Configuração da comunicação serial USB com a placa do SoBot
ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1,  dsrdtr=False)
time.sleep(2)  # Tempo para estabilização da conexão serial


def enviar_comando(comando):
    """Envia a string de comando formatada para o SoBot."""
    ser.write(comando.encode("ascii"))
    time.sleep(0.5)


# --- CONFIGURAÇÃO E PARÂMETROS DO PERCURSO ---
AT = 500  # Tempo de aceleração (ms)
DT = 500  # Tempo de desaceleração (ms)
V = 10  # Velocidade cruzeiro (cm/s)

# Distâncias calculadas para a pista (em milímetros - ajuste conforme o tamanho real da sua mesa/pista)
DIST_ATE_COLETA = 300  # Avanço inicial do Start até o Ponto de Coleta
DIST_ENTRE_PONTOS = 800  # Avanço do Ponto de Coleta até o Ponto de Depósito

# --- EXECUÇÃO DO DESAFIO (SEM SENSOR DE LINHA) ---

# 1. Habilita os motores principais (MT0) e garante elevador totalmente abaixado
enviar_comando("MT0 E1")
enviar_comando("EL DN")
enviar_comando("DL3000")  # Aguarda 3 segundos para conclusão da descida do garfo

# 2. Avança do ponto inicial (Start) até o Ponto de Coleta (Collect Point)
enviar_comando(f"MT0 D{DIST_ATE_COLETA} AT500 DT500 V15")
enviar_comando("DL4500")

# 3. Coleta do Pallet: eleva o garfo do elevador
enviar_comando("EL UP")
enviar_comando("DL3500")  # Aguarda o elevador subir com a carga

# 4. Giro de 180° sobre o próprio eixo (com o pallet elevado)
enviar_comando(f"MT0 D180 R AT500 DT500 V15")
enviar_comando("DL3500")  # Aguarda a curva de 180° completar

# 5. Avança de ré/frente até a área de depósito (Deposit Point)
# Como o robô girou 180°, ele avança de frente em direção ao ponto de depósito
enviar_comando(f"MT0 D{DIST_ENTRE_PONTOS} AT500 DT500 V15")
enviar_comando("DL9500")

# 6. Depósito do Pallet: abaixa o elevador para deixar a carga no chão
enviar_comando("EL DN")
enviar_comando("DL3500")  # Aguarda a descida do elevador

# 7. Recua ligeiramente para desengatar o garfo do pallet
enviar_comando(f"MT0 D-150 AT500 DT500 V15")
enviar_comando("DL3000")

# 8. Giro de 180° para alinhar com o início e finalizar o ciclo
enviar_comando(f"MT0 D180 R AT500 DT500 V15")
enviar_comando("DL3500")

# Finalização: Interrompe acionamento do elevador e desabilita motores
enviar_comando("EL ST")
enviar_comando("MT0 E0")

ser.close()
