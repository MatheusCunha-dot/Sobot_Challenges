import serial
from time import sleep

# Conexão serial com a placa de controle do SoBot
# Ajuste '/dev/ttyUSB0' conforme a porta do seu sistema
s = serial.Serial('/dev/ttyUSB0', 9600)

def definir_led(r, g, b):
    """Função para configurar a cor da fita de LED RGB do SoBot"""
    s.write(f"LT E1 RD{r} GR{g} BL{b}".encode()) #[cite: 39]

def pausar(segundos):
    """Aguardar a execução do comando antes de enviar o próximo"""
    sleep(segundos)


==============================================================================
(Comandos Fixos e Curva no Próprio Eixo)
==============================================================================
print("Iniciando Nível Básico: Comandos Fixos...")

# Habilita os motores das rodas
s.write(b"MT0 E1") #[cite: 9, 15]

# 1. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 D1000 AT500 DT500 V10") #[cite: 9, 13, 14, 15]

# 2. Esquerda (sobre o próprio eixo) | Azul
definir_led(0, 0, 255) #[cite: 39]
s.write(b"MT0 D90 L AT500 DT500 V10") #[cite: 13, 14, 15]

# 3. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 D1000 AT500 DT500 V10") #[cite: 9, 13, 14, 15]

# 4. Direita (sobre o próprio eixo) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 D90 R AT500 DT500 V10") #[cite: 14, 15]

# 5. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 D1000 AT500 DT500 V10") #[cite: 9, 13, 14, 15]

# 6. Para Trás (Ré) | Vermelho
definir_led(255, 0, 0) #[cite: 39]
s.write(b"MT0 D-1000 AT500 DT500 V10") #[cite: 13, 14, 15]

# 7. Direita (sobre o próprio eixo) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 D90 R AT500 DT500 V10") #[cite: 14, 15]

# 8. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 D1000 AT500 DT500 V10") #[cite: 9, 13, 14, 15]

# 9. Direita (sobre o próprio eixo) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 D90 R AT500 DT500 V10") #[cite: 14, 15]

# 10. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 D1000 AT500 DT500 V10") #[cite: 9, 13, 14, 15]

# 11. Direita (sobre o próprio eixo) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 D90 R AT500 DT500 V10") #[cite: 14, 15]

# Desabilita motores e apaga o LED ao encerrar a etapa
s.write(b"MT0 E0") #[cite: 9, 15]
s.write(b"LT E0") #[cite: 39]
pausar(2)


==============================================================================
(Movimento Contínuo e Curvas Diferenciais)
==============================================================================
print("Iniciando Nível Intermediário: Modo Contínuo e Curva Diferencial...")

# Habilita movimentação contínua com curva diferencial habilitada
s.write(b"MT0 ME1") #[cite: 17, 18]
s.write(b"MT0 MC MD1 RI100 AT100 DT100 V10") #[cite: 17, 18, 19]

# 1. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 MF") #[cite: 17, 19]
pausar(3)

# 2. Esquerda (Diferencial) | Azul
definir_led(0, 0, 255) #[cite: 39]
s.write(b"MT0 ML") #[cite: 17, 19]
pausar(1.5)

# 3. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 MF") #[cite: 17, 19]
pausar(3)

# 4. Direita (Diferencial) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 MR") #[cite: 17, 19]
pausar(1.5)

# 5. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 MF") #[cite: 17, 19]
pausar(3)

# 6. Para Trás (Ré) | Vermelho
definir_led(255, 0, 0) #[cite: 39]
s.write(b"MT0 MB") #[cite: 17, 19]
pausar(3)

# 7. Direita (Diferencial) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 MR") #[cite: 17, 19]
pausar(1.5)

# 8. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 MF") #[cite: 17, 19]
pausar(3)

# 9. Direita (Diferencial) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 MR") #[cite: 17, 19]
pausar(1.5)

# 10. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT0 MF") #[cite: 17, 19]
pausar(3)

# 11. Direita (Diferencial) | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT0 MR") #[cite: 17, 19]
pausar(1.5)

# Pausa a movimentação e desabilita motores
s.write(b"MT0 MP") #[cite: 17, 19]
s.write(b"MT0 ME0") #[cite: 17, 18]
s.write(b"LT E0") #[cite: 39]
pausar(2)


==============================================================================
(Controle dos Motores por Pulsos por Segundo)
==============================================================================
print("Iniciando Nível Avançado: Controle por Pulsos...")

def desligar_motores():
    s.write(b"MT1 E0 MT2 E0") #[cite: 29, 30]

# 1. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS500") #[cite: 29]
pausar(3)

# 2. Esquerda | Azul
definir_led(0, 0, 255) #[cite: 39]
s.write(b"MT1 E1 PS-500 MT2 E1 PS500") #[cite: 30]
pausar(1)

# 3. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS500") #[cite: 29]
pausar(3)

# 4. Direita | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS-500") #[cite: 30]
pausar(1)

# 5. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS500") #[cite: 29]
pausar(3)

# 6. Para Trás (Ré) | Vermelho
definir_led(255, 0, 0) #[cite: 39]
s.write(b"MT1 E1 PS-500 MT2 E1 PS-500") #[cite: 29]
pausar(3)

# 7. Direita | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS-500") #[cite: 30]
pausar(1)

# 8. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS500") #[cite: 29]
pausar(3)

# 9. Direita | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS-500") #[cite: 30]
pausar(1)

# 10. Frente | Verde
definir_led(0, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS500") #[cite: 29]
pausar(3)

# 11. Direita | Amarelo
definir_led(255, 255, 0) #[cite: 39]
s.write(b"MT1 E1 PS500 MT2 E1 PS-500") #[cite: 30]
pausar(1)

# Finalização Geral
desligar_motores()
s.write(b"LT E0") #[cite: 39]
print("Desafio concluído com sucesso!")

```
