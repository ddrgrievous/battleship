'''
Created on Oct 27, 2015

@author: Jared
'''
from Start_Player import Start_Player
class Player(object):
    '''
    classdocs
    '''    
    def __init__(self):
        self.parser = Start_Player()
    
    def take_turn(self, user_hit_board, clu_board):
        input = raw_input("Coordinate of your shot: " );
        point = self.parser.parse_input(input)
        
        if clu_board.spaces[point[0]][point[1]] == ' ':
            user_hit_board.spaces[point[0]][point[1]] = 'O'
            print "Sir we have missed the enemy ship."
        else:
            user_hit_board.spaces[point[0]][point[1]] = 'X'
            clu_board.spaces[point[0]][point[1]]      = 'X'
            print "Sir we have hit the enemy ship!"
            