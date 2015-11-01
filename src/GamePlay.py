
from Board import Board
from AI import AI_Novice  
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
''' PLAYER VS CPU        
if __name__ == '__main__':

    ships = {'P' : 2, # Patrol Boat
             'D' : 3, # Destroyer
             'S' : 3, # Submarine
             'B' : 4, # Battleship
             'A' : 5  # Aircraft Carrier
             }
    # create the user_board
    user_board = Board(10,10)
    user_hit_board = Board(10,10)
    original_board = Board(10,10)
    # create the AI_board    
    clu_board = Board(10,10)
    
    # create AI
    clu = AI()
    # create user
    start = Start_Player()
    # place the ships
    clu.place_ships(clu_board, ships)
    clu.place_ships(user_board, ships)
    
    # get a saved state of original board
    original_board.spaces = deepcopy(user_board.spaces);
    # show clu board for debugging
    clu_board.display()   
    
    #start.place_ships(user_board, ships) 
    
    user = Player()
    
    no_winner = True
    # Let the Games BEGIN!
    while no_winner:
        user.take_turn(user_hit_board, clu_board)
        user_hit_board.display()
        print "Clu's turn..."
        time.sleep( 2 )
        clu.take_turn(user_board, original_board)
        user_board.display()
        time.sleep( 2 )
        user_hit_board.display()
'''
'''
Single Match    
if __name__ == '__main__':


    ships = {'P' : 2, # Patrol Boat
             'D' : 3, # Destroyer
             'S' : 3, # Submarine
             'B' : 4, # Battleship
             'A' : 5  # Aircraft Carrier
             }
    # create tron
    tron = AI()
    tron_board = Board(10,10)
    tron.place_ships(tron_board, ships)
    original_tron = Board(10,10)
    original_tron.spaces = deepcopy(tron_board.spaces);
    
    # create clu
    clu = AI()
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

'''
''' multiple cpu match'''
if __name__ == '__main__':
    games_played = 0
    tron_wins = 0
    clu_wins = 0
    while games_played < 10000:
        ships = {'P' : 2, # Patrol Boat
                 'D' : 3, # Destroyer
                 'S' : 3, # Submarine
                 'B' : 4, # Battleship
                 'A' : 5  # Aircraft Carrier
                 }
        # create tron
        tron = AI_Novice()
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
    