'''
Created on Oct 22, 2015

@author: Jared
'''
from copy import copy, deepcopy
import random
from random import randint
class AI_Intermediate(object):
    '''
    classdocs
    '''

    def __init__(self):
        self.first_hit = []
        self.attempt = 1
        self.distance = 0
        self.sinking_ship = False
        self.ship_names = { 'P' : 'Patrol Boat',
                   'D' : 'Destroyer',
                   'S' : 'Submarine',
                   'B' : 'Battleship',
                   'A' : 'Aircraft Carrier'
                  }
        self.ships_bool = {'P' : True, # Patrol Boat
             'D' : True, # Destroyer
             'S' : True, # Submarine
             'B' : True, # Battleship
             'A' : True  # Aircraft Carrier
             }
        self.ships_remaining = {'P' : 2, # Patrol Boat
             'D' : 3, # Destroyer
             'S' : 3, # Submarine
             'B' : 4, # Battleship
             'A' : 5  # Aircraft Carrier
             }

    def read_stats(self):
        # setup our array
        spaces = []
        row_num = 0
        for i in range(0,10):
            spaces.append([])
            
            
        # loop through the file to get the stats       
        with open('stats') as openfileobject:
            for line in openfileobject:
                spaces[row_num] = line.replace("\n", "").split(',')
                row_num += 1
                
        for i in range(len(spaces)):
            for j in range(len(spaces)):
                spaces[i][j] = str(int(spaces[i][j]) + randint(0,9))
                
        return spaces 
    
    def is_not_out_of_bounds(self, point, user_board):
        if point[0] > len(user_board.spaces) - 1:
            return False
        elif point[0] < 0:
            return False
        elif point[1] > len(user_board.spaces[len(user_board.spaces) - 1]) - 1:
            return False
        elif point[1] < 0:
            return False
        else:
            return True
    
    def find_open_space(self, user_board, point):
        open = True
        #count starting space so start at 1
        open_vert = 1
        open_hori = 1
        
        
        i = 1
        # check right
        while open:
            if self.is_not_out_of_bounds([point[0],point[1] + i], user_board):
                if user_board.spaces[point[0]][point[1] + i] != 'O' and user_board.spaces[point[0]][point[1] + i] != '*':
                    open_hori +=1
                    i += 1
                else:        
                    open = False
            else:
                open = False
        i = 1
        open = True
        #check left
        while open:  
            if self.is_not_out_of_bounds([point[0],point[1] - i], user_board):      
                if user_board.spaces[point[0]][point[1] - i] != 'O' and user_board.spaces[point[0]][point[1] - i] != '*':
                    open_hori += 1
                    i += 1
                else:
                    open = False
            else:
                open = False
        i = 1
        open = True
        # find spaces verticle
        # check down
        while open:
            if self.is_not_out_of_bounds([point[0] + i,point[1]], user_board):
                if user_board.spaces[point[0] + i][point[1]] != 'O' and user_board.spaces[point[0] + i][point[1]] != '*':
                    open_vert +=1
                    i += 1
                else:        
                    open = False
            else:
                open = False
        i = 1
        open = True         
        # check up       
        while open:
            if self.is_not_out_of_bounds([point[0] - i,point[1]], user_board):
                if user_board.spaces[point[0] - i][point[1]] != 'O' and user_board.spaces[point[0] - i][point[1]] != '*':
                    open_vert +=1
                    i += 1
                else:        
                    open = False 
            else:
                open = False
                
        return [open_vert, open_hori]
    def find_ship_location(self,size,stats):
        lowest_num = 99
        # array of points (x,y)
        best_loc = []
        for i in range(0,size):
            best_loc.append([0,0])  
        
        # loop through each row
        for i in range(0,10):
            # loop through each col
            for j in range(0,10):
                if i > size - 2:
                    total = 0
                    
                    # add up all the spaces
                    for k in range(0,size):
                        total += int(stats[i - k][j])
                    
                    # check row
                    if total < lowest_num:
                        lowest_num = total
                        for k in range(0,size):
                            best_loc[k][0] = i - k
                            best_loc[k][1] = j
                        
                if j > size - 2:
                    total = 0
                    
                    # add up all the spaces
                    for k in range(0,size):
                        total += int(stats[i][j - k])
                    
                    # check col
                    if total < lowest_num:
                        lowest_num = total
                        for k in range(0,size):
                            best_loc[k][0] = i 
                            best_loc[k][1] = j - k                   
        
        print "Best location found for a size " + str(size) + " ship at coordinates: "    
        print best_loc
        print "Total time area has been shot:"
        print str(lowest_num)
        return best_loc 
    
    def place_ship(self, points, board, stats, size, key):  
               
        for i in range(0,len(points)):
            board.spaces[points[i][0]][points[i][1]] = key
            stats[points[i][0]][points[i][1]] = '999' 
  
    
    def place_ships(self, board, ships):
        # grab the stats board
        stats = self.read_stats() 
        
        # randomize the keys to randomize the ships a bit
        keys = ships.keys()
        random.shuffle(keys)       
        for key in keys:
            # find a place for the ship
            points = self.find_ship_location(ships[key], stats);       
            self.place_ship(points, board, stats, ships[key], key)
            
    def which_ships_are_sunk(self, ships, user_board):
        # get rid of all ships found on board
        for i in range(len(user_board.spaces)):
            for j in range(len(user_board.spaces)):
                for key in ships:
                    if user_board.spaces[i][j] == key:
                        ships[key] = False        
        
            
    def is_ship_possible(self, point, user_board):
        ''' 
        TODO: Have the AI check to see if the point could possibly have a ship.
        '''
        pass
        
    def get_direction(self):
        if self.attempt == 1 or self.attempt == 2:
            self.direction = 'vertical'
        else:
            self.direction = 'horizontal'  
    
    def is_ship_sunk(self, user_board, original_board):
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
                        user_board.spaces[i][j] = '*'
                        ship_is_sunk = True
                        key = k;
        
        if ship_is_sunk:
            print "We have sunk the enemy's " + self.ship_names[key]
            del self.ships_remaining[key]
            del self.ships_bool[key]
        
        return ship_is_sunk             
             
    def sink_ship(self): 
        self.distance += 1
            
        if self.attempt == 5:
            self.attempt = 1
        # down
        if self.attempt == 1:
            return [self.first_hit[0] + self.distance, self.first_hit[1]]
        # up
        elif self.attempt == 2:
            return [self.first_hit[0]  + (self.distance * -1),self.first_hit[1]] 
        # right
        elif self.attempt == 3:
            return [self.first_hit[0], self.first_hit[1] + self.distance]         
        # left
        elif self.attempt == 4:
            return [self.first_hit[0], self.first_hit[1] + (self.distance * -1)]         
    def take_turn(self, user_board, original_user_board):
        invalid_point = True
        while invalid_point:
            
            # if clu found a ship
            if self.sinking_ship:
                point = self.sink_ship() 
            # clu is seeking a ship                     
            else:
                point = [randint(0,9), randint(0,9)]
                self.is_ship_possible(point, user_board)
            
            # check if shot is in boundaries
            if point[0] >= 0 and point[0] <= 9 and point[1] >= 0 and point[1] <= 9 :
                if user_board.spaces[point[0]][point[1]] == 'x' and self.sinking_ship:
                    self.distance +=1
                
                # make sure this spot hasn't been chosen already
                if user_board.spaces[point[0]][point[1]] != 'O' and user_board.spaces[point[0]][point[1]] != 'X' and user_board.spaces[point[0]][point[1]] != '*':
                    invalid_point = False 
                elif self.sinking_ship:        
                    self.attempt += 1
                    self.distance = 0 
                    
            elif self.sinking_ship:        
                self.attempt += 1
                self.distance = 0 
                 
        if user_board.spaces[point[0]][point[1]] == ' ':
            user_board.spaces[point[0]][point[1]] = 'O'
            if self.sinking_ship:
                self.attempt += 1
                self.distance = 0
            
            print 'Sir, enemy has fired a miss!'
        else:
            user_board.spaces[point[0]][point[1]] = 'X'
            if not self.sinking_ship:
                self.first_hit = point
                # do a check to see which direction to start shooting the ship
                open_space = self.find_open_space(user_board, self.first_hit)
                
                # if there are more spaces horizontally open then start on attempt 3        
                if open_space[0] < open_space[1]:
                    self.attempt = 3
            if self.sinking_ship:
                self.get_direction()
            self.sinking_ship = True
            print 'Sir, we have been hit!'
            if self.is_ship_sunk(user_board, original_user_board):
                self.sinking_ship = False
                self.attempt = 1
                self.distance = 0 
                for i in range(len(user_board.spaces)):
                    for j in range(len(user_board.spaces)): 
                        if user_board.spaces[i][j] == 'X':
                            self.sinking_ship = True
                            self.first_hit = [i,j] 
          

        
        