# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.



'''RULES'''
'''
1.IN THIS WE DEFINE 11 PLAYERS FIRST
2.THEY FLIP A BOOK PAGE WHERE THE RUNS ARE ADDED BASED UPON THE LAST DIGIT OF THE PAGE;S PAGE N0
3.CONSIDERING THE BOOK PAGE NO TO BE OF 1000 PAGES
4.IF 0 COMES WE CONSIDER IT OUT
5.ELSE WE ADD THE SCORE TO PLAYER
6.IF OUT NEXT PLAYER COMES IN
'''
import random
class Player(object):
    
    def __init__(self,name):
        
        self.name=name
        self.runs=0
        self.balls=10
        
    ''' add runs'''
    def add_runs(self,runs):
        self.runs+=runs
    ''' add balls'''
    def add_balls(self,balls):
        self.balls+=balls
        
    

Rohit = Player('Rohit')
Dhawan = Player('Dhawan')
Virat = Player('Virat')
Dhoni = Player('Dhoni')
Sharma = Player('Sharma')
Pathan = Player('Pathan')
Suraj = Player('Suraj')
Patil = Player('Patil')
Chahal = Player('Chahal')
Narine = Player('Narine')
kurunian = Player('kurunian')
 
Batsmen = (Rohit, Dhawan, Virat, Dhoni, Sharma, Pathan, Suraj, Patil, Chahal,Narine, kurunian)

def book_flip():
    '''RANDOM VALUE GENERATED AS THE DEPICTING THE BOOK PAGE NO IN BOOK CRICKET'''
    rand_value=random.randint(0,1000)
    value=rand_value%10
    results=(0,1,2,3,4,5,6,7,8,9)
    return results[value]

def flipping():
    page=book_flip()
    ''' IF ZERO ITS OUT ELSE RETURN THE SCORE'''
    if page!=0:
        
        return page
    else:
        print("He is Out")
        return page

def scorecard(total_team_score, total_balls):
    '''ScoreCard'''
    print ('%-10s %-10s %-10s' % ('Player ','Runs', 'Balls'))
    print()
    for i in range(0,11):
        print ('%-10s %-10s %-7d ' % (Batsmen[i].name,Batsmen[i].runs, Batsmen[i].balls))
    print()
    print ('%-10s %-10d %-7d' % ('Total', total_team_score, total_balls))    

def main():
    player_number=0
    total_team_score=0
    total_balls=0
    
    '''FOR LOOP FOR ALL THE PLAYER BATTING IS NOT FINISHED'''
    while(player_number<10):
        
        ball=flipping()
        '''ADDING THE BALL IN TOTAL BALLS'''
        total_balls+=1
        Batsmen[player_number].add_balls(1)
        
        if (ball):
            '''here runs are added according to the last digit of the page no'''
            Batsmen[player_number].add_runs(ball)
            total_team_score+=ball
        else:
            '''here a plyer has been out since page no value has last digit 0'''
            player_number+=1
        print (Batsmen[player_number].name + ' now has %s' %Batsmen[player_number].runs+' runs')
        
            
    print()
    print("SCOREBOARD")
    scorecard(total_team_score, total_balls)       
            

main()








    
    
