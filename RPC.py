import pygame, sys, time, random
from pygame.locals import *


def main():
    
    pygame.init()
    mainClock = pygame.time.Clock()

    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 900
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption("Ele-mental")


    BLACK = [0, 0, 0]
    WHITE = [255, 255, 255]
    RED = [255, 0, 0]
    GREEN = [0, 255, 0]
    BLUE = [0, 0, 255]



    p_HP = 100
    ai_HP = 100
    p_combo = 0
    ai_combo = 0
    nextScreen = 0
    done = 0


    titleScreenImg = pygame.image.load("TitleScreen.png")
    fireImg = pygame.image.load("fire.png")
    waterImg = pygame.image.load("water.png")
    grassImg = pygame.image.load("grass.png")

    tutFont = pygame.font.SysFont('arial', 12)
    statFont = pygame.font.SysFont('arial',32)

    tutText1 = tutFont.render("Welcome to Ele-mental! You are a mage capeable of bending the elements to your will! Mages of this type are called Weavers and battle in the Elemental Pits for the enjoyment of the masses.", True, WHITE, BLACK)
    tutText2 = tutFont.render("At the begining of each round you and your opponent will choose an element (either FIRE, WATER, or GRASS) and sqaure off. FIRE beats GRASS, GRASS beats WATER, and WATER beats FIRE.", True, WHITE, BLACK)
    tutText3 = tutFont.render("You both start at 100HP. The winner of a round deals damage to the other Weaver and gains a combo point.", True, WHITE, BLACK)
    tutText4 = tutFont.render("The damage dealt is equal to 10hp multiplied by how many combo points you have. If you lose a round your combo points get set back to zero", True, WHITE, BLACK)
    promptText = tutFont.render("Enter your selection! 1: FIRE 2. GRASS 3. WATER",True, WHITE, BLACK)


    pHpText = statFont.render("Player HP: "+str(p_HP), True, WHITE, BLACK)
    pCpText = statFont.render("Player CP: "+str(p_combo), True, WHITE, BLACK)
    aiHpText = statFont.render("Enemy HP: "+str(ai_HP), True, WHITE, BLACK)
    aiCpText = statFont.render("Enemy CP: "+str(ai_combo), True, WHITE, BLACK)

    winText1 = statFont.render("FIRE BEATS GRASS!", True, WHITE, BLACK)
    winText2 = statFont.render("GRASS BEATS WATER!", True, WHITE, BLACK)
    winText3 = statFont.render("WATER BEATS FIRE!", True, WHITE, BLACK)
    winText4 = statFont.render("Tie!", True, WHITE, BLACK)
    winText5 = statFont.render("Player Wins!!", True, WHITE, BLACK)
    winText6 = statFont.render("Player Loses!", True, WHITE, BLACK)
    

    tutTextRect1 = tutText1.get_rect()
    tutTextRect1.center = (600, 25)

    tutTextRect2 = tutText2.get_rect()
    tutTextRect2.center = (600, 50)

    tutTextRect3 = tutText3.get_rect()
    tutTextRect3.center = (375, 75)

    tutTextRect4 = tutText3.get_rect()
    tutTextRect4.center = (375, 100)

    pHpTextRect = pHpText.get_rect()
    pHpTextRect.center = (300, 400)

    pCpTextRect = pCpText.get_rect()
    pCpTextRect.center = (300, 450)

    aiHpTextRect = aiHpText.get_rect()
    aiHpTextRect.center = (600, 400)

    aiCpTextRect = aiCpText.get_rect()
    aiCpTextRect.center = (600, 450)

    promptTextRect = promptText.get_rect()
    promptTextRect.center = (600, 50)

    winTextRect1 = winText1.get_rect()
    winTextRect1.center = (500, 100)

    winTextRect2 = winText2.get_rect()
    winTextRect2.center = (500, 100)

    winTextRect3 = winText3.get_rect()
    winTextRect3.center = (500, 100)

    winTextRect4 = winText4.get_rect()
    winTextRect4.center = (500, 100)

    winTextRect5 = winText5.get_rect()
    winTextRect5.center = (500, 200)

    winTextRect6 = winText6.get_rect()
    winTextRect6.center = (500, 200)
    
   

  

    #Title loop
    while True:
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                nextScreen = 1
        windowSurface.blit(titleScreenImg,(0,0))
        pygame.display.flip()
        if nextScreen == 1:
            break
    nextScreen = 0
            
        
    windowSurface.fill(BLACK)
    pygame.display.flip()
    #tutorial loop
    while True:
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                nextScreen = 1
    #render tutotial txt
        windowSurface.blit(tutText1, tutTextRect1)
        windowSurface.blit(tutText2, tutTextRect2)
        windowSurface.blit(tutText3, tutTextRect3)
        windowSurface.blit(tutText4, tutTextRect4)
        
        pygame.display.flip()
        if nextScreen == 1:
            break
    nextScreen = 0
    windowSurface.fill(BLACK)

            
        
    #game loop

    while True:
        p_choiceN = 0
        windowSurface.blit(promptText, promptTextRect)
        pygame.display.flip()
        #events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if done == 1:
                    main()
                elif event.key == K_1:
                    p_choiceN = 1
                elif event.key == K_2:
                    p_choiceN = 2
                elif event.key == K_3:
                    p_choiceN = 3
                else:
                    break

                ai_choiceN = random.randint(1,3)
             
                if p_choiceN == 1:
                    p_choice = "FIRE"
                    p_img = fireImg
                elif p_choiceN == 2:
                    p_choice = "GRASS"
                    p_img = grassImg
                elif p_choiceN == 3:
                    p_choice = "WATER"
                    p_img = waterImg
                if ai_choiceN == 1:
                     ai_choice = "FIRE"
                     ai_Img = fireImg
                elif ai_choiceN == 2:
                    ai_choice = "GRASS"
                    ai_Img = grassImg
                elif ai_choiceN == 3:
                    ai_choice = "WATER"
                    ai_Img = waterImg

                windowSurface.fill(BLACK)
                    
                #debug
                #print("AI int = " + str(ai_choiceN)+ " P int = " + str(p_choiceN) + " AI str = " + ai_choice + " P Str = " + p_choice+"\n\n")

                #compare choices
                #player chooses fire
                if p_choiceN== 1:
                    if ai_choiceN == 1:
                        windowSurface.blit(winText4, winTextRect4)
                    elif ai_choiceN == 2:
                        windowSurface.blit(winText1, winTextRect1)
                        p_combo += 1
                        ai_HP -= (10*p_combo)
                        ai_combo = 0
                    elif ai_choiceN == 3:
                        windowSurface.blit(winText3, winTextRect3)
                        ai_combo += 1
                        p_HP -= (10*ai_combo)
                        p_combo = 0
                #player chooses grass
                if p_choiceN== 2:
                    if ai_choiceN == 1:
                        windowSurface.blit(winText1, winTextRect1)
                        ai_combo += 1
                        p_HP -= (10*ai_combo)
                        p_combo = 0 
                    elif ai_choiceN == 2:
                         windowSurface.blit(winText4, winTextRect4)
                    elif ai_choiceN == 3:
                        windowSurface.blit(winText2, winTextRect2)
                        p_combo += 1
                        ai_HP -= (10*p_combo)
                        ai_combo = 0
                        #player chooses water
                if p_choiceN== 3:
                    if ai_choiceN == 1:
                        windowSurface.blit(winText3, winTextRect3)
                        p_combo += 1
                        ai_HP -= (10*p_combo)
                        ai_combo = 0  
                    elif ai_choiceN == 2:
                        windowSurface.blit(winText2, winTextRect2)
                        ai_combo += 1
                        p_HP -= (10*ai_combo)
                        p_combo = 0
                    elif ai_choiceN == 3:
                        windowSurface.blit(winText4, winTextRect4)

                if p_HP < 0:
                    p_HP = 0
                if ai_HP < 0:
                    ai_HP = 0
                
                pHpText = statFont.render("Player HP: "+str(p_HP), True, WHITE, BLACK)
                pCpText = statFont.render("Player CP: "+str(p_combo), True, WHITE, BLACK)
                aiHpText = statFont.render("Enemy HP: "+str(ai_HP), True, WHITE, BLACK)
                aiCpText = statFont.render("Enemy CP: "+str(ai_combo), True, WHITE, BLACK)


                

                windowSurface.blit(p_img,(300, 600))
                windowSurface.blit(ai_Img,(600, 600))
                windowSurface.blit(pHpText, pHpTextRect)
                windowSurface.blit(pCpText, pCpTextRect)
                windowSurface.blit(aiHpText, aiHpTextRect)
                windowSurface.blit(aiCpText, aiCpTextRect)
                pygame.display.flip()
                

                if p_HP <= 0:
                    windowSurface.blit(winText6, winTextRect6)
                    done = 1
                if ai_HP <= 0:
                   windowSurface.blit(winText5, winTextRect5)
                   done = 1
                
                    
            
main()


            

            
