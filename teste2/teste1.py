import RPi.GPIO as GPIO
import random, time

## definição pinos de cada led(VERMELHO, AMARELO, VERDE, TALVEZ(BRANCO))
LED_VERM = 17##fisico: 11
LED_VERD = 18##fisico: 12
LED_AMAR = 27##fisico: 13
LED_BRAN = 22##fisisco 15

## definição pinos de cada btn
BTN_VERM = 5##fisico: 29
BTN_VERD = 6##fisico: 31
BTN_AMAR = 13##fisico: 33
BTN_BRAN = 19##fisico: 32

## setup basico ##
GPIO.setmode(GPIO.BCM)
#### LEDS ####
GPIO.setup(LED_VERM, GPIO.OUT)
GPIO.setup(LED_VERD, GPIO.OUT)
GPIO.setup(LED_AMAR, GPIO.OUT)
GPIO.setup(LED_BRAN, GPIO.OUT)
#### BTNS ####
GPIO.setup(BTN_VERM, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_VERD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_AMAR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_BRAN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#### array cor e btn ####
cores = []
btn_AP = []

#gerara o array de cores
def gen_color():
    i = 0
    while i <= 3: 
        gen_num = random.randint(0, 3)
        ##if gen_num == 0:
        ##    cores.append("VERM")  não acho que vai ficar eficiente no codigo final ent eu cortei
        ##elif gen_num == 1:
        ##    cores.append("VERD")
        ##elif gen_num == 2:
        ##    cores.append("AMAR")
        ##elif gen_num == 3:
        ##    cores.append("BRAN")

#limpa o array cores

def piscar():# 1 - ver 2 - verd 3 - amar 4 - bran
    for cor in cores:
        if cor == 0:
            GPIO.output(LED_VERM, GPIO.HIGH)
            time.sleep(0.56)
            GPIO.output(LED_VERM, GPIO.LOW)
        elif cor == 1:
            GPIO.output(LED_VERD, GPIO.HIGH)
            time.sleep(0.56)
            GPIO.output(LED_VERD, GPIO.LOW)
        elif cor == 2:
            GPIO.output(LED_AMAR, GPIO.HIGH)
            time.sleep(0.56)
            GPIO.output(LED_AMAR, GPIO.LOW)
        if cor == 3:
            GPIO.output(LED_BRAN, GPIO.HIGH)
            time.sleep(0.56)
            GPIO.output(LED_BRAN, GPIO.LOW)

def win():
    GPIO.output(LED_VERM, GPIO.HIGH)
    GPIO.output(LED_VERD, GPIO.HIGH)
    GPIO.output(LED_AMAR, GPIO.HIGH)
    GPIO.output(LED_BRAN, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(LED_VERM, GPIO.LOW)
    GPIO.output(LED_VERD, GPIO.LOW)
    GPIO.output(LED_AMAR, GPIO.LOW)
    GPIO.output(LED_BRAN, GPIO.LOW)

def cor_btn():
    trys = 0
    print("aguardando os botões")
    for i in range(4):
        while True:
            if GPIO.input(BTN_VERM) == GPIO.LOW:
                btn_AP.append(0)
                time.sleep(0.2)
                break
            elif GPIO.input(BTN_VERD) == GPIO.LOW:
                btn_AP.append(1)
                time.sleep(0.2)
                break
            elif GPIO.input(BTN_AMAR) == GPIO.LOW:
                btn_AP.append(2)
                time.sleep(0.2)
                break
            elif GPIO.input(BTN_BRAN) == GPIO.LOW:
                btn_AP.append(3)
                time.sleep(0.2)
                break
            time.sleep(0.1)
    print(btn_AP) ##vai servir mais pra debug pq eu acho que vai funcionar mas nunca se sabe

#def conf_res():
#    num_acrtos = 0
#    for cor in cores:
#        if cor == btn_AP[cor]:
#            num_acrtos += 1
#    if(num_acrtos == 3):
#        win()

#teste
def conf_res():
    if len(cores) != len(btn_AP):  # Verifica se tem o mesmo número de elementos
        return False
    
    acertos = sum(1 for c, b in zip(cores, btn_AP) if c == b)
    if acertos == len(cores):
        win()
        return True
    return False

## inicializar tudo com sua devida logica

try:
    while True:
        print("\n -- inicializou -- ")
        cores = []
        btn_AP = []

        gen_color()
        print("sequencia: ", cores)
        piscar()
        cor_btn()
        
        #conf_res()

        if conf_res():
            print("Ganhou!!!")
        else:
            print("Errou!")
        time.sleep(1)
        print("finalizou!!")
except:
    GPIO.cleanup()
    print("BUGOU. BRUTAL! Its over pro betinha")
