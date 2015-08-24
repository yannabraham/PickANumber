'''
Created on Feb 14, 2014

@author: abrahya1
'''

from random import randint

def pickANumber(turns=3,minNum=1,maxNum=10):
    score = [0,0]
    while turns>0:
        secretNumber = randint(minNum, maxNum)
        print 'Choisis un chiffre entre %i et %i\t' % (minNum, maxNum)
        myGuess = None
        while myGuess is None:
            myGuess = raw_input('??')
            if ( int(myGuess)<minNum ) | ( int(myGuess)>maxNum ):
                myGuess = None
        if int(myGuess)==secretNumber:
            print 'Gagne :-)'
            score[0]+=1
        else:
            print 'Perdu :-('
            score[1]+=1
        turns-=1
    print 'Score final apres %i tours\n' % sum(score)
    print 'Moi: %i\nVous: %i' % (score[1],score[0])
    return(None)

if __name__ == '__main__':
    pickANumber(5,1,10)