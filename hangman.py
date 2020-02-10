import pygame
import numpy as np
import random
import math
import os

black = (0, 0, 0)
white= (255, 255, 255)
skb=(135,206,255)
pygame.init()

height =720
width = 1280
size = [width, height]
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 60)
clock = pygame.time.Clock()
gameDisplay = pygame.display.set_mode((width,height))
game_dir = os.path.dirname(__file__)
Movie_folder = os.path.join(game_dir,'Movie')

pygame.display.set_caption("Hangman")
wor = {
"auto":"manual or..." ,
"else":"conditional",
"long":"datatype",
"switch":"cases",
"break":"loop control",
"enum":"user defined data type",
"register":"data holder",
"typedef":"define a type",
"case":"conditional control",
"extern":"extennd visibility",
"return":"leave execution",
"union":"user defined data type",
"char":"data type",
"float":"data type",
"short":"data type",
"unsigned":"non-negative",
"const":"cannot be altered",
"for":"control flow",
"signed":"",
"void":"return type",
"continue":"loop control",
"goto":"loop control",
"sizeof":"unary operator",
"volatile":"qualifier",
"default":"preexisting value",
"if":"conditional",
"static":"global variable",
"while":"control flow",
"do":"control flow",
"int":"data type",
"struct":"user defined data type",
"Packed":"structure",
"double":"data type",
"abstract":"principle of object oriented programming",
"assert":"test assumptions",
"boolean":"data type",
"byte":"data unit",
"catch":"exception handling",
"char":"data type",
"class":"user defined data type",
"extends":"Java Applet",
"finally":"exception handling",
"float":"data type",
"for":"control flow",
"goto":"loop control",
"if":"conditional",
"implements":"program execution",
"import":"include",
"instanceof":"returns boolean value",
"int":"data type",
"interface":"concept of object oriented programming",
"long":"data type",
"native":"software or data-format",
"new":"memory allocation",
"package":"namespace",
"private":"access specifier",
"protected":"access specifier",
"public":"access specifier",
"return":"leave execution",
"short":"data type",
"static":"global variable",
"super":"parent of class",
"synchronized":"",
"this":"pointer",
"throw":"exception handling",
"throws":"exception handling",
"transient":"temporary",
"try":"exception handling",
"void":"return type",
"volatile":"can be altered",
"while":"control flow",
"and":"logical operator",
"exec":"executable file",
"not":"logical operator",
"assert":"test assumption",
"finally":"exception handling",
"or":"logical operator",
"break":"loop control",
"for":"control flow",
"pass":"loop control",
"class":"user defined data type",
"from":"used in import statement",
"print":"output to consol",
"continue":"loop control",
"global":"scope is entire program",
"raise":"exception handling",
"def":"define a user-defined function",
"if":"conditional",
"return":"leave execution",
"del":"delete",
"import":"include",
"try":"exception handing",
"elif":"conditional",
"in":"test a sequence",
"while":"control flow",
"else":"conditional",
"is":"testing the object identity",
"with":"wrap execution of a block",
"except":"exception handling",
"lambda":"inline function without &nbsp; return statement",
"yield":"return dictionary"}
print(len(wor))
taken = []


def game_over(score):
    #screen.fill(black)

    text = font.render("Game Over!", True, white)
    screen.blit(text, (width/2-150, height/2-50))
    string = "Score : " + str(score)

    text = font.render(string, True, white)
    screen.blit(text, (width/2-150, height/2))
    with open('score.txt', 'a') as fout:
        fout.write(str(score))
        fout.write("\n")
    pygame.display.update()
    while True:
        pygame.time.delay(1000)


def display(keyword, selected, lives, score, time):
    string = ""
    correct_letters = 0
    for i in range(0,len(keyword)):
        if keyword[i] in selected:
            string += keyword[i] + " "
            correct_letters += 1
        else:
            string += "_ "
    text = font.render(string,True,white)
    screen.blit(text,(100,height/2-50))
    num = 10 - lives
    img_sel = "ha" + str(num)
    screen.blit(pygame.image.load("./img/"+ img_sel +".png"),(950,150))
    score_print = "Score: "+str(score)
    text = font.render(score_print, 1, white)
    text_pos = (900, 50)
    screen.blit(text, text_pos)
    min = math.floor(time/60)
    sec = int(time%60)
    rem_time = str(min) + ":" + str(sec)
    text = font.render(rem_time, 1, white)
    text_pos = (580, 50)
    screen.blit(text, text_pos)
    text_pos = (100,50)
    quetotal="Que: "+str(que)
    text = font.render(quetotal ,1, white)
    #screen.blit(text,text_pos)
    life = "Lives: "+str(lives)
    text2 = font.render(life,1,white )
    screen.blit(text2, (900, 600))
    pygame.display.update()
    return correct_letters
        

def play(score, start_ticks):
    keyword = random.choice(list(wor)).lower()
    while keyword in taken:
        keyword = random.choice(list(wor)).lower()
    #keyword="lambda"
    taken.append(keyword)
    selected = []
    lives = 10
    flag=0
    i = 1 
    hint1="Hint: "+wor.get(keyword)
   
    while True:
        pic_sel="Pictures"+str(i)+".jpg"
        I = pygame.image.load(os.path.join("./Movie/"+pic_sel))
        gameDisplay.blit(I,(0,0))
        elapsed_time = pygame.time.get_ticks() - start_ticks
        rem_time = (10*60*1000 - elapsed_time)/1000
        #screen.fill(black)
        #rem_time = 0
        if rem_time <= 0:
            game_over(score)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)
                if event.key == pygame.K_BACKSPACE:
                   score-=1
                   flag=1        
                if pressed_key not in selected and event.key!= pygame.K_BACKSPACE :
                    if pressed_key not in keyword:
                        lives -= 1
                    selected.append(pressed_key)
            
            if lives == 0:
                flag=0
                return score - 2
                    
        correct_letters = display(keyword, selected, lives, score, rem_time)
        if correct_letters == len(keyword):
            pygame.time.delay(1000)
            score += 2
            flag = 0
            return score
            break
        clock.tick(100)

        if i<1150:
            i+=1
        else:
            i=188
        if flag == 1:
            hint = font.render(hint1,1,white)
            hint_pos=(100,500)
            screen.blit(hint,hint_pos)
            pygame.display.update()

score = 0
time = 0
que = 1
start_ticks = pygame.time.get_ticks()
while True:
    score = play(score, start_ticks)
    print(score)
