from extra.aula import rodar

@rodar
def programa():
    
    # importação de bibliotecas
    from time import sleep
    from mplayer import Player
    from gpiozero import LED
    from gpiozero import Button
    from Adafruit_CharLCD import Adafruit_CharLCD


    # definição de funções
    #player.loadfile("musica.mp3")
    #player.loadlist("lista.txt")

    def TocarEPausar():
      player.pause()
      if (player.paused):
        led.blink()
      else:
        led.on()


    def ProximaFaixa():
      player.pt_step(1)
      return

    def FaixaAnterior():
      if (player.time_pos > 2.00):
        player.time_pos = 0.00
        return
      player.pt_step(-1)
      return

    # criação de componentes
    player = Player()
    player.loadlist("playlist.txt")

    led = LED(21)
    
    lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)

    button1 = Button(11)
    button2 = Button(12)
    button3 = Button(13)
    
    button1.when_pressed = FaixaAnterior
    button2.when_pressed = TocarEPausar
    button3.when_pressed = ProximaFaixa

    led.on()
    # loop infinito
    while True:
      metadados = player.metadata
      if metadados != None: 
        nome = player.metadata["Title"]
        lcd.clear()
        lcd.message(nome)
      sleep(0.2)

