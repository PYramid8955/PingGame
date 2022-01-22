import pygame as p
from pygame.locals import *
from random import choice, randint
p.init()
scr = p.display.set_mode((200,400))
p.display.set_caption("Platformer by ImNotHereToPlayGames")
icon = p.image.load('res/logo.png')
p.display.set_icon(icon)
SPD = 1
spd = 0
foo = 1
foox = 5 if randint(0,1) == 0 else -5
fooy = 5 if randint(0,1) == 0 else -5
ballx = 100
bally = 200
aix = 100
fill = (0,0,0)
again = 0
cout = 0
font = p.font.SysFont('arial', 15)
fill1 = 0
fillspd = 0
fooaix = 5
y = 1
while y:
        p.time.delay(60)
        key = p.key.get_pressed()
        pos=p.mouse.get_pos()
        scr.fill(fill)
        if pos[0] + 15 > 195:
                platformX = 165
        elif pos[0] - 15 < 5:
                platformX = 5
        else:
                platformX = pos[0] - 15
        p.draw.rect(scr, (255,255,0), (platformX, 10,30,3))
        if aix + 15 > 195:
                platformX = 165
        elif aix - 15 < 5:
                platformX = 5
        else:
                platformX = aix - 15
        p.draw.rect(scr, (255,255,0), (platformX, 390, 30, 3))
        p.draw.rect(scr, (0,255,0), (0, 0,5,400))
        p.draw.rect(scr, (0,255,0), (195, 0,5,400))
        text = font.render(str(cout), True, (100,100,100), fill)
        text2 = font.render("Game Over", True, (0,255,0), fill)
        text3 = font.render("You Won!", True, (255,255,0), fill)
        textRect = p.draw.rect(scr, fill, (95,195,5,5))
        textRect2 = p.draw.rect(scr, fill, (10,0,5,5))
        scr.blit(text, textRect)
        if spd == 0:
                if ballx <= 10:
                        foox *= -1
                if ballx >= 190:
                        foox *= -1
                if bally <= -5:
                        again = 1
                if bally >= 405:
                        again = 2
                if bally-5 <= 13 and ballx in range(pos[0]-15, pos[0]+15):
                        fooy *= -1
                        cout +=1
                if ballx-5 == pos[0] + 15 and bally in range(10, 13):
                        foox *= -1
                        fooy *= -1
                        if fooy != 3:
                                fooy -= 3
                        cout +=1
                if ballx+5 == pos[0] - 15 and bally in range(10, 13):
                        foox *= -1
                        fooy *= -1
                        if fooy != 3:
                                fooy -= 3
                        cout +=1
                if bally + 5 >= 390 and ballx in range(round(aix)-15, round(aix)+15):
                        fooy *= -1
                if cout == 25 and bally-5 <= 13 and ballx in range(pos[0]-15, pos[0]+15):
                        foox *= 2
                        fooy *= 1.5
                        fooaix *= 1.5
                        fill = (26, 0, 0)
                        fill1 = 9
                ballx += foox
                bally += fooy
                if bally >= 200 and fooy >= 0:
                        if aix < ballx:
                                aix += fooaix
                        if aix > ballx:
                                aix -= fooaix
                spd = SPD
        if fill1 != 0 and fillspd == 0:
                if fill == (26, 0, 0):
                        fill = (51, 0, 0)
                elif fill == (51, 0, 0):
                        fill = (77, 0, 0)
                elif fill == (77, 0, 0):
                        fill = (102, 0, 0)
                elif fill == (102,0,0):
                        fill = (128, 0, 0)
                elif fill == (128, 0, 0):
                        fill = (153, 0, 0)
                elif fill == (153, 0, 0):
                        fill = (179, 0, 0)
                elif fill == (179, 0, 0):
                        fill = (204, 0, 0)
                elif fill == (204, 0, 0):
                        fill = (230, 0, 0)
                elif fill == (230, 0, 0):
                        fill = (255, 0, 0)
                fill1 -= 1
                fillspd = 3
        if again == 1:
                SPD = 0
                scr.blit(text2, textRect2)
        elif again == 2:
                SPD = 0
                scr.blit(text3, textRect2)
        for event in p.event.get():
                if event.type == p.QUIT or key[p.K_ESCAPE]:
                        y = 0
                if again != 0 and event.type == p.MOUSEBUTTONUP:
                        SPD = 1
                        spd = 1
                        foo = 1
                        foox = 5 if randint(0,1) == 0 else -5
                        fooy = 5 if randint(0,1) == 0 else -5
                        ballx = 100
                        bally = 200
                        aix = 100
                        fill = (0,0,0)
                        again = 0
                        cout = 0
                        fill1 = 0
                        fillspd = 0
                        fooaix = 5
                        y = 1
        if fill1 != 0:
                fillspd -= 1
        spd -= 1
        p.draw.circle(scr, (255,0,255), (ballx, bally), 5)
        p.display.update()        
p.quit()

