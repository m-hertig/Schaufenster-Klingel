import RPi.GPIO as GPIO
import pygame
import time

GPIO.setmode(GPIO.BCM)
pins = [4,17,18,22,27,23]
prev_inputs = [True,True,True,True,True,True]

for pin in pins:
    GPIO.setup(pin,GPIO.IN)

pygame.init()
pygame.mixer.init()
print("Loading sounds and images...")
infoObject = pygame.display.Info()
# screen = pygame.display.set_mode((1280, 720), pygame.FULLSCREEN )
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
running = True
image1 = pygame.image.load("/home/pi/dynamo/images/frequenz.jpg")
image2 = pygame.image.load("/home/pi/dynamo/images/frequenz2.jpg")
image3 = pygame.image.load("/home/pi/dynamo/images/frequenz3.jpg")
image4 = pygame.image.load("/home/pi/dynamo/images/frequenz4.jpg")
image5 = pygame.image.load("/home/pi/dynamo/images/frequenz5.jpg")
image6 = pygame.image.load("/home/pi/dynamo/images/frequenz6.jpg")

images = [image1,image2,image3,image4,image5,image6]

defaultImage1 = pygame.image.load("/home/pi/dynamo/images/frequenza.jpg")
defaultImage2 = pygame.image.load("/home/pi/dynamo/images/frequenza2.jpg")

defaultImages = [defaultImage1,defaultImage2]
framecounter = 0
lastTimeSwapped = pygame.time.get_ticks()

sound1 = "/home/pi/dynamo/sounds/EvaMaria.mp3"
sound2 = "/home/pi/dynamo/sounds/TheTongue.mp3"
sound3 = "/home/pi/dynamo/sounds/AntagonistPictures.mp3"
sound4 = "/home/pi/dynamo/sounds/RetakeRecycling.mp3"
sound5 = "/home/pi/dynamo/sounds/CreativeAlchemy.mp3"
sound6 = "/home/pi/dynamo/sounds/Nextzurich.mp3"

sounds = [sound1,sound2,sound3,sound4,sound5,sound6]

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
print("Loading complete!")
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    for index, pin in enumerate(pins):
        inputVal = GPIO.input(pin)
        if (not inputVal):
            # prev_inputs[index] = inputVal
            pygame.mixer.music.load(sounds[index])
            pygame.mixer.music.play()
            print("playing sound!")
            print("Pressed "+str(pin))
            screen.fill((0,0,0))
            screen.blit(images[index],(0,0))
            clock.tick(60)
            pygame.display.flip()
    if not pygame.mixer.music.get_busy():
            screen.fill((0,0,0))
            currentTime = pygame.time.get_ticks()
            timeDiff = currentTime - lastTimeSwapped
            if timeDiff<2500:
                screen.blit(defaultImage1,(0,0))
            elif timeDiff<5000:
                screen.blit(defaultImage2,(0,0))
            else:
                screen.blit(defaultImage2,(0,0))
                lastTimeSwapped = pygame.time.get_ticks()
            pygame.display.flip()
