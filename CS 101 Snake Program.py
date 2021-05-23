##CS 101
##Program 5
##Cory Free
##cmfm98@mail.umsl.edu
##
##PROBLEM: Create a game of snake where you move around the grid
##         collecting food pellets. Each time you collect one your
##         snake grows. You lose if you hit the walls or your own snake.
##
##ALGORITHM:
##      1. Call the main game function which initializes variables and creates a window
##      2. Create a list that has every point in window for the game
##      3. Make a block that will be the food block.
##      4. Make a block that will be the snake
##      5. Call the title function to display the rules
##      6. Make the snake move and change direction when another key is inputted
##      7. If the snake runs into the wall or ceiling or itself then call the end_screen function
##      8. Display the score and give instructions for restarting or quitting the game
##      9. If they input up then call the main_game function again
##      10. If they input down then end the game
##
##ERROR HANDLING: None
##
##OTHER COMMENTS: None
############################################################

## import these modules to use later on
import random
import time
import python_graphics as gfx

## Create a function for the title screen that displays the instructions
def title():
    ''' This function displays the instructions and ends when the user inputs right '''
    instructions = '''
Welcome to snake. Collect the food pellets
to grow your snake and increase your score.
If you run into your snake or hit the walls
then you lose.

Press the right on the arrow keys to begin.'''
## get the global variable win so that you can add text to the window
    global win
## get the last input from the user and return False when right is pressed
    start_game = win.get_last_key()
    while start_game != 'Right':
        win.draw_text(150, 100, instructions, 'yellow')
        win.draw_screen()
        start_game = win.get_last_key()
    return False

## Create a function to show the score and ask if they want to play again
def end_screen(score):
    ''' This function displays the score you lose '''
    global win
    restart_game = win.get_last_key()
    while True:
        end_text = '''
You lost! Your total score was %d.
Press up to play again, or
down to end game.''' %score
        win.draw_text(150, 150, end_text, 'white')
        win.draw_screen()
        restart_game = win.get_last_key()
        if restart_game == 'Up':
            main_game()
        elif restart_game == 'Down':
            return

## This is the main function that is the actual game itself
def main_game():
    score = 0
    bw = 140
    bh = 159
    global win
    win.draw_screen()
    snake = [ [bw, bh] ]
    b_len = 19
    movement = 20



## This creates a list that is the whole grid that the snake can be in
    viable_food_nums = [ [0, 19], [20, 39], [40, 59], [60, 79], [80, 99],
                         [100, 119], [120, 139], [140, 159], [160, 179],
                         [0, 39], [0, 59], [0, 79], [0, 99], [0, 119], [0, 139],
                         [0, 159], [20, 179], [20, 59], [20, 79],
                         [20, 99], [20, 119], [20, 139], [20, 159], [20, 179],
                         [40, 39], [40, 79], [40, 99], [40, 119], [40, 139],
                         [40, 159], [40, 179], [60, 39], [60, 59],
                         [60, 99], [60, 119], [60, 139], [60, 159], [60, 179],
                         [80, 39], [80, 59], [80, 79], [80, 119], [80, 139],
                         [80, 159], [80, 179], [100, 39], [100, 59], [100, 79],
                         [100, 99], [100, 139], [100, 159], [100, 179],
                         [120, 39], [120, 59], [120, 79], [120, 99], [120, 119],
                         [120, 159], [120, 179], [140, 39], [140, 59], [140, 79],
                         [140, 99], [140, 119], [140, 139], [140, 179],
                         [160, 39], [160, 59], [160, 79], [160, 99], [160, 119], [160, 139],
                         [160, 159], [180, 39], [180, 59], [180, 79],
                         [180, 99], [180, 119], [180, 139], [180, 159], [180, 179], [20, 219],
                         [20, 239], [20, 259], [20, 279], [0, 219],
                         [0, 239], [0, 259], [0, 279], [40, 219],
                         [40, 239], [40, 259], [40, 279], [60, 219],
                         [60, 239], [60, 259], [60, 279], [80, 219],
                         [80, 239], [80, 259], [80, 279], [100, 219],
                         [100, 239], [100, 259], [100, 279], [120, 219],
                         [120, 239], [120, 259], [120, 279], [140, 219],
                         [140, 239], [140, 259], [140, 279], [160, 219],
                         [160, 239], [160, 259], [160, 279], [180, 219],
                         [180, 239], [180, 259], [180, 279], [200, 219],
                         [200, 239], [200, 259], [200, 279], [220, 219],
                         [220, 239], [220, 259], [220, 279], [240, 219],
                         [240, 239], [240, 259], [240, 279], [260, 219],
                         [260, 239], [260, 259], [260, 279], [280, 219],
                         [280, 239], [280, 259], [280, 279], [0, 199], [20, 199],
                         [40, 199], [60, 199], [80, 199], [100, 199], [120, 199],
                         [140, 199], [160, 199], [180, 199], [200, 199], [220, 199],
                         [240, 199], [260, 199], [280, 199] ] 

## This makes the food pellet spawn in a random square
    food_x_val = random.choice(viable_food_nums)
    food = [food_x_val[0], food_x_val[1]]

## call the title function
    new_head = [snake[0][0], snake[0][1]]

    beginning = title()
    lastkey = 'Right'
    while beginning == False:
        
        new_head = [snake[0][0], snake[0][1]]
        win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')   

        for i in snake:
            win.draw_rect(i[0], i[1], i[0]+b_len, i[1]+b_len, 'blue')

        win.draw_screen()

## this checks to see if the snake is out of bounds or if it hits itself
        if new_head in snake[2:] \
           or 319 < new_head[0]+b_len or new_head[0] < -19 \
           or 319 < new_head[1]+b_len or new_head[1] < -1:
            end_screen(score)
            break

#        lastkey = win.get_last_key()
        
## Create a while loop for each direction
        while lastkey == 'Left':
            time.sleep(0.1) #make the code delay for .1 seconds
            new_head = [snake[0][0], snake[0][1]] #make sure the head is at the start of the snake
            for i in snake: #draw a block for each block in snake
                win.draw_rect(i[0], i[1], i[0]+b_len, i[1]+b_len, 'blue')
            win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red') #draw a square for the food
            win.draw_screen() 
            new_head[0] -= movement #change direction of the snake
            snake.insert(0, new_head) #make a new block at the beginning of snake
            lastkey = win.get_last_key() #check the last key entered
        #check to see if the snake hits itself
        #check if the snake hits the walls
            if new_head in snake[2:] \
           or 319 < new_head[0]+b_len or new_head[0] < -19 \
           or 319 < new_head[1]+b_len or new_head[1] < -1:
                end_screen(score) #calls the end screen function
                break

            ## This is for if the snake head hits a food pellet
            if new_head[0] == food[0] and new_head[1] == food[1]:
                food = None
                score += 1 #add one to the score
                while food is None:
                    x_val_food = random.choice(viable_food_nums) #This assigns the food to a new square
                    newfood = [
                        x_val_food[0],
                        x_val_food[1]
                    ]
                    food = newfood if newfood not in snake else None #make sure food doesnt spaw inside snake

    ## This draws the actual food pellet and draws a snake block to increase the length of the snake
                win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
                win.draw_rect(snake[1][0], snake[1][1], snake[1][0]+b_len, snake[1][1]+b_len, 'blue')
            else:
                tail = snake.pop()
            if lastkey == None:
                lastkey = 'Left'
                
        while lastkey == 'Up': #Same as the last while loop for Left
            time.sleep(0.1)
            new_head = [snake[0][0], snake[0][1]]
            for i in snake:
                win.draw_rect(i[0], i[1], i[0]+b_len, i[1]+b_len, 'blue')
            win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
            win.draw_screen()
            new_head[1] -= movement
            snake.insert(0, new_head)
            lastkey = win.get_last_key()

            if new_head in snake[2:] \
           or 319 < new_head[0]+b_len or new_head[0] < -19 \
           or 319 < new_head[1]+b_len or new_head[1] < -1:
                end_screen(score)
                break
            ## This is for if the snake head hits a food pellet
            if new_head[0] == food[0] and new_head[1] == food[1]:
                food = None
                score += 1 #add one to the score
                while food is None:
                    x_val_food = random.choice(viable_food_nums) #This assigns the food to a new square
                    newfood = [
                        x_val_food[0],
                        x_val_food[1]
                    ]
                    food = newfood if newfood not in snake else None #make sure food doesnt spaw inside snake

    ## This draws the actual food pellet and draws a snake block to increase the length of the snake
                win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
                win.draw_rect(snake[1][0], snake[1][1], snake[1][0]+b_len, snake[1][1]+b_len, 'blue')
            else:
                tail = snake.pop()
            if lastkey == None:
                lastkey = 'Up'
                
        while lastkey == 'Right': #Same as the last while loop for up
            time.sleep(0.1)
            new_head = [snake[0][0], snake[0][1]]
            for i in snake:
                win.draw_rect(i[0], i[1], i[0]+b_len, i[1]+b_len, 'blue')
            win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
            win.draw_screen()
            new_head[0] += movement
            snake.insert(0, new_head)
            lastkey = win.get_last_key()

            if new_head in snake[2:] \
           or 319 < new_head[0]+b_len or new_head[0] < -19 \
           or 319 < new_head[1]+b_len or new_head[1] < -1:
                end_screen(score)
                break

            ## This is for if the snake head hits a food pellet
            if new_head[0] == food[0] and new_head[1] == food[1]:
                food = None
                score += 1 #add one to the score
                while food is None:
                    x_val_food = random.choice(viable_food_nums) #This assigns the food to a new square
                    newfood = [
                        x_val_food[0],
                        x_val_food[1]
                    ]
                    food = newfood if newfood not in snake else None #make sure food doesnt spaw inside snake

    ## This draws the actual food pellet and draws a snake block to increase the length of the snake
                win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
                win.draw_rect(snake[1][0], snake[1][1], snake[1][0]+b_len, snake[1][1]+b_len, 'blue')
            else:
                tail = snake.pop()
            if lastkey == None:
                lastkey = 'Right'
                
        while lastkey == 'Down': #Same as the last while loop for down
            time.sleep(0.1)
            new_head = [snake[0][0], snake[0][1]]
            for i in snake:
                win.draw_rect(i[0], i[1], i[0]+b_len, i[1]+b_len, 'blue')
            win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
            win.draw_screen()
            new_head[1] += movement
            snake.insert(0, new_head)
            lastkey = win.get_last_key()

            if new_head in snake[2:] \
           or 319 < new_head[0]+b_len or new_head[0] < -19 \
           or 300 < new_head[1]+b_len or new_head[1] < -1:
                end_screen(score)
                break

            ## This is for if the snake head hits a food pellet
            if new_head[0] == food[0] and new_head[1] == food[1]:
                food = None
                score += 1 #add one to the score
                while food is None:
                    x_val_food = random.choice(viable_food_nums) #This assigns the food to a new square
                    newfood = [
                        x_val_food[0],
                        x_val_food[1]
                    ]
                    food = newfood if newfood not in snake else None #make sure food doesnt spaw inside snake

    ## This draws the actual food pellet and draws a snake block to increase the length of the snake
                win.draw_rect(food[0], food[1], food[0]+b_len, food[1]+b_len, 'red')
                win.draw_rect(snake[1][0], snake[1][1], snake[1][0]+b_len, snake[1][1]+b_len, 'blue')
            else:
                tail = snake.pop() #gets rid of the block that the snake was just on
            if lastkey == None:
                lastkey = 'Down'

## Create a global variable that makes the window for the game
win = gfx.Window(300, 300, 'CS101 block')
## Call the main_game function to start the game
try:  #tries this function and if the user closes the window then it gives an error
    main_game()    
except Exception as e:
    print('Error: %s. Restart program to replay' %e)
    








            
