#Rice University - Introduction to interactive programming with python
#Memory - not with classes
#Produced in Codeskulptor and changed to use simpleguitk to implement 
#codeskultpors GUI components

import simpleguitk as simplegui
import random

turns = 0

# helper function to initialize globals
def new_game():
    global card_deck, exposed, position, state, card_one, card_two, turns
    card_deck = range(8) # eight cards in the range of 0-7
    card_deck *= 2 #take the list and make two of the same lists
    random.shuffle(card_deck) # shuffle the two lists together
    print card_deck
    exposed = [False]*len(card_deck) #make each exposed part of the card deck set to false
    state = 0
    turns = 0 # start the game in state zero and turns to 0, initialize the global variables
    label.set_text("Turns = " + str(turns))
    
# define event handlers
def mouseclick(pos):
    global card_deck, exposed, position, state , i, card_one, card_two, turns
    # add game state logic here
    position = list(pos)[0]//50 #each click/card has an x variable within the range of 50 pixels
    
    if exposed[position] == False: #if everything is false, start in state zero
        if state == 0:
            card_one = position #store the index of the card
            exposed[position] = True
            state = 1
        elif state == 1:
            card_two = position #store the index of the second card
            exposed[position] = True
            turns += 1
            label.set_text("Turns = " + str(turns))
            state = 2
        else:
            if card_deck[card_one] != card_deck[card_two]: #if card one and card two do not match
                exposed[card_one], exposed[card_two] = False, False #then they go back to flase
            card_one = position # set card_one back to position because will never go back to state 0
            exposed[position] = True #just like in state 0
            state = 1
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
        global card_deck, exposed, position, state, turns
        for i in range(len(card_deck)):
            if exposed[i]:
                canvas.draw_polygon(([i * 50, 0], [i * 50, 100],[(i+1) * 50 , 100] , [(i+1)*50, 0])
                                    , 2 , 'Fuchsia', 'Teal')
                canvas.draw_text(str(card_deck[i]), (i * 50 + 13, 70), 40, 'DeepPink')
            if not exposed[i]:
                canvas.draw_polygon(([i * 50, 0], [i * 50, 100],[(i+1) * 50 , 100] , [(i+1)*50, 0])
                                    , 2 , 'Fuchsia', 'Purple')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " + str(turns))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric