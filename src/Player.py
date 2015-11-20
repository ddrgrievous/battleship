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
        self.turn_count = 1;
        self.shot_map = []
        row_num = 0
        for i in range(0,10):
            self.shot_map.append([])
            
            
        # loop through the file to get the stats       
        with open('shot_map') as openfileobject:
            for line in openfileobject:
                self.shot_map[row_num] = line.replace("\n", "").split(',')
                row_num += 1
    
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
            
        self.update_shot_map(point, user_hit_board.spaces)
            
    def update_shot_map(self, shot_point, spaces):
        is_exploration = True
        for i in range(0,10):
            for j in range(0,10):
                if spaces[i][j].lower() == 'x':
                    is_exploration = False
        #determine the value to assign to the shot map       
        if not is_exploration:
            self.shot_map[shot_point[0]][shot_point[1]] = '1'
        elif self.turn_count <= 10:
            self.shot_map[shot_point[0]][shot_point[1]] = '3'
        elif self.turn_count <= 20:
            self.shot_map[shot_point[0]][shot_point[1]] = '2'
        else:
            self.shot_map[shot_point[0]][shot_point[1]] = '1'

        #increment turn count
        if is_exploration:
            self.turn_count += 1 
            
    def save_shot_map(self):  
        ship_map_file = open('shot_map','w')
        s = "";
        for i in range(len(self.shot_map)):
            s = "";
            for j in range(len(self.shot_map)):
                if j == 0:
                    s += str(self.shot_map[i][j])
                else:
                    s += ',' + str(self.shot_map[i][j])
            
            ship_map_file.write(s +'\n')
        ship_map_file.close()     
            
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
            