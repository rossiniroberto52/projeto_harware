import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

led_vermelho = 18
led_amarelo = 23
led_verde = 24
led_azul = 25

btn_vermelho = 5
btn_amarelo = 8
btn_verde = 12
btn_azul = 13

btn_inicio = 16

GPIO.setup(led_vermelho, GPIO.OUT)
GPIO.setup(led_amarelo, GPIO.OUT)
GPIO.setup(led_verde, GPIO.OUT)
GPIO.setup(led_azul, GPIO.OUT)

GPIO.setup(btn_vermelho, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_amarelo, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_verde, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_azul, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_inicio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def acender_led(pino_led, tempo):
    GPIO.output(pino_led, GPIO.HIGH)
    time.sleep(tempo)
    GPIO.output(pino_led, GPIO.LOW)
    time.sleep(0.3)

def mostrar_sequencia(led1, led2, led3):
    acender_led(led1, 0.5)
    acender_led(led2, 0.5)
    acender_led(led3, 0.5)

def ler_botao():
    while True:
        if GPIO.input(btn_vermelho) == GPIO.HIGH:
            while GPIO.input(btn_vermelho) == GPIO.HIGH:
                time.sleep(0.05)
            return led_vermelho
        elif GPIO.input(btn_amarelo) == GPIO.HIGH:
            while GPIO.input(btn_amarelo) == GPIO.HIGH:
                time.sleep(0.05)
            return led_amarelo
        elif GPIO.input(btn_verde) == GPIO.HIGH:
            while GPIO.input(btn_verde) == GPIO.HIGH:
                time.sleep(0.05)
            return led_verde
        elif GPIO.input(btn_azul) == GPIO.HIGH:
            while GPIO.input(btn_azul) == GPIO.HIGH:
                time.sleep(0.05)
            return led_azul

while True:
    if GPIO.input(btn_inicio) == GPIO.HIGH:
        tempo_pressionado = time.time()
        while GPIO.input(btn_inicio) == GPIO.HIGH:
            time.sleep(0.1)
        duracao = time.time() - tempo_pressionado

        if duracao > 2:
            break 
        
        lista_leds = [led_vermelho, led_amarelo, led_verde, led_azul]
        primeiro_led = random.choice(lista_leds)
        segundo_led = random.choice(lista_leds)
        terceiro_led = random.choice(lista_leds)

        mostrar_sequencia(primeiro_led, segundo_led, terceiro_led)

        acertos = 0

        resposta1 = ler_botao()
        acender_led(resposta1, 0.3)
        if resposta1 == primeiro_led:
            acertos += 1

        resposta2 = ler_botao()
        acender_led(resposta2, 0.3)
        if resposta2 == segundo_led:
            acertos += 1

        resposta3 = ler_botao()
        acender_led(resposta3, 0.3)
        if resposta3 == terceiro_led:
            acertos += 1

        if acertos == 3:
            acender_led(led_verde, 0.2)
            acender_led(led_verde, 0.2)
            acender_led(led_verde, 0.2)
        else:
            acender_led(led_vermelho, 0.2)
            acender_led(led_vermelho, 0.2)
            acender_led(led_vermelho, 0.2)

        time.sleep(1)

GPIO.cleanup()