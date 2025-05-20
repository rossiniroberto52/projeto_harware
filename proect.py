import RPI.GPIO as GPIO
import Adafruit_Python_CharLCD as LCD
import time, random

ask_pos = 0
btn_pressed = 0
c_aswer = 0
w_answer = 0

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCDPlate(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

#time1 leds (fata leds por conta da baixa pinagem do raspberry3 Model B - v1.2) -> programa: Fritzing

led1 = 4
led2 = 27
led3 = 10
led4 = 9
led5 = 11
led6 = 5
led7 = 6
led8 = 13
#time2 leds (falta leds por conta da baixa pinagem do raspberry3 Model B - v1.2) -> programa Fritzing

led9 = 21
led10 = 20
led11 = 16
led12 = 12
led13 = 19
led14 = 26

leds = [led1, led2, led3, led4, led5, led6, led7, led8, led9, led10, led11, led12, led13, led14]



GPIO.setmode(GPIO.BCM)
GPIO.setup(07, GPIO.input, pull_up_down=GPIO.PUD_UP)
GPIO.setup(08, GPIO.input, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.input, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.input, pull_up_down=GPIO.PUD_UP)

def gen_nums():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    num3 = random.randint(0, 3)
    return num1, num2, num3

def display_nums(num1, num2, num3):
    lcd.cursor(0, 0)
    if num3 == 0:
        lcd.message(f"{num1} + {num2} = ?")
    elif num3 == 1:
        lcd.message(f"{num1} - {num2} = ?")
    elif num3 == 2:
        lcd.message(f"{num1} * {num2} = ?")
    elif num3 == 3:
        lcd.message(f"{num1} / {num2} = ?")

def gen_answers(num1, num2, num3):
    if num3 == 0:
        c_aswer = num1 + num2
        w_answer = num1 + num2 + random.randint(1, 10)
        lcd.cursor(0, 2)
        if ask_pos == 0:
            lcd.message(f"{c_aswer} || {w_answer}")
        else:
            lcd.message(f"{w_answer} || {c_aswer}")
    elif num3 == 1:
        c_aswer = num1 - num2
        w_answer = num1 - num2 + random.randint(1, 10)
        lcd.cursor(0, 2)
        if ask_pos == 0:
            lcd.message(f"{c_aswer} || {w_answer}")
        else:
            lcd.message(f"{w_answer} || {c_aswer}")
    elif num3 == 2:
        c_aswer = num1 * num2
        w_answer = num1 * num2 + random.randint(1, 10)
        lcd.cursor(0, 2)
        if ask_pos == 0:
            lcd.message(f"{c_aswer} || {w_answer}")
        else:
            lcd.message(f"{w_answer} || {c_aswer}")
    elif num3 == 3:
        c_aswer = num1 / num2
        w_answer = num1 / num2 + random.randint(1, 10)
        lcd.cursor(0, 2)
        ask_pos = random.randint(0, 1)
        if ask_pos == 0:
            lcd.message(f"{c_aswer} || {w_answer}")
        else:
            lcd.message(f"{w_answer} || {c_aswer}")
    return c_aswer, w_answer

def check_answer(num3, ask_pos, btn, c_aswer):
    acertou = False
    if num3 == 0:
        if(ask_pos == 0):
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
        else:
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
    elif num3 == 1:
        if(ask_pos == 0):
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
        else:
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
    elif num3 == 2:
        if(ask_pos == 0):
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
        else:
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
    elif num3 == 3:
        if(ask_pos == 0):
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
        else:
            if(btn == c_aswer):
                lcd.message("+1 ponto")
                time.sleep(2)
                lcd.clear()
            else:
                lcd.message("não consegue né!?")
                time.sleep(2)
                lcd.clear()
    return acertou

def check_btn_pressed():
    if GPIO.input(07) == GPIO.LOW:
        btn_pressed = 1
    elif GPIO.input(08) == GPIO.LOW:
        btn_pressed = 2
    elif GPIO.input(15) == GPIO.LOW:
        btn_pressed = 3
    elif GPIO.input(14) == GPIO.LOW:
        btn_pressed = 4

def led_on(btn_pressed):
    for i in leds:
        if(check_answer(num3, ask_pos, btn_pressed, c_aswer) == True):
            GPIO.output(i, GPIO.HIGH)
        else:
            GPIO.output(i, GPIO.LOW)
try:
    while True:
        lcd.clear()
        while True:
            num1, num2, num3 = gen_nums()
            display_nums(num1, num2)
            gen_answers(num1, num2, num3)
            time.sleep(2)
            check_answer(num1, num2, num3, ask_pos, check_btn_pressed, c_aswer)
            led_on(btn_pressed)
except:
    GPIO.cleanup()
    lcd.clear()
    lcd.message("ERROR")
    time.sleep(2)