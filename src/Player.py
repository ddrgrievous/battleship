'''
Created on Oct 27, 2015

@author: Jared
'''
from Start_Player import Start_Player
from copy import copy, deepcopy
class Player(object):
    '''
    classdocs
    '''    
    def __init__(self):
        self.parser = Start_Player()
        self.ships_bool = {
            'P' : True, # Patrol Boat
            'D' : True, # Destroyer
            'S' : True, # Submarine
            'B' : True, # Battleship
            'A' : True  # Aircraft Carrier
            }
        self.ship_names = { 
            'P' : 'Patrol Boat',
            'D' : 'Destroyer',
            'S' : 'Submarine',
            'B' : 'Battleship',
            'A' : 'Aircraft Carrier'
            }
        
        self.ships_remaining = {
            'P' : 2, # Patrol Boat
            'D' : 3, # Destroyer
            'S' : 3, # Submarine
            'B' : 4, # Battleship
            'A' : 5  # Aircraft Carrier
            }
    
    def take_turn(self, user_hit_board, clu_board, original_clu_board):
        input = raw_input("Coordinate of your shot: " );
        point = self.parser.parse_input(input, user_hit_board)
        
        if clu_board.spaces[point[0]][point[1]] == ' ':
            user_hit_board.spaces[point[0]][point[1]] = 'O'
            print "Sir we have missed the enemy ship."
        else:
            user_hit_board.spaces[point[0]][point[1]] = 'X'
            clu_board.spaces[point[0]][point[1]]      = 'X'
            print "Sir we have hit the enemy ship!"
            self.is_ship_sunk(clu_board, original_clu_board, user_hit_board)
            
    def is_ship_sunk(self, user_board, original_board, user_hit_board):
        key = ''
        ship_is_sunk = False
        ships = deepcopy(self.ships_bool);
        
        
        # get rid of all ships found on board
        self.which_ships_are_sunk(ships, user_board)

        print ships                
        # make the ship turn into *
        for i in range(len(user_board.spaces)):
            for j in range(len(user_board.spaces)):
                for k in ships:
                    if k == original_board.spaces[i][j] and ships[k]:
                        user_hit_board.spaces[i][j] = '*'
                        ship_is_sunk = True
                        key = k;
        
        if ship_is_sunk:
            print "We have sunk the enemy's " + self.ship_names[key]
            del self.ships_remaining[key]
            del self.ships_bool[key]
        
        return ship_is_sunk 
    
    def which_ships_are_sunk(self, ships, user_board):
        # get rid of all ships found on board
        for i in range(len(user_board.spaces)):
            for j in range(len(user_board.spaces)):
                for key in ships:
                    if user_board.spaces[i][j] == key:
                        ships[key] = False           
            