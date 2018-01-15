import sys, os, pygame, random, math

# Declare some variables
size = width, height = 750, 750 # Size of window
black = 0, 0, 0 # The colour black
ticc = 5 # How thicccc the line of the outside box is supposed to be
angle = 0 # The current angle of the boxes with respect to one another
message = "FRACTAL"
rndGreen = 128
rndBlue = 255

# Initialize pygame
pygame.init()
pygame.display.set_caption("Fractal")
try:
    font = pygame.font.SysFont("Bauhaus 93", 48)
except Exception as e:
    font = pygame.font.SysFont("Arial", 48)

screen = pygame.display.set_mode(size)
screen.fill(black)

# Capture the previous screen and save a scaled image of it
previousScreen = pygame.transform.rotozoom(screen.copy(),angle,1/(math.sin(math.radians(angle))+math.cos(math.radians(angle))))

# Game loop
while 1:

    # delay between each frame
    pygame.time.Clock().tick(60)

    # Check if it's supposed to exit, and if it is, exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # Fill the screen to remove the previous image
    screen.fill(black)

    # Calculate the colour needed for this frame
    frameColour = pygame.Color(int(255*math.sin(math.radians(angle*2))), rndGreen, rndBlue, 0)

    # Draw the old screen onto the new screen
    screen.blit(previousScreen, (pygame.Rect(0,0,1,1)))

    # Draw the outside box
    pygame.draw.rect(screen, frameColour, pygame.Rect(0, 0, width, height), ticc)

    # Capture the previous screen and save a scaled image of it
    previousScreen = pygame.transform.rotozoom(screen.copy(), angle, 1/(math.sin(math.radians(angle))+math.cos(math.radians(angle))))

    # Draw the text to the screen
    textWidth, textHeight = font.size(message)
    screen.blit(font.render(message, True, frameColour), pygame.Rect(width//2-textWidth//2, height//2-textHeight//2, 1, 1))

    # Update the angle for the next iteration
    angle+=1
    if (angle > 89):
        angle = 0
        # Change the randomized portion of the colour
        rndGreen = random.randint(0, 255)
        rndBlue = random.randint(0, 255)

    pygame.display.flip()
