'''
Created on Nov 10, 2015

@author: Jared
'''
from copy import copy, deepcopy
if __name__ == '__main__':
    
    file_num = 0
    while file_num != 3:        
        ship_stats = []
        row_num = 0
        for i in range(0,10):
            ship_stats.append([])
            
            
        # loop through the file to get the stats       
        with open('ship_stats' + str(file_num) + '.txt') as openfileobject:
            for line in openfileobject:
                ship_stats[row_num] = line.replace("\n", "").split(',')
                row_num += 1
        if file_num == 0:
            total = deepcopy(ship_stats)
        else:
            for i in range(0,10):
                for j in range(0,10):
                    total[i][j] = int(total[i][j]) + int(ship_stats[i][j])
        file_num += 1
        openfileobject.close()
        
    total_file = open('total','w')
    s = "";
    for i in range(len(total)):
        s = "";
        for j in range(len(total)):
            if j == 0:
                s += str(total[i][j])
            else:
                s += ',' + str(total[i][j])
            
        total_file.write(s +'\n')
    total_file.close()

                    