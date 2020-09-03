from extra.aula import rodar

from Adafruit_CharLCD import Adafruit_CharLCD

@rodar
def programa():
    
    # importação de bibliotecas
    from gpiozero import LED
    from gpiozero import Button
    from time import sleep


    # definição de funções
    def apertaELiga():
      led.toggle()
      return
    
    def piscaQuatro():
      led2.blink(n=4)
      return

    def piscaContinuamente(): 
      led3.blink(on_time=1, off_time=3.0)

      return
    
    def Noaperto():
      global count
      count = count + 1
      lcd.clear()
      lcd.message(str(count))
      piscaQuatro()
      return

    def mantemAceso():
      led5.on()
      return

    # criação de componentes
    led  = LED(21)
    led2 = LED(22)
    led3 = LED(23)
    led5 = LED(25)
    button = Button(11)
    button2 = Button(12)
    button3 = Button(13)

    lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)

    global count
    count = 0

    button.when_pressed = apertaELiga
    button2.when_pressed = Noaperto

    piscaContinuamente()

    # loop infinito
    while True:
        if (led3.is_lit and button3.is_pressed):
          mantemAceso()
        else:
          led5.off()
        sleep(0.2)
