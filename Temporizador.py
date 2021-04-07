import time
import pygame

def alarma(repeticiones):
  return repeticiones

2
def tiempo(duracion,tipo):
  
  if tipo == 1:
    i=0
    while(i<duracion):
      i+=1
      print(i)
      time.sleep(1)
    print('el tiempo terminó')
    pygame.mixer.init()
    #pygame.mixer.Sound.play(pygame.mixer.Sound('alarma1.ogg'))
    sound = pygame.mixer.Sound("alarma1.ogg")
    sound.play()
    time.sleep(5)
  elif tipo == 2:
    i=0
    while(i<duracion):
      i+=1
      print(i)
      time.sleep(1)
    print('el tiempo terminó')
    pygame.mixer.init()
    #pygame.mixer.Sound.play(pygame.mixer.Sound('alarma1.ogg'))
    sound = pygame.mixer.Sound("alarma2.ogg")
    sound.play()
    time.sleep(5)    

d = int(input('¿Cuantos segundos desea trabajar?'))
tiempo(d,1)
tiempo(60-d,2)

  
