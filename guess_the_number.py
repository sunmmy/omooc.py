
import simplegui
import random
import math

game_range=100

def new_game():
    print "choose a number between 0-",game_range
    global secret_number
    secret_number = random.randrange(0, game_range)

def range100():
    
    global range100
    range100 = 1
    new_game()
    
    
def input_guess(guess):
    entered_number=int(guess)
    print "you have guessed",entered_number
    
    if entered_number>secret_number:
       print "Lower!"
    elif entered_number<secret_number:
        print "Higher!"
    else:
        print "Correct!"
        
# creat frame
frame=simplegui.create_frame("guess the number",200,200)

frame.add_input("Guess",input_guess,100)
button=frame.add_button("choose100",range100,100)

frame.start()

new_game

    