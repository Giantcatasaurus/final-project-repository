import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load("intro.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue


# Colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
DGREY = (50, 50, 50)

pygame.init()

# Screen
size = (800, 600)
screen = pygame.display.set_mode(size)

# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()

# List of each block in the game
block_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()

# List of each goal
goal_list = pygame.sprite.Group()

class Block(pygame.sprite.Sprite):
    """ This class represents the block. """
    def __init__(self, color):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([20, 15])
        self.image.fill(color)
 
        self.rect = self.image.get_rect()
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
   
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(GREY)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(WHITE)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.x += 3
 
 
 
class Goal(pygame.sprite.Sprite):
    """ This represents the goal """
    def __init__(self, width, height):
        # Call the parent class constructor
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        
        
        # Making the top left corner the passed-in location
        self.rect = self.image.get_rect()
        self.rect.y = 510
        self.rect.x = 790        
        
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()

pygame.display.set_caption("A Maze Game Thing")

# Looping until the user clicks the close button
done = False

 

# Screen Updates
clock = pygame.time.Clock()

#Rectangle starting position
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

score = 0
currentLevel = 0
# Font
font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1
name = ""

# -------- Instruction Page Loop -----------
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1  
                if instruction_page == 4:
                    display_instructions = False                
                    
                    
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close()                                 
 
    # Set the screen background
    screen.fill(BLACK)
    # Code for introduction page 1
    
    if instruction_page == 1:
        
        text = font.render("A Game", True, WHITE)
        screen.blit(text, [350, 250])
        
        text = font.render("Please press enter to continue", True, RED)
        screen.blit(text, [225, 350])
        
        scoretext = "The high score is: " + str(score)
        text = font.render(scoretext, True, WHITE)
        screen.blit(text, [10, 10])       
        
        pygame.draw.rect(screen, RED,(390, 400, 20, 20))
        pygame.draw.rect(screen, GREY,(371, 380, 50, 10))
        pygame.draw.rect(screen, GREY,(371, 380, 10, 50))
        pygame.draw.rect(screen, GREY,(421, 380, 10, 50))
        pygame.draw.rect(screen, GREY,(371, 430, 60, 10))

    if instruction_page == 2:
        # Code for introduction page 2
              

        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 10])    
       
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 10])        
 
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])
       
    if instruction_page == 3:
        # code for introduction page 3
        text = font.render("This program is Michael's Final Project", True, RED)
        screen.blit(text, [10, 10])    
 
        text = font.render("Arrow Keys to move around", True, WHITE)
        screen.blit(text, [10, 40])
        
        text = font.render("Ok?", True, WHITE)
        screen.blit(text, [10, 80])   
                
        text = font.render("Your name is", True, WHITE)
        screen.blit(text, [320, 550])           
        
        text = font.render(name, True, WHITE)
        screen.blit(text, [320, 570])            
        
        pygame.draw.rect(screen, RED,(150, 115, 20, 20))
        
        text = font.render("This is you", True, WHITE)
        screen.blit(text, [10, 110])         
        
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
   
    score = 0
    
    
# --Backdrop Prog Loop--
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()


wall = Wall(0, 0, 10, 600)# border 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(790, 0, 10, 500)#border 2
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 0, 790, 10)# border 3
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(10, 590, 790, 10)# border 4
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 100, 700, 10)# long wall 1
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(700, 100, 10, 200)# Corner wall
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(700, 400, 10, 100)# outer path wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(600, 300, 10, 100)# outer path wall 2
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(210, 200, 400, 10)# gate outer wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(300, 300, 300, 10)# north inner wall 2
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(200, 200, 10, 300)# west inner wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 100, 10, 400)# west inner wall 2
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(100, 500, 500, 10)# south inner wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(200, 400, 300, 10)# middle inner wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(600, 400, 100, 10)# gate inner wall 1
wall_list.add(wall)
all_sprite_list.add(wall)

wall = Wall(700, 500, 100, 10)# Corner wall
wall_list.add(wall)
all_sprite_list.add(wall)

goal = Goal(10, 90)# Corner wall
goal_list.add(goal)
all_sprite_list.add(goal)



# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list

file = open('highscores.txt', 'w')
writescore = str(score) + "\n"
file.write(writescore)
writename = name + "\n"
file.write(writename)
file.close()             
all_sprite_list.add(player)
 
clock = pygame.time.Clock()
 
done = False
 #--------Main Program Loop---------
while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            file = open('highscores.txt', 'w')
            writescore = str(score) + "\n"
            file.write(writescore)
            writename = name + "\n"
            file.write(writename)
            file.close()                    
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 5)
 
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(5, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-5, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 5)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -5)

                
                
    all_sprite_list.update()
    
    screen.fill(DGREY)
 
    all_sprite_list.draw(screen)    
 
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()