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
    "auto":"manual or...",
    "else":"conditional",
    "long":"datatype",
    "switch":"cases",
    "break":"",
    "enum":"",
}
'''
  "register",
    "typedef",
    "case",
    "extern",
    "union",
    "char",
    "float",
    "short",
    "unsigned",
    "const",
    "for",
    "signed",
    "void",
    "continue",
    "goto",
    "sizeof",
    "volatile",
    "default",
    "if",
    "static",
    "while",
    "do",
    "int",
    "struct",
    "Packed",
    "double",
    "abstract",
    "assert",
    "boolean",
    "break",
    "byte",
    "case",
    "catch",
    "char",
    "class",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extends",
    "finally",
    "float","for",
    "goto",
    "if",
    "implements",
    "import",
    "instanceof",
    "int",
    "interface",
    "long",
    "native",
    "new",
    "package",
    "private",
    "protected",
    "public",
    "short",
    "static",
    "super",
    "synchronized",
    "this",
    "throw",
    "throws",
    "transient",
    "try",
    "void",
    "volatile","while",
    "and",
    "exec",
    "not",
    "assert",
    "finally",
    "or",
    "break",
    "for",
    "pass",
    "class",
    "from",
    "print",
    "continue",
    "global",
    "raise",
    "def",
    "if",
    "return",
    "del",
    "import",
    "try",
    "elif",
    "in",
    "while",
    "else",
    "is",
    "with",
    "except",
    "lambda",
    "yield"
'''
print(len(wor))
taken = []

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
    
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
        

def game_over(score):
    #screen.fill(black)
    text = font.render("Game Over!", True, white)
    screen.blit(text, (width/2-150, height/2-50))
    string = "Score : " + str(score)
    text = font.render(string, True, white)
    screen.blit(text, (width/2-150, height/2))
    pygame.display.update()
    while True:
        pygame.time.delay(1000)
        

        
def game_loop():
	score = 0
	time = 0
	start_ticks = pygame.time.get_ticks()
	while True:
	    score = play(score, start_ticks)
	    print(score)


def quitgame():
	pygame.quit()
	sys.exit()        


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
    screen.blit(text,(50,height/2-50))
    num = 10 - lives
    img_sel = "ha" + str(num)
    screen.blit(pygame.image.load("./img/"+ img_sel +".png"),(800,150))
    score_print = str(score)
    text = font.render(score_print, 1, white)
    text_pos = (800, 50)
    screen.blit(text, text_pos)
    min = math.floor(time/60)
    sec = int(time%60)
    rem_time = str(min) + ":" + str(sec)
    text = font.render(rem_time, 1, white)
    text_pos = (50, 50)
    screen.blit(text, text_pos)
    pygame.display.update()
    return correct_letters
        

def play(score, start_ticks):
    keyword = random.choice(list(wor)).lower()
    while keyword in taken:
        keyword = random.choice(list(wor)).lower()
    taken.append(keyword)
    selected = []
    lives = 10
    flag = 0
    i = 1    
    hint1 = wor.get(keyword)
    print(hint1)
    while True:
        I = pygame.image.load(os.path.join(Movie_folder,f'Pictures{i}.jpg'))
        gameDisplay.blit(I,(0,0))
        elapsed_time = pygame.time.get_ticks() - start_ticks
        rem_time = (10*60*1000 - elapsed_time)/1000
        #screen.fill(black)
        if rem_time <= 0:
            game_over(score)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pressed_key = pygame.key.name(event.key)   
                if event.key == pygame.K_BACKSPACE:
                    lives +=1
                    score -=1
                    flag = 1
                    

                
                if pressed_key not in selected:
                    if pressed_key not in keyword:
                        lives -= 1
                    selected.append(pressed_key)
            
            if lives == 0:
                flag = 0
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
                    hint = font.render('Hint :'+hint1,1,white)
                    hint_pos = (100, 100)
                    screen.blit(hint, hint_pos)
                    pygame.display.update()

game_intro()
