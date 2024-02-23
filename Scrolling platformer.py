import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Side-Scrolling Game')
mousePos = (400,400)
clock = pygame.time.Clock()
img = pygame.image.load("forest.jpg").convert() #loads image, goes above globals
player = [100, 450, 0, 0]
isOnGround = False
offset = 0
platforms = [(500, 400), (700, 300), (800, 200), (900, 300), (1000, 400),(1200,273), (1400, 400), (1600, 200) ]

#keys = [False, False, False, False]

player = [100, 496, 0, 0]#xpos, ypos, xvel, yvel

def move_player():
    global isOnGround #needed to modify a global variable from within a function
    global offset
    
    isOnGround = False
    
    if player[1] > 543-50:#Check for ground collision
        player[1] = 543-50
        isOnGround = True
        
    for i in range(len(platforms)):#Platform collison
        if player[0]+50>platforms[i][0]+offset and player[0]<platforms[i][0]+100+offset and player[1]+50>platforms[i][1] and player[1]+50< platforms[i][1]+50:
            isOnGround = True
            player[1]=platforms[i][1]-50
            player[3] = 0
            
            
    if keys[pygame.K_LEFT]:#Left and Right keyboard movement
        if offset > 260 and player[0]>0:#Check if you've reached the left edge of the map
           player[2] = -5 #Let player get back to the center of the game screen
           
        elif player[0]>400 and offset < -1500: #Check if we're on the far right edge of the map
            player[2] = -5 #Let player get back to the center of the game screen
            
        elif player[0]>0:#If player is recentered, Move the *offset*, not the player
            offset += 5
            player[2] = 0
            
        else:
            player[2]=0 #Make sure motion is off (stops from going off edge)
    
    elif keys[pygame.K_RIGHT]:
        if offset < -1500 and player[0]<750:#Check if you've reached the right edge of the map
            player[2] = 5#Let player get back to the center of the game screen
        
        elif offset >260 and player[0]<400:#check if we're on the far left edge of the map
            player[2] = 5#Let players get back to the center of the game screen
            
        elif player[0]<750:#If player is recentered, Move the *offset*, not the player
            offset -= 5
            player[2] = 0
            
        else:
            player[2]=0
        
    #Jump mechanics
    if isOnGround == True and keys[pygame.K_UP]:
        player[3] = -20 #Player jumps
        isOnGround = False  
    
    
    if isOnGround == False:
        player[3] += 1 #gravity
        
    if isOnGround == True:
        player[3] = 0
        
    player[0]+=player[2] #Add velocity to x position
    player[1]+=player[3] #Add velocity to y position
    
    
    
    
        
    #print(player[0], player[1])
running = True
def draw_clouds():
    #Draw clouds in the background
    for x in range(100, 3000, 200): #Controls where and how many clouds are drawn
        for i in range(3): #Draw 3 circles
            pygame.draw.circle(screen, (255, 255, 255), (x + offset, 100), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x-50 + offset, 125), 40)
            pygame.draw.circle(screen, (255, 255, 255), (x+50 + offset, 125), 40)
        pygame.draw.rect(screen, (255, 255, 255), (x-50 + offset, 100, 100, 65))#Flattens bottom edge

def draw_tree():
     for x in range(100, 3000, 300): #Controls where and how many clouds are drawn
        for i in range(3): #Draw 3 circles
            pygame.draw.rect(screen, (102, 51, 0), (x+8 + offset, 309, 33, 300))
            pygame.draw.circle(screen, (0, 204, 0), (x+70 + offset, 300), 40)
            pygame.draw.circle(screen, (0, 204, 0), (x+24 + offset, 270), 40)#Add or subtract to x to move left or right and add to 125/y to move up or down
            pygame.draw.circle(screen, (0, 204, 0), (x-20 + offset, 300), 40)

def draw_platforms():
    for i in range(len(platforms)):
        pygame.draw.rect(screen, (150, 10, 10), (platforms[i][0] + offset, platforms[i][1], 100, 30))
            

  
while running: # Main game loop----------------------------
    clock.tick(60) #set the FPS
    #input section--------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        print(mousePos) 
    
    keys = pygame.key.get_pressed()
    #Physics section----------------------------------------
    move_player()
    #Render section-----------------------------------------
    screen.blit(img, (0, 0)) #draws to screen, goes in render section
    
    
    
    draw_clouds()#Function call
    
    draw_tree()
    
    draw_platforms()
    
    pygame.draw.rect(screen, (0, 204, 0), (0, 543, 800, 115))#Draw ground  
    pygame.draw.rect(screen, (255, 0, 255), (player[0], player[1], 50, 50)) #player
    pygame.display.flip()
    
   
    
pygame.quit() 
