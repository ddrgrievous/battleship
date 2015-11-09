from Board import Board
from AI_Expert import AI_Expert
from AI_Intermediate import AI_Intermediate
from AI_Novice import AI_Novice  
from AI_Easy import AI_Easy   
from Start_Player import Start_Player
  
from Player import Player
from copy import copy, deepcopy
import time         
def is_win(ships):
    for k in ships:
        if not ships[k]:
            return False
    
    return True
         
    
def player_vs_computer(): 
    not_valid_input = True  
    while not_valid_input:
        level = raw_input("Easy, Medium or Hard? ")
         # create AI
        if level.lower() == 'easy':    
            clu = AI_Easy()
            not_valid_input = False
        elif level.lower() == 'medium':
            clu = AI_Intermediate()
            not_valid_input = False
        elif level.lower() == 'hard':
            clu = AI_Expert()
            not_valid_input = False
    
    
    ships = {'P' : 2, # Patrol Boat
             'D' : 3, # Destroyer
             'S' : 3, # Submarine
             'B' : 4, # Battleship
             'A' : 5  # Aircraft Carrier
             }
       
    # create the user_board
    user_board = Board(10,10)
    user_hit_board = Board(10,10)
    original_user_board = Board(10,10)
    
    # create user
    start = Start_Player()
    start.place_ships(user_board, ships) 
    original_user_board.spaces = deepcopy(user_board.spaces);    
    user = Player()
    
    # create the AI   
    clu_board = Board(10,10)
    clu.place_ships(clu_board, ships)
    original_clu_board = Board(10,10)
    original_clu_board.spaces = deepcopy(clu_board.spaces);    

    print " "
    
    user_hit_board.display()
    no_winner = True
    # Let the Games BEGIN!
    while no_winner:
        ''' USER MOVE'''
        user.take_turn(user_hit_board, clu_board, original_clu_board)
        user_hit_board.display()
        bool_ships = {'P' : True, # Patrol Boat
             'D' : True, # Destroyer
             'S' : True, # Submarine
             'B' : True, # Battleship
             'A' : True  # Aircraft Carrier
            }
        user.which_ships_are_sunk(bool_ships, clu_board)
        if is_win(bool_ships):
            print "Game over you win!"
            break
        
        ''' CLU's TURN '''
        print "Clu's turn..."
        time.sleep( 2 )       
        bool_ships = {'P' : True, # Patrol Boat
             'D' : True, # Destroyer
             'S' : True, # Submarine
             'B' : True, # Battleship
             'A' : True  # Aircraft Carrier
            }
        clu.take_turn(user_board, original_user_board)
        user_board.display()
        user_hit_board.display()
        clu.which_ships_are_sunk(bool_ships, user_board)
        if is_win(bool_ships):
            print "Game over clu wins!"
            break

''' One Game computer vs computer '''
def computers_vs_computer_one():

    ships = {'P' : 2, # Patrol Boat
             'D' : 3, # Destroyer
             'S' : 3, # Submarine
             'B' : 4, # Battleship
             'A' : 5  # Aircraft Carrier
             }
    # create tron
    tron = AI_Easy()
    tron_board = Board(10,10)
    tron.place_ships(tron_board, ships)
    original_tron = Board(10,10)
    original_tron.spaces = deepcopy(tron_board.spaces);
    
    # create clu
    clu = AI_Easy()
    clu_board = Board(10,10)
    clu.place_ships(clu_board, ships)
    original_clu = Board(10,10)
    original_clu.spaces = deepcopy(clu_board.spaces);
       
    no_winner = True
    # Let the Games BEGIN!
    while no_winner:
        
        bool_ships = {'P' : True, # Patrol Boat
             'D' : True, # Destroyer
             'S' : True, # Submarine
             'B' : True, # Battleship
             'A' : True  # Aircraft Carrier
            }
        # Tron's Turn
        print "tron's turn..."
        #time.sleep( 2 )
        tron.take_turn(clu_board, original_clu)
        #clu_board.display()
        tron.which_ships_are_sunk(bool_ships, clu_board)
        if is_win(bool_ships):
            print "game over tron wins"
            break
        
        bool_ships = {'P' : True, # Patrol Boat
             'D' : True, # Destroyer
             'S' : True, # Submarine
             'B' : True, # Battleship
             'A' : True  # Aircraft Carrier
            }
        # Clu's turn
        print "Clu's turn..."
        #time.sleep( 2 )
        clu.take_turn(tron_board, original_tron)
        #tron_board.display()
        clu.which_ships_are_sunk(bool_ships, tron_board)
        if is_win(bool_ships):
            print "game over clu wins"
            break


def computer_vs_computer_many():
    games_played = 0
    tron_wins = 0
    clu_wins = 0
    while games_played < 1000:
        ships = {'P' : 2, # Patrol Boat
                 'D' : 3, # Destroyer
                 'S' : 3, # Submarine
                 'B' : 4, # Battleship
                 'A' : 5  # Aircraft Carrier
                 }
        # create tron
        tron = AI_Expert()
        tron_board = Board(10,10)
        tron.place_ships(tron_board, ships)
        original_tron = Board(10,10)
        original_tron.spaces = deepcopy(tron_board.spaces);
        
        # create clu
        clu = AI_Intermediate()
        clu_board = Board(10,10)
        clu.place_ships(clu_board, ships)
        original_clu = Board(10,10)
        original_clu.spaces = deepcopy(clu_board.spaces);
           
        no_winner = True
        # Let the Games BEGIN!
        while no_winner:
            
            bool_ships = {'P' : True, # Patrol Boat
                 'D' : True, # Destroyer
                 'S' : True, # Submarine
                 'B' : True, # Battleship
                 'A' : True  # Aircraft Carrier
                }
            # Tron's Turn
            print "tron's turn..."
            #time.sleep( 2 )
            tron.take_turn(clu_board, original_clu)
            #clu_board.display()
            tron.which_ships_are_sunk(bool_ships, clu_board)
            if is_win(bool_ships):
                print "game over tron wins"
                tron_wins += 1
                break
            
            bool_ships = {'P' : True, # Patrol Boat
                 'D' : True, # Destroyer
                 'S' : True, # Submarine
                 'B' : True, # Battleship
                 'A' : True  # Aircraft Carrier
                }
            # Clu's turn
            print "Clu's turn..."
            #time.sleep( 2 )
            clu.take_turn(tron_board, original_tron)
            #tron_board.display()
            clu.which_ships_are_sunk(bool_ships, tron_board)
            if is_win(bool_ships):
                print "game over clu wins"
                clu_wins += 1
                break
        games_played = tron_wins + clu_wins
    
    print 'Tron ' + str(tron_wins)
    print 'Clu ' + str(clu_wins)
    
if __name__ == '__main__':
    print "**********************"
    print "Welcome to Battleship!"
    print "**********************"
    #player_vs_computer()
    computer_vs_computer_many()  
    # computers_vs_computer_one() 