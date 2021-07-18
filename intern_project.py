import random
 
class Player(object):
    '''The team members!'''
    def __init__(self, name):
        self.name = name
        self.runs = 0
        self.balls = 0
        self.fours = 0
        self.sixes = 0
        self.dismissal = ''
        
    def add_runs(self, runs):
        self.runs += runs
 
    def add_balls(self, balls):
        self.balls += balls
 
    def add_fours(self, fours):
        self.fours += fours
 
    def add_sixes(self, sixes):
        self.sixes += sixes
        
    def add_dismissal(self, dismissal):
        self.dismissal = dismissal
 
'''The players'''
Cook = Player('Cook')
Prior = Player('Prior')
Pietersen = Player('Pietersen')
Bell = Player('Bell')
Trott = Player('Trott')
Compton = Player('Compton')
Swann = Player('Swann')
Patel = Player('Patel')
Broad = Player('Broad')
Anderson = Player('Anderson')
Panesar = Player('Panesar')
 
Batters = (Cook, Prior, Pietersen, Bell, Trott, Compton, Swann, Patel, Broad, Anderson, Panesar)
 
def first_dice():
    '''Simulates the rolling of the first die
    Returns runs scored or Owzthat appeal'''
    rand_value = random.randint(0,5)
    results = (1, 2, 3, 4, 6, 'Owzthat!')
    return results[rand_value]
 
def second_dice():
    '''Simulates the second 'appeal' die
    Returns the result of the appeal'''
    rand_value = random.randint(0,5)
    results = ('Bowled!', 'Caught!', 'Not Out!', 'Stumped!', 'L.B.W!', 'No Ball!')
    return results[rand_value]
 
def bowl():
    '''Simulates a single bowl
    Either returns the runs scored or the result of the appeal'''
    ball = first_dice()
    if  ball != 'Owzthat!':
        print ('Nice hit! Thats %s runs.' % ball)
        return ball
    else:
        print ('Owzthat! It\'s going to appeal!')
        appeal = second_dice()
        print ('The decision is...%s' % appeal)
        return appeal
 
def scorecard(extras, total_team_score, total_balls):
    '''Produces a standardised scorecard'''
    print ('%-20s %-7s %-7s %-7s %-7s' % (' ', 'Runs', 'Balls', 'Fours', 'Sixes'))
    for i in range(0,11):
        print ('%-10s %-10s %-7d %-7d %-7d %-7d' % (Batters[i].name, Batters[i].dismissal,
                                               Batters[i].runs, Batters[i].balls,
                                               Batters[i].fours, Batters[i].sixes))
    print ('%-21s %-7d' % ('Extras', extras))
    print ('%-21s %-7d %-7d' % ('Total', total_team_score, total_balls))
    
def main():
    player_number = 0 # initializes player index
    total_team_score = 0 # stores total runs scored
    total_balls = 0 # stores total number of balls bowled
    extras = 0 # stores total extras scored as a result of 'no balls'
    while player_number < 10:
        ball = bowl()
        total_balls += 1 # adds one to to the number of balls bowled in match
        Batters[player_number].add_balls(1) # adds one to the number of balls bowled to batter
        if ball in ['Bowled!', 'Caught!', 'Stumped!', 'L.B.W!']: # if batter is out
            print (Batters[player_number].name + ' scores %s' %Batters[player_number].runs)
            print ('England are now %s for %s' %(total_team_score, player_number + 1))
            Batters[player_number].add_dismissal(ball) # adds the type of dismissal to the batter
            player_number += 1 # moves to next batter
        elif ball == 'No Ball!': # if a no ball is bowled
            extras += 1 # add one to the extras
            total_team_score += 1 # add one to the total runs score
        elif ball == 'Not Out!': # if it's not out
            pass # don't do anything
        else: # if runs are scored
            Batters[player_number].add_runs(ball) # add runs to batters total score
            total_team_score += ball # add runs to total runs scored
            if ball == 4: # if a four is scored
                Batters[player_number].add_fours(1) # add one to the number of fours scored by batter
            elif ball == 6: # if a six is scored
                Batters[player_number].add_sixes(1) # add one to the number of sixes scored by batter
        print (Batters[player_number].name + ' now has %s' %Batters[player_number].runs)
    scorecard(extras, total_team_score, total_balls) # print out scorecard at end of game
    
main()
