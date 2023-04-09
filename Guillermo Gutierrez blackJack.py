from numpy import random
def deck():
    nominals = ('Ace','Two','Three','Four','Five','Six','Seven','Eight',
    'Nine','Ten','Jack','Queen','King')
    suits = ("Clubs","Hearts","Spades","Diamonds")
    p = random.randint(-18,18)
    placement = 209 + p
    cardDict = {
    ("Ace", "ace"): 1,
    ("Two", "two", "2"): 2,
    ("Three", "three", "3"): 3,
    ("Four", "four", "4"): 4,
    ("Five", "five", "5"): 5,
    ("Six", "six", "6"): 6,
    ("Seven", "seven", "7"): 7,
    ("Eight","eight", "8"): 8,
    ("Nine", "nine", "9"): 9,
    ("Ten", "ten", "10"): 10,
    ("Jack", "jack"): 10,
    ("Queen", "queen"): 10,
    ("King", "king"): 10
    }
    cardsAll = []
    for i in nominals:
        for y in suits:
            cardsAll.append(i + ' of ' + y)
    cardsAll = cardsAll * 8
    random.shuffle(cardsAll)
    n = 416 - placement
    cardsInPlay = cardsAll[n:]
deck()

def announceGame():

    print('::| /\ | /\ | /\ |         | /\ | /\ | /\ |::')
    print('::| Good evening and Welcome to all!      |::')
    print('::| At this table, the house will be host-|::')
    print('::| -ing Black Jack. Four decks are used  |::')
    print('::| out of a total of Eight. The payouts  |::')
    print('::| for Black Jack are 3 to 2. For insura-|::')
    print('::| -nce the payout is 2 to 1.            |::')
    print('::| Beating the Dealer will payout 1 to 1 |::')
    print('::| Before we begin, how many will join us|::')
    print('::| for our next hand? Unfortunately, the |::')
    print('::| table only seats six people.          |::')
    print('::| /\ | /\ | /\ |         | /\ | /\ | /\ |::')
    try:
        people = int(input())
    except ValueError:
        print('Could you repeat that as an integer? Let us go over it all again.')
        announceGame()
    nameList = []
    i = 0
    while i < 7:
        nameList.append(input(f'Player{i+1}, Hello! Please tell us your name!\n'))
        i += 1
    mainBetList = []
    i = 0
    while i < 7:
        mainBetList.append(input(f'{nameList(i)}, Please give us your Main Bet for this round.\n'))
        i += 1
    sideBetList = []
    i = 0
    while i < 7:
        sideBetList.append(input(f'{nameList(i)}, Please give us your Side Bet for this round.\n'))
        i += 1
    print('All bets are now closed. Let the games begin.\n')
announceGame()

class Better:
  def __init__(self, name, mainBet, sideBet, hand, x):
    name = announceGame.nameList[x]
    self.name = name
    mainBet = announceGame.mainBetList[x]
    self.mainBet = mainBet
    sideBet = announceGame.sideBetList[x]
    self.sideBet = sideBet
    self.hand = hand

def gameMechanics():

    def move():
        pass

    def cardPulling():
        pass

    def beatDealer():
        pass

    def payouts():
        pass