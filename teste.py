import RPi.GPIO as GPIO
import time 
import random

led_verm = 17 # pino físico 11
led_verd = 18 # pino físico 12
led_azul = 27 # pino físico 13
led_amar = 22 # pino físico 15

btn_verm = 23 # pino Físico 16
btn_verd = 24 # pino Físico 18
btn_azul = 25 # pino Físico 22
btn_amar = 5 # pino Físico 29

# Basicamente vai configurar os leds como receptores de sinal e os botões como "o sinal". ( botão como low e pisca como High eu acho kkkkkkkkkk )
def configuração_gpio():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led_verm, GPIO.OUT)
    GPIO.setup(led_verd, GPIO.OUT)
    GPIO.setup(led_azul, GPIO.OUT)
    GPIO.setup(led_amar, GPIO.OUT)

    GPIO.setup(btn_verm, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn_verd, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn_azul, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btn_amar, GPIO.IN, pull_up_down=GPIO.PUD_UP)   


def G_cor():
    cor_random = random.randint(1, 4)
    if cor_random == 1:
        return "V"
    elif cor_random == 2:
        return "E"
    elif cor_random == 3:
        return "A"
    elif cor_random == 4:
        return "O"
    
# basicamente, vai relacionar o G_cor com a função pisca_led, faz com que a letra gerada ative uma led.

def pisca_led(cor):
    if cor == "V":
        GPIO.output(led_verm, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_verm, GPIO.LOW)
    elif cor == "E":
        GPIO.output(led_verd, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_verd, GPIO.LOW)
    elif cor == "A":
        GPIO.output(led_azul, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_azul, GPIO.LOW)
    elif cor == "O":
        GPIO.output(led_amar, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_amar, GPIO.LOW)
    time.sleep(0.2)

# Mostra a sequencia de acertos
def mostra_sequencia(seq):
    s = 0
    while s < len(seq):
        pisca_led(seq[s])
        s = s + 1

# faz relação ao led e botão, quando se aperta o botão o led acende 
def ler_botao():
    while True:
        if GPIO.input(btn_verm) == GPIO.LOW:
            pisca_led("V")
            return "V"
        elif GPIO.input(btn_verd) == GPIO.LOW:
            pisca_led("E")
            return "E"
        elif GPIO.input(btn_azul) == GPIO.LOW:
            pisca_led("A")
            return "A"
        elif GPIO.input(btn_amar) == GPIO.LOW:
            pisca_led("O")
            return "O"
        time.sleep(0.05)

# vai identificar se o jogador acertou ou não
def V_F(sequencia, resposta):
    s = 0
    while s < len(sequencia):
        if sequencia[s] != resposta[s]:
            return False
        s = s + 1
    return True

# Código base do jogo 
def inicio_jogo():
    configuração_gpio()

    sequencia = ""
    Rolando = True

    while Rolando:
        nova_cor = G_cor()
        sequencia = sequencia + nova_cor
        mostra_sequencia(sequencia)

        print("Sua vez!")
        resposta = ""
        s = 0
        while s < len(sequencia):
            tecla = ler_botao()
            resposta = resposta + tecla
            s = s + 1

        if V_F(sequencia, resposta):
            print("Correto!")
            time.sleep(1)
        else:
            print("Resposta errada :/")
            pisca_led("V")
            pisca_led("V")
            pisca_led("V")
            continuar = False

    GPIO.cleanup()

inicio_jogo()