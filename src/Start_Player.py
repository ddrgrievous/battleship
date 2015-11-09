'''
Created on Oct 26, 2015

@author: Jared
'''
class Start_Player(object):
    '''
    classdocs
    '''
    key = {'A' : 0,
           'B' : 1,
           'C' : 2,
           'D' : 3,
           'E' : 4,
           'F' : 5,
           'G' : 6,
           'H' : 7,
           'I' : 8,
           'J' : 9,               
               }
    
    ship_direction = "left"

    def __init__(self):
        '''
        Constructor
        '''
        self.ship_stats = []
        row_num = 0
        for i in range(0,10):
            self.ship_stats.append([])
            
            
        # loop through the file to get the stats       
        with open('ship_stats.txt') as openfileobject:
            for line in openfileobject:
                self.ship_stats[row_num] = line.replace("\n", "").split(',')
                row_num += 1
        
                
    def parse_input(self, input):
        point = []
        if(len(input) >= 3 or input[0].isdigit() or input[1].isalpha()):
            print "Invalid Input!"
            return

        point.append(self.key[input[0].upper()])
        point.append(int(input[1]))
        
        return point
    
    def find_ship_length(self, point1, point2):
        x = point1[0] - point2[0]
        y = point1[1] - point2[1]
        if y > 0:
            self.direction ="left"
        elif y < 0:
            self.direction = "right"
        elif x < 0:
            self.direction = "down"
        elif x > 0:
            self.direction = "up"
            
        x = abs(x)
        y = abs(y)
    
        if (x == 0):
            return y
        elif (y == 0):
            return x    
        else:
            print "invalid input"
            return 100
        
    def fill_in_ship(self, point1, point2, board, size, key):
        '''
        TODO I need this to only start inputing when we find out all points are good!
        do this by having an array of points and then assign the array to the size
        '''
        ship_points = []
        ship_points.append(point1)
        # if filling into the left
        if self.direction == "left":
            # start at end point
            i = point2[1]
            
            # so long as we have not reached the other side
            while point1[1] != point2[1]:
                if board.spaces[point2[0]][point2[1]] != ' ':
                    # stop if we find this is incorrect
                    return False
                # fill in with the ship size
                ship_points.append([point2[0],point2[1]])
                
                # increment
                i += 1
                # assign
                point2[1] = i
                
        # right        
        elif self.direction == "right":
            # start at end point
            i = point2[1]
            
            # so long as we have not reached the other side
            while point1[1] != point2[1]:
                if board.spaces[point2[0]][point2[1]] != ' ':
                    # stop if we find this is incorrect
                    return False
                
                # fill in with the ship size
                ship_points.append([point2[0],point2[1]])
                
                # decrement
                i -= 1                
                # assign
                point2[1] = i  
        
        # down              
        elif self.direction == "down":
            # start at end point
            i = point2[0]
            
            # so long as we have not reached the other side
            while point1[0] != point2[0]:
                if board.spaces[point2[0]][point2[1]] != ' ':
                    # stop if we find this is incorrect
                    return False
                
                # fill in with the ship size
                ship_points.append([point2[0],point2[1]])
                
                # decrement
                i -= 1                
                # assign
                point2[0] = i   
                
        # up                 
        elif self.direction == "up":
            
            # start at end point
            i = point2[0]
            
            # so long as we have not reached the other side
            while point1[0] != point2[0]:
                if board.spaces[point2[0]][point2[1]] != ' ':
                    # stop if we find this is incorrect
                    return False
                
                # fill in with the ship size
                ship_points.append([point2[0],point2[1]])
                
                # show board
                board.display()
                
                # increment
                i += 1
                
                # assign
                point2[0] = i 
        
        for i in range(len(ship_points)):
            board.spaces[ship_points[i][0]][ship_points[i][1]] = key  
               
        for i in range(len(ship_points)):
            self.ship_stats[ship_points[i][0]][ship_points[i][1]] = int(self.ship_stats[ship_points[i][0]][ship_points[i][1]]) + 1 
                  
        # all went well 
        return True  
    def place_ships(self, board, ships):
        
        print "Example coordinate format: 'A8'"
        for key in ships:
            invalid_ship = True
            
            while invalid_ship:
                board.display()
                point1 = []
                point2 = []
                # inputing will remain true until valid input is recieved
                inputing = True
                
                while inputing:
                    # get user input
                    input = raw_input("Start coordinate of your ship of size " + str(ships[key]) + ": ")
                    
                    # parse user input into a point
                    point1 = self.parse_input(input)
                    
                    # if point array has 2 values and the space doesn't have a ship already
                    if (len(point1) == 2) and (board.spaces[point1[0]][point1[1]] == ' '):                    
                        # end the looping            
                        inputing = False
                        
                        # put the ship size the board
                        board.spaces[point1[0]][point1[1]] = '*'
                    else:                  
                        # or reprompt
                        print "invalid point"
                    
    
                inputing = True           
                while inputing:
                    # show the board to the user with updated start spot
                    board.display()
                    
                    # get user input
                    input = raw_input("End coordinate of your ship of size "   + str(ships[key]) + ": ")
                    
                    # parse user input into point
                    point2= self.parse_input(input)
                    
                    # determine the size of the ship they have created
                    size = self.find_ship_length(point1,point2) + 1
                    
                    # if point array has 2 values and the space doesn't have a ship already
                    if len(point1) == 2 and size == ships[key]:
                        inputing = False
                        if self.fill_in_ship(point1, point2, board, ships[key], key):           
                            invalid_ship = False   
                        else:
                            board.spaces[point1[0]][point1[1]] = ' '  
                            print "overlapping ship"  
                    else:
                        print "invalid input size"  
        
        ship_stats_file = open('ship_stats.txt','w')
        s = "";
        for i in range(len(self.ship_stats)):
            s = "";
            for j in range(len(self.ship_stats)):
                if j == 0:
                    s += str(self.ship_stats[i][j])
                else:
                    s += ',' + str(self.ship_stats[i][j])
            
            ship_stats_file.write(s +'\n')
