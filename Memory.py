# add game state logic here
import simplegui
import random
deck = []
exposed = []
flipped = False # a flag to make sure that the clicked card is not previously face up
state = 0 ; #the initial
count = 0
face_up = [-1 , -1 ]
match = False
# helper function to initialize globals
def new_game():
    global deck , exposed , state , count
    count = 0
    state = 0
    list_a = range(0 , 8)
    list_b = range(0 , 8)
    deck = list_a + list_b
    random.shuffle(deck)
    label.set_text("Turns = " + str(count))
    exposed = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 , 0 , 0 , 0 ,0 , 0 , 0 , 0]
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed , state , count , match
    #get the index of the clicked card
    index = pos[0]  / 50
    
    if exposed[index] == 0:
        exposed[index] = 1
        flipped = True
    else:
        return
    if state == 0:
        state = 1
        face_up[0] = index
    elif state == 1:
        count = count + 1
        label.set_text("Turns = " + str(count))
        state = 2 #now check if both cards matches
        face_up[1] = index
        if deck[face_up[0]] != deck[face_up[1]]:#index us  for the recently opened card
            match = False
        else:
            match = True;
            #keep them exposed
    else:
        state = 1
        if not match:#face the old ones down
            exposed[face_up[0]] = 0
            exposed[face_up[1]] = 0
            face_up[1] = -1
        face_up[0] = index        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    counter = 0
    for card in deck:
        pt1 = [counter * 50 , 0] # the upper left corner
        pt2 = [ 50 + counter * 50, 0] # the upper right corner
        pt3 =  [50 + counter * 50 , 100] #the lower right
        pt4 = [counter * 50 , 100 ]#the lower left
        
        if counter < 16 and exposed[counter] == 0:
            canvas.draw_polygon([pt1 , pt2 , pt3 , pt4 ], 1 , "Green" , "Green" )
            #print pt1 , pt2 , pt3 , pt4 , counter
        else:
           canvas.draw_text(str(card) , [(counter * 50)+ 10 , 80 ] , 50 , "Blue")
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
label = frame.add_label("Turns = " + str(count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
#frame.set_canvas_background("Green")
# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric