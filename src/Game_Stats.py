'''
Created on Nov 20, 2015

@author: Jared
'''
class Game_Stats(object):
    '''
    classdocs
    '''

    def __init__(self):
        pass
    @staticmethod  
    def read_game_stats():
        game_file_items = {
        'GamesPlayed' : 0, 
        'rounds' : 0,
        'CompWins' : 0, 
        'UserWins' : 0, 
        }
        game_stats = [];
        
        # read file
        with open('data\game_stats') as game_stats_file:
            for line in game_stats_file:
                game_stats = line.replace("\n", "").split(',')
                
        # put the stats into the dictionary
        for i in range(0,len(game_stats)):
            if game_stats[i] == 'GamesPlayed':
                game_file_items['GamesPlayed'] = int(game_stats[i+1])
            elif game_stats[i] == 'rounds':
                game_file_items['rounds'] = int(game_stats[i+1])                       
            elif game_stats[i] == 'CompWins':
                game_file_items['CompWins'] = int(game_stats[i+1])
            elif game_stats[i] == 'UserWins':
                game_file_items['UserWins'] = int(game_stats[i+1])  
        
        game_stats_file.close()       
        return game_file_items        
    @staticmethod       
    def write_game_stats(games_played, rounds, comp_wins, user_wins):
        # read in current stats
        current_game_stats = Game_Stats.read_game_stats()
        
        # add the parameters
        current_game_stats['GamesPlayed'] += games_played
        current_game_stats['rounds'] += rounds
        current_game_stats['CompWins'] += comp_wins
        current_game_stats['UserWins'] += user_wins
        # overwrite file
        game_stats_file = open('data/game_stats','w')            
        game_stats_file.write('GamesPlayed,'+str(current_game_stats['GamesPlayed'])+
                              ',rounds,'+str(current_game_stats['rounds'])+
                              ',CompWins,'+str(current_game_stats['CompWins'])+
                              ',UserWins,'+str(current_game_stats['UserWins']))
        game_stats_file.close()                          