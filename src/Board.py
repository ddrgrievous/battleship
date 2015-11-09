'''
Created on Oct 1, 2015

@author: Jared
'''
from sysconfig import sys
import string

class Board(object):
    
    def __init__(self, rows, cols):
        self.spaces = []
        # create board based on parameters
        for i in range(0,rows):
            self.spaces.append([])  
             
        for i in range(0, rows):
            for j in range(0, cols):
                self.spaces[i].append(' ')  
        #print self.spaces[0][0]         
        
    def display(self):
        print '\n '
        sys.stdout.write("  ")
        for i in range(0, len(self.spaces)):
            sys.stdout.write( " " + str(i))
        for y in range(0,len(self.spaces)):              
            for x in range(0, len(self.spaces[y])):
                if x == 0:
                    print "\n" + string.ascii_uppercase[y] + " |" + self.spaces[y][x] + "|",
                elif x == 9:
                    sys.stdout.write(self.spaces[y][x] + "| " + string.ascii_uppercase[y])
                else:                
                    sys.stdout.write(self.spaces[y][x] + "|")
        sys.stdout.write("\n  ")
        for i in range(0, len(self.spaces)):
            sys.stdout.write( " " + str(i))
        print '\n '
        