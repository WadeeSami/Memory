# implementation of card game - Memory

import simplegui
import random

deck = []
# helper function to initialize globals
def new_game():
    global deck
    list_a = range(0 , 8)
	list_b = range(0 , 8)
    deck = list_a + list_b
    random.shuffle(list_a , list_b)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pass# implementation of card game - Memory

import simplegui
import random

deck = []
# helper function to initialize globals
def new_game():
    global deck
    list_a = range(0 , 8)
    list_b = range(0 , 8)
    deck = list_a + list_b
    random.shuffle(deck)
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    counter = 0
    for card in deck:
        canvas.draw_text(str(card) , [(counter * 50)+ 10 , 80 ] , 40 , "White")
        counter = counter + 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric