import pygame
import os  # cmd
import time
from random import randint  # Random -> int

try:
    pygame.init()
except:
    print("ERRO ! O Modulo 'Pygame' Não Foi Inicializado !")
    print("Você Pode Instala-lo Com o CMD :")
    print("pip install pygame --user")


# sairaomorrer = False  # int(
#    input(print("Sair (Game Over) ao Encostar nas Bordas ? 1 -> Sim , 0 -> Não"))
# )
# if sairaomorrer == 1:
#     sairaomorrer = True
# elif sairaomorrer == 0:
#     sairaomorrer = False
# else:
#     print("Error , Porém Vou Finjir que foi um Não .")
#     sairaomorrer = False

SCREEN_WIDTH = 640   # 600
SCREEN_HEIGHT = 480  # 400

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
title = pygame.display.set_caption("Snake Game.py")

# -STR- -Int- -Bool -Bool-
# Name, Size, Bold, Italic
# 12 -> Muito Pequeno, 24 -> MédioPequeno, 40 -> Normal ,120 -> grande
font = pygame.font.SysFont("Consolas", 40, False, False)

BACKGROUND = pygame.image.load('media/background.png')
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))


def writeMsg(msg, color):
    text = font.render(msg, True, color)
    BACKGROUND.blit(text, [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2])


def writeMsg2(msg, color):
    text = font.render(msg, True, color)
    BACKGROUND.blit(text, [5, 320])


def writeMsg3(msg, color):
    text = font.render(msg, True, color)
    BACKGROUND.blit(text, [5, 380])


def fechar(Pontos):
    events = pygame.event.get()

    writeMsg("Game Over !", RED)
    writeMsg2("Press Any Key To Continue !", BLACK)
    writeMsg3("Score : "+str(Pontos), BLACK)
    pygame.display.update()

    for event in events:
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            title = pygame.display.set_caption("Game.py - Exiting")
            print("Exiting .")
            time.sleep(0.5)
            print("Exiting ..")
            time.sleep(0.8)
            print("Exiting ...")
            time.sleep(1.5)
            print("Exiting .")
            time.sleep(1)
            print("Exiting ..")
            time.sleep(0.5)
            print("Exiting ...")
            time.sleep(0.5)
            time.sleep(1)
            os.system('cmd /k "taskkill /f /IM game.exe"')
            # os.system('cmd /k "taskkill /f /IM python.exe"') # kill the game
            # pygame.quit() # Exit the game


# cores:
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (45, 45, 45)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 242, 0)
ORANGE = (255, 200, 15)
PURPLE = (162, 72, 164)


# Jogo Da Cobrinha:
tamanho = 10
# pos_x = SCREEN_WIDTH / 2
# pos_y = SCREEN_HEIGHT / 2


def Snake(SnakeXY):
    for XY in SnakeXY:
        pygame.draw.rect(screen, BLACK, [XY[0], XY[1], tamanho, tamanho])


def Apple(apple_pos_x, apple_pos_y):
    pygame.draw.rect(screen, RED, [apple_pos_x, apple_pos_y, tamanho, tamanho])


def game():
    Gameover = False

    pos_x = randint(0, (SCREEN_WIDTH-tamanho)/10) * 10
    pos_y = randint(0, (SCREEN_HEIGHT - tamanho) / 10) * 10

    apple_x = randint(0, (SCREEN_WIDTH-tamanho)/10) * 10
    apple_y = randint(0, (SCREEN_HEIGHT - tamanho) / 10) * 10

    vel_x = 0
    vel_y = 0

    SnakeXY = []
    SnakeWidth = 5

    clock = pygame.time.Clock()

    cheats = False
    cheatTries = 0

    Score = 0

    sairaomorrer = False
    print("Press 1 To (Des)Enable GameOver on Colide to the Border !")

    while True:

        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                title = pygame.display.set_caption("Game.py - Exiting")
                print("Exiting .")
                time.sleep(0.5)
                print("Exiting ..")
                time.sleep(0.8)
                print("Exiting ...")
                time.sleep(1.5)
                print("Exiting .")
                time.sleep(1)
                print("Exiting ..")
                time.sleep(0.5)
                print("Exiting ...")
                time.sleep(0.5)
                time.sleep(1)
                os.system('cmd /k "taskkill /f /IM python.exe"')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    if cheats == False:
                        print("Cheats Enabled !")
                        cheats = True
                        sairaomorrer == False
                    elif cheats == True:
                        print("Cheats Disabled !")
                        cheats = False
                        sairaomorrer == True
                elif event.key == pygame.K_1:
                    if sairaomorrer == True:
                        sairaomorrer = False
                        print("Exit on Colide With Border = False")
                    elif sairaomorrer == False:
                        sairaomorrer = True
                        print("Exit on Colide With Border = True")
                elif event.key == pygame.K_EQUALS and cheats == True:
                    print(f"Debug: SnakeWidth : {SnakeWidth}")
                    SnakeWidth += 1
                elif event.key == pygame.K_EQUALS and cheats == False:
                    if cheatTries < 3:
                        print(
                            "Cheats Desabled ! Please Press '0' To Enable !")
                        cheatTries += 1
                    elif cheatTries == 3:
                        print(
                            "Cheats Desabled ! Please Press '0' To Enable ! or Go F*ck Yourself ! >:( ")

                if event.key == pygame.K_1:
                    keyDebug = True
                elif event.key == pygame.K_2:
                    keyDebug = False

        screen.blit(BACKGROUND, (0, 0))

        # Se nao tiver BACKGROUND => screen.fill(colors['RED'])
        # cobrinha :
        #pygame.draw.rect(screen, BLACK, [pos_x, pos_y, tamanho, tamanho])

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and vel_x != -tamanho:
                if(vel_x != 1.5):
                    vel_x = tamanho  # + 1.5
                    vel_y = 0
                #pos_x += 2
            elif event.key == pygame.K_LEFT and vel_x != tamanho:
                if(vel_x != -1.5):
                    vel_x = -tamanho  # - 1.5
                    vel_y = 0
                # pos_x -= 2
            elif event.key == pygame.K_UP and vel_y != tamanho:
                if(vel_y != -1.5):
                    vel_y = -tamanho  # - 1.5
                    vel_x = 0
                # pos_y -= 2
            elif event.key == pygame.K_DOWN and vel_y != -tamanho:
                if(vel_y != 1.5):
                    vel_y = tamanho  # + 1.5
                    vel_x = 0
                # pos_y += 2

        pos_x += vel_x
        pos_y += vel_y

        SnakeHead = []  # Inicio da cobra
        SnakeHead.append(pos_x)
        SnakeHead.append(pos_y)
        SnakeXY.append(SnakeHead)

        if len(SnakeXY) > SnakeWidth:
            del SnakeXY[0]
        if any(Bloco == SnakeHead for Bloco in SnakeXY[-1]):
            fechar(Score)

        Snake(SnakeXY)
        if pos_x == apple_x and pos_y == apple_y:
            apple_x = randint(0, (SCREEN_WIDTH - tamanho)/10) * 10
            apple_y = randint(0, (SCREEN_HEIGHT - tamanho) / 10) * 10
            SnakeWidth += 1
            Score += 1
            print(f"Score : {Score} | Lenght: {SnakeWidth}")

        Apple(apple_x, apple_y)

        pygame.display.update()
        clock.tick(15)  # 15 -> devagar , 1 -> eu
        # Dar a Volta (Sem Colisao) :
        if sairaomorrer == False:
            if pos_x > SCREEN_WIDTH:
                pos_x = 0
            if pos_x < 0:
                pos_x = SCREEN_WIDTH - tamanho
            if pos_y > SCREEN_HEIGHT:
                pos_y = 0
            if pos_y < 0:
                pos_y = SCREEN_HEIGHT - tamanho
        elif sairaomorrer:
            # Fechar (Com Colisao) [Game Over] :
            if pos_x > SCREEN_WIDTH:
                fechar(Score)
            if pos_x < 0:
                fechar(Score)
            if pos_y > SCREEN_HEIGHT:
                fechar(Score)
            if pos_y < 0:
                fechar(Score)

        # pygame.init()


game()

"""
# if player.pos_x >= obj['espinho'].pos_x:
if player esta colidindo com objeto espinho:
    player = pygame.image.load("PlayerMorte.png")
    playerEstaMorto = True
while playerEstaMorto and GamePausado == False:
    txto = setText("Gameover")
while playerEstaMorto == False:
    if tecla == K_d:
        andar('direita')

def andar(e):
    if e == "direita":
        player.xPos += 1

if event == esc:
    game.pausado = True
while GamePuasado:
    setText("Pausado")
    timer.stop
"""


"""
RGB = ("Red", "Green", "Blue")  # DarkesrGrey = '#323232'
colors = []

colors['WHITE'] = (255, 255, 255)
colors['BLACK'] = (0, 0, 0)
colors['GREY'] = (45, 45, 45)

colors['RED'] = (255, 0, 0)
colors['GREEN'] = (0, 255, 0)
colors['BLUE'] = (0, 0, 255)

colors['YELLOW'] = (255, 242, 0)
colors['ORANGE'] = (255, 200, 15)
colors['PURPLE'] = (162, 72, 164)

"""
