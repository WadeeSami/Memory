
    # add game state logic here
    
import simplegui
import random

deck = []
exposed = []
# helper function to initialize globals
def new_game():
    global deck , exposed
    list_a = range(0 , 8)
    list_b = range(0 , 8)
    deck = list_a + list_b
    random.shuffle(deck)
    exposed = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 ,0 , 0 , 0 , 0]
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    counter = 0
    for card in deck:
        pt1 = [counter * 50 , 0] # the upper left corner
        pt2 = [ 50 + counter * 50, 0] # the upper right corner
        pt3 =  [50 + counter * 50 , 100] #the lower right
        pt4 = [counter * 50 , 100 ]#the lower left
        
        if counter < 16 and exposed[counter] == 0:
            canvas.draw_polygon([pt1 , pt2 , pt3 , pt4 ], 1 , "Green" , "Blue" )
            #print pt1 , pt2 , pt3 , pt4 , counter
        else:
           canvas.draw_text(str(card) , [(counter * 50)+ 10 , 80 ] , 40 , "Blue")
        canvas.draw_line( pt1, [counter * 50 , 100] , 1 ,"black")
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
#frame.set_canvas_background("Green")
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric