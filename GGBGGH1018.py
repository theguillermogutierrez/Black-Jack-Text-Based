##Code completely written by Guillermo Gutierrez
##Text based Black Jack game with multiplayer and betting support.
##This is a Bet version as I was writing this as a refresher, and did not use outside resources. As such, there are too many lines of code and now it is too complicated to fix the bugs that have cropped up. I will finish and public this game once I start accessing outisde resources.


## Imports random module, and creates the deck and its values.
from numpy import random
cards = ['ACE',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
values = [111,2,3,4,5,6,7,8,9,10,10,10,10]
suits = ['Clubs','Diamonds','Spades','Hearts']

## Player counting and hand creation.
r = 1
c = []
v = []
x = int(input('\nHello to all who have joined us tonight at Python Casino & Resort. The Dealer is a little hard of hearing, so please refrain from full sentences.\nThe table is currently hosting Blackjack, using 8 decks of cards and playing with 4.\n\nHow many players will be joining our next hand? '))
while x >= 7:
    print('\nUnfortunately, the table only sits 6. However we do not have a limit on bet behinds.')
    x = int(input('Have we decided how many should play first at this time? '))
print('Please place your main bets, the minimum bet at this table is $1.')
mainBets = []
mainBets1 = int(input('Player 1, What would you like to bet? '))
mainBets.append(mainBets1)
if x == 2:
    mainBets2 = int(input('Player 2, What would you like to bet? '))
    mainBets.append(mainBets2)
if x == 3:
    mainBets2 = int(input('Player 2, What would you like to bet? '))
    mainBets.append(mainBets2)
    mainBets3 = int(input('Player 3, What would you like to bet? '))
    mainBets.append(mainBets3)
if x == 4:
    mainBets2 = int(input('Player 2, What would you like to bet? '))
    mainBets.append(mainBets2)
    mainBets3 = int(input('Player 3, What would you like to bet? '))
    mainBets.append(mainBets3)
    mainBets4 = int(input('Player 4, What would you like to bet? '))
    mainBets.append(mainBets4)
if x == 5:
    mainBets2 = int(input('Player 2, What would you like to bet? '))
    mainBets.append(mainBets2)
    mainBets3 = int(input('Player 3, What would you like to bet? '))
    mainBets.append(mainBets3)
    mainBets4 = int(input('Player 4, What would you like to bet? '))
    mainBets.append(mainBets4)
    mainBets5 = int(input('Player 5, What would you like to bet? '))
    mainBets.append(mainBets5)
if x == 6:
    mainBets2 = int(input('Player 2, What would you like to bet? '))
    mainBets.append(mainBets2)
    mainBets3 = int(input('Player 3, What would you like to bet? '))
    mainBets.append(mainBets3)
    mainBets4 = int(input('Player 4, What would you like to bet? '))
    mainBets.append(mainBets4)
    mainBets5 = int(input('Player 5, What would you like to bet? '))
    mainBets.append(mainBets5)
    mainBets6 = int(input('Player 6, What would you like to bet? '))
    mainBets.append(mainBets6)

sideBets = []
print('Please place your side bets, the minimum bet at this table is $1. Tonight we have a special promotion that gives both perfect pair and 21 + 3 for side bet placements.')
sideBets1 = int(input('Player 1, What would you like to bet? '))
sideBets.append(sideBets1)

if x == 2:
    sideBets2 = int(input('Player 2, What would you like to bet? '))
    sideBets.append(sideBets2)
if x == 3:
    sideBets2 = int(input('Player 2, What would you like to bet? '))
    sideBets.append(sideBets2)
    sideBets3 = int(input('Player 3, What would you like to bet? '))
    sideBets.append(sideBets3)
if x == 4:
    sideBets2 = int(input('Player 2, What would you like to bet? '))
    sideBets.append(sideBets2)
    sideBets3 = int(input('Player 3, What would you like to bet? '))
    sideBets.append(sideBets3)
    sideBets4 = int(input('Player 4, What would you like to bet? '))
    sideBets.append(sideBets4)
if x == 5:
    sideBets2 = int(input('Player 2, What would you like to bet? '))
    sideBets.append(sideBets2)
    sideBets3 = int(input('Player 3, What would you like to bet? '))
    sideBets.append(sideBets3)
    sideBets4 = int(input('Player 4, What would you like to bet? '))
    sideBets.append(sideBets4)
    sideBets5 = int(input('Player 5, What would you like to bet? '))
    sideBets.append(sideBets5)
if x == 6:
    sideBets2 = int(input('Player 2, What would you like to bet? '))
    sideBets.append(sideBets2)
    sideBets3 = int(input('Player 3, What would you like to bet? '))
    sideBets.append(sideBets3)
    sideBets4 = int(input('Player 4, What would you like to bet? '))
    sideBets.append(sideBets4)
    sideBets5 = int(input('Player 5, What would you like to bet? '))
    sideBets.append(sideBets5)
    sideBets6 = int(input('Player 6, What would you like to bet? '))
    sideBets.append(sideBets6)
#### Figure out how to accept both a str and an int for sidebets
while r <= 2*(int(x)+1):
    p = random.randint(0,12)
    c.append(cards[p])
    v.append(values[p])
    r += 1
## Now figure out how to dynamically assign hands to players and then to the dealer.
dealerIC = c[(2*int(x)):(2*int(x)+2)]
dSuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
player1IC = c[0:2]
p1SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
if x == 2:
    player2IC = c[2:4]
    p2SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
if x == 3:
    player2IC = c[2:4]
    p2SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player3IC = c[4:6]
    p3SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
if x == 4:
    player2IC = c[2:4]
    p2SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player3IC = c[4:6]
    p3SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player4IC = c[6:8]
    p4SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
if x == 5:
    player2IC = c[2:4]
    p2SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player3IC = c[4:6]
    p3SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player4IC = c[6:8]
    p4SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player5IC = c[8:10]
    p5SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
if x == 6:
    player2IC = c[2:4]
    p2SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player3IC = c[4:6]
    p3SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player4IC = c[6:8]
    p4SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player5IC = c[8:10]
    p5SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]
    player6IC = c[10:12]
    p6SuitsIC = [suits[random.randint(0,3)],suits[random.randint(0,3)]]


print('Player One has pulled a ' + str(player1IC[0]) + ' of ' + p1SuitsIC[0] + '. ')
if x == 2:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
if x == 3:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
if x == 4:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
if x == 5:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
    print('Player Five has pulled a ' + str(player5IC[0]) + ' of ' + p5SuitsIC[0] + '. ')
if x == 6:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
    print('Player Five has pulled a ' + str(player5IC[0]) + ' of ' + p5SuitsIC[0] + '. ')
    print('Player Six has pulled a ' + str(player6IC[0]) + ' of ' + p6SuitsIC[0] + '. ')
print('The dealer shows an open ' + str(dealerIC[0]) + ' of ' + dSuitsIC[0] + '. ')
print('Player One has pulled a ' + str(player1IC[1]) + ' of ' + p1SuitsIC[1] + '. ')
if x == 2:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
if x == 3:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
if x == 4:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
if x == 5:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
    print('Player Five has pulled a ' + str(player5IC[0]) + ' of ' + p5SuitsIC[0] + '. ')
if x == 6:
    print('Player Two has pulled a ' + str(player2IC[0]) + ' of ' + p2SuitsIC[0] + '. ')
    print('Player Three has pulled a ' + str(player3IC[0]) + ' of ' + p3SuitsIC[0] + '. ')
    print('Player Four has pulled a ' + str(player4IC[0]) + ' of ' + p4SuitsIC[0] + '. ')
    print('Player Five has pulled a ' + str(player5IC[0]) + ' of ' + p5SuitsIC[0] + '. ')
    print('Player Six has pulled a ' + str(player6IC[0]) + ' of ' + p6SuitsIC[0] + '. ')

## Figure out how to get input from player for all three decisions

decision = str(input('Player 1, what would you like to do with ' + str(player1IC[0]) + ' and ' + str(player1IC[1]) + '? '))
while decision not in ('stand', 'hit', 'double down'):
    decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
def hit(decision):
    if decision == 'hit':
        player1Hand = player1IC
        p = random.randint(0,12)
        player1Hand.append(cards[p])
        print(player1Hand)
        if player1Hand[0] + player1Hand[1] + player1Hand[2] > 21:
            print('Too many')
            p1Win = False
        elif player1Hand[0] + player1Hand[1] + player1Hand[2] == 21:
            print('Good job. 21.')
            pass
        else:
            decision = str(input('Player 1, what would you like to do with ' + str(player1IC[0]), str(player1IC[1]) + ' and ' + str(player1IC[2]) + '? '))
    else:
        pass
def stand(decision):
    if decision == 'stand':
        pass
    else:
        pass
def doubleD(decision):
    if decision == 'double down':
        player1Hand = player1IC
        p = random.randint(0,12)
        player1Hand.append(cards[p])
        print(player1Hand)
    else:
        pass
hit(decision)
stand(decision)
doubleD(decision)
if x == 2:
    decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]) + ' and ' + str(player2IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
            if player2Hand[0] + player2Hand[1] + player2Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player2Hand[0] + player2Hand[1] + player2Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]), str(player2IC[1]) + ' and ' + str(player2IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
if x == 3:
    decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]) + ' and ' + str(player2IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
            if player2Hand[0] + player2Hand[1] + player2Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player2Hand[0] + player2Hand[1] + player2Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]), str(player2IC[1]) + ' and ' + str(player2IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]) + ' and ' + str(player3IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
            if player3Hand[0] + player3Hand[1] + player3Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player3Hand[0] + player3Hand[1] + player3Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]), str(player3IC[1]) + ' and ' + str(player3IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
if x == 4:
    decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]) + ' and ' + str(player2IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
            if player2Hand[0] + player2Hand[1] + player2Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player2Hand[0] + player2Hand[1] + player2Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]), str(player2IC[1]) + ' and ' + str(player2IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]) + ' and ' + str(player3IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
            if player3Hand[0] + player3Hand[1] + player3Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player3Hand[0] + player3Hand[1] + player3Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]), str(player3IC[1]) + ' and ' + str(player3IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]) + ' and ' + str(player4IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
            if player4Hand[0] + player4Hand[1] + player4Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player4Hand[0] + player4Hand[1] + player4Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]), str(player4IC[1]) + ' and ' + str(player4IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
if x == 5:
    decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]) + ' and ' + str(player2IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
            if player2Hand[0] + player2Hand[1] + player2Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player2Hand[0] + player2Hand[1] + player2Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]), str(player2IC[1]) + ' and ' + str(player2IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]) + ' and ' + str(player3IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
            if player3Hand[0] + player3Hand[1] + player3Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player3Hand[0] + player3Hand[1] + player3Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]), str(player3IC[1]) + ' and ' + str(player3IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]) + ' and ' + str(player4IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
            if player4Hand[0] + player4Hand[1] + player4Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player4Hand[0] + player4Hand[1] + player4Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]), str(player4IC[1]) + ' and ' + str(player4IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 5, what would you like to do with ' + str(player5IC[0]) + ' and ' + str(player5IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player5Hand = player5IC
            p = random.randint(0,12)
            player5Hand.append(cards[p])
            print(player5Hand)
            if player5Hand[0] + player5Hand[1] + player5Hand[2] > 21:
                print('Too many')
                p5Win = False
            elif player5Hand[0] + player5Hand[1] + player5Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 5, what would you like to do with ' + str(player5IC[0]), str(player5IC[1]) + ' and ' + str(player5IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player5Hand = player5IC
            p = random.randint(0,12)
            player5Hand.append(cards[p])
            print(player5Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
if x == 6:
    decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]) + ' and ' + str(player2IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
            if player2Hand[0] + player2Hand[1] + player2Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player2Hand[0] + player2Hand[1] + player2Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 2, what would you like to do with ' + str(player2IC[0]), str(player2IC[1]) + ' and ' + str(player2IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player2Hand = player2IC
            p = random.randint(0,12)
            player2Hand.append(cards[p])
            print(player2Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]) + ' and ' + str(player3IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
            if player3Hand[0] + player3Hand[1] + player3Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player3Hand[0] + player3Hand[1] + player3Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 3, what would you like to do with ' + str(player3IC[0]), str(player3IC[1]) + ' and ' + str(player3IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player3Hand = player3IC
            p = random.randint(0,12)
            player3Hand.append(cards[p])
            print(player3Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]) + ' and ' + str(player4IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
            if player4Hand[0] + player4Hand[1] + player4Hand[2] > 21:
                print('Too many')
                p2Win = False
            elif player4Hand[0] + player4Hand[1] + player4Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 4, what would you like to do with ' + str(player4IC[0]), str(player4IC[1]) + ' and ' + str(player4IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player4Hand = player4IC
            p = random.randint(0,12)
            player4Hand.append(cards[p])
            print(player4Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 5, what would you like to do with ' + str(player5IC[0]) + ' and ' + str(player5IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player5Hand = player5IC
            p = random.randint(0,12)
            player5Hand.append(cards[p])
            print(player5Hand)
            if player5Hand[0] + player5Hand[1] + player5Hand[2] > 21:
                print('Too many')
                p5Win = False
            elif player5Hand[0] + player5Hand[1] + player5Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 5, what would you like to do with ' + str(player5IC[0]), str(player5IC[1]) + ' and ' + str(player5IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player5Hand = player5IC
            p = random.randint(0,12)
            player5Hand.append(cards[p])
            print(player5Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
    decision = str(input('Player 6, what would you like to do with ' + str(player6IC[0]) + ' and ' + str(player6IC[1]) + '? '))
    while decision not in ('stand', 'hit', 'double down'):
        decision = str(input('Sorry, your choices are to hit, double down, or stand. Which do you choose? '))
    def hit(decision):
        if decision == 'hit':
            player6Hand = player6IC
            p = random.randint(0,12)
            player6Hand.append(cards[p])
            print(player6Hand)
            if player6Hand[0] + player6Hand[1] + player6Hand[2] > 21:
                print('Too many')
                p5Win = False
            elif player6Hand[0] + player6Hand[1] + player6Hand[2] == 21:
                print('Good job. 21.')
                pass
            else:
                decision = str(input('Player 6, what would you like to do with ' + str(player6IC[0]), str(player6IC[1]) + ' and ' + str(player6IC[2]) + '? '))
        else:
            pass
    def stand(decision):
        if decision == 'stand':
            pass
        else:
            pass
    def doubleD(decision):
        if decision == 'double down':
            player6Hand = player6IC
            p = random.randint(0,12)
            player6Hand.append(cards[p])
            print(player6Hand)
        else:
            pass
    hit(decision)
    stand(decision)
    doubleD(decision)
print('The dealer reveals a ' + str(dealerIC[1]) + ' of ' + dSuitsIC[1] + '. ')

if 'ACE' == (dealerIC[0] or dealerIC[1]):
    if 'ACE' == (dealerIC[0] and dealerIC[1]):
        print('Soft 12')
    elif 'ACE' == (dealerIC[0] and not((dealerIC[1]))):
        print('Soft ' + dealerIC[1] + 10)
    elif 'ACE' != (dealerIC[0] and not(dealerIC[1])):
        print('Soft ' + dealerIC[0] + 10)
    else:
        pass

if 'Jack' == dealerIC[0] or 'Jack' == dealerIC[1]:
    if 'Jack' == (dealerIC[0] and dealerIC[1]):
        print('20')
    elif 'Jack' == dealerIC[0] and 'Jack' != dealerIC[1]:
        print(str(10 + int(dealerIC[1])))
    elif 'Jack' != (dealerIC[0] and 'Jack' != dealerIC[1]):
        print(str(10 + int(dealerIC[0])))
    else:
        pass

if 'Queen' == dealerIC[0] or 'Queen' == dealerIC[1]:
    if 'Queen' == (dealerIC[0] and 'Queen' == dealerIC[1]):
        print('20')
    elif 'Queen' == (dealerIC[0] and 'Queen' != dealerIC[1]):
        print(str(10 + int(dealerIC[1])))
    elif 'Queen' != (dealerIC[0] and 'Queen' != dealerIC[1]):
        print(str(10 + int(dealerIC[0])))
    else:
        pass

if 'King' == dealerIC[0] or 'King' == dealerIC[1]:
    if 'King' == dealerIC[0] and 'King' == dealerIC[1]:
        print('20')
    elif 'King' == dealerIC[0] and 'King' != dealerIC[1]:
        print(str(10 + int(dealerIC[1])))
    elif 'King' != dealerIC[0] and 'King' != (dealerIC[1]):
        print(str(10 + int(dealerIC[0])))
    else:
        pass

print(dealerIC[0] + dealerIC[1])
betPayouts = []
print(mainBets,sideBets)
print(player1IC[3])