import time
import serial

# Conexão serial com a placa de controle do SoBot
ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1, dsrdtr=False)
time.sleep(2)  # Aguarda inicialização


def enviar_comando(comando):
    """Envia o comando formatado em bytes para o SoBot via serial."""
    ser.write(comando.encode("ascii"))
    time.sleep(0.1)


def ler_sensores_linha():
    """Lê os 3 sensores de linha (SL1, SL2, SL3).

    Retorna uma tupla de inteiros (sl1, sl2, sl3).
    - 0: Superfície reflexiva (Branco)
    - 1: Linha preta detectada
    """
    ser.write(b"SL")
    time.sleep(0.05)
    resposta = ser.read_all().decode("ascii", errors="ignore")

    # Caso receba resposta válida (ex: "SL1 0 SL2 1 SL3 0")
    if "SL1" in resposta:
        partes = resposta.split()
        try:
            sl1 = int(partes[1])
            sl2 = int(partes[3])
            sl3 = int(partes[5])
            return sl1, sl2, sl3
        except (IndexError, ValueError):
            pass
    return 0, 0, 0


def seguir_linha_ate_marca():
    """Mantém o robô seguindo a linha no modo contínuo até encontrar

    uma marcação lateral (SL1=1 ou SL3=1).
    """
    # Habilita motores no modo contínuo
    enviar_comando("MT0 ME1")
    enviar_comando("MT0 MC AT100 DT100 V5")

    while True:
        sl1, sl2, sl3 = ler_sensores_linha()

        # Marca de parada detectada (sensor lateral sobre a fita)
        if sl1 == 1 or sl3 == 1:
            enviar_comando("MT0 MP")  # Pausa o movimento contínuo
            time.sleep(0.2)
            break

        # Controle simples de seguidor de linha
        if sl2 == 1:
            enviar_comando("MT0 MF")  # Segue em frente
        elif sl1 == 1:
            enviar_comando("MT0 ML")  # Ajusta para esquerda
        elif sl3 == 1:
            enviar_comando("MT0 MR")  # Ajusta para direita
        else:
            enviar_comando("MT0 MF")

        time.sleep(0.05)


# --- FLUXO DO DESAFIO (SOBOT FORK LIFT) ---

# 1. Habilita motores e garante garfo abaixado no início
enviar_comando("MT0 E1")
enviar_comando("EL DN")
enviar_comando("DL3000")  # Aguarda descida do elevador

# 2. Navegação até a estação de coleta (Collect Point)
seguir_linha_ate_marca()

# Coleta do Pallet: avança um pouco, sobe o elevador e recua
enviar_comando("MT0 D100 AT500 DT500 V5")
enviar_comando("DL2500")

enviar_comando("EL UP")  # Eleva o pallet
enviar_comando("DL4000")

# 3. Giro de 180 graus no próprio eixo
enviar_comando("MT0 D180 R AT500 DT500 V10")
enviar_comando("DL4000")

# 4. Navegação até o ponto de depósito (Deposit Point)
seguir_linha_ate_marca()

# Depósito do Pallet: abaixa o elevador e recua
enviar_comando("EL DN")  # Deposta o pallet
enviar_comando("DL4000")

enviar_comando("MT0 D-150 AT500 DT500 V5")  # Recua para desengatar
enviar_comando("DL3000")

# 5. Giro de 180 graus e retorno à base inicial
enviar_comando("MT0 D180 R AT500 DT500 V10")
enviar_comando("DL4000")

# Finalização
enviar_comando("EL ST")
enviar_comando("MT0 E0")
ser.close()
