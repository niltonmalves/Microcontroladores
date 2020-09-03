# COMECE COPIANDO AQUI O SEU CÓDIGO DA IMPLEMENTAÇÃO
# DEPOIS FAÇA OS NOVOS RECURSOS

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
      #player.speed = 2
      return

    def FaixaAnterior():
      if (player.time_pos > 2.00):
        player.time_pos = 0.00
        return
      player.pt_step(-1)
      return
    
    def Acelera():
      player.speed = player.speed * 2
    
    def VoltaAoNormal():
      velocidade = player.speed
      if velocidade != None and velocidade > 1:
        player.speed = 1
        return
      ProximaFaixa()
      
    def embaralhaLista():
  
      f = open("playlist.txt", "r")
      lista = f.readlines()
      random.shuffle(lista)
      f.close()
      
      f = open("playlist_nova.txt", "w")
      f.writelines(lista)
      f.close()
      
      player.loadlist("playlist_nova.txt")
      
    # criação de componentes
    player = Player()
    player.loadlist("playlist.txt")

    led = LED(21)
    
    lcd = Adafruit_CharLCD(2,3,4,5,6,7,16,2)

    button1 = Button(11)
    button2 = Button(12)
    button3 = Button(13)
    button4 = Button(14)
    
    button1.when_pressed = FaixaAnterior
   
    button2.when_pressed = TocarEPausar

    button3.when_held = Acelera

    button3.when_released = VoltaAoNormal
    button4.when_pressed = embaralhaLista

    led.on()
    # loop infinito
    while True:
      metadados = player.metadata
      posicao = player.time_pos
      duracao = player.length
      print(metadados)
      
      if (metadados != None and posicao != None and duracao != None):
        
        nome = metadados["Title"]
        #if nome > 16:
            
        tempo_atual = int(posicao)
        tamanho = int(duracao)
        
        minuto_atual = str(tempo_atual // 60)
        segundos_atual = str(int(tempo_atual % 60))
        
        tamanho_minutos = str(tamanho // 60)
        tamanho_segundos = str(int(tamanho % 60))
        
        texto = "%s:%s de %s:%s"%(minuto_atual.zfill(2),segundos_atual.zfill(2),tamanho_minutos.zfill(2),tamanho_segundos.zfill(2))
        
        lcd.clear()
        lcd.message(nome)
        lcd.message('\n')
        lcd.message(texto)
        
      sleep(0.2)

