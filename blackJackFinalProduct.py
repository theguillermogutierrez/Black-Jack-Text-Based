## Copyright Guillermo Gutierrez 2022

## Begin program by importing random module which will be used in created the deck in play
import random

## The following function both creates the basic structure of a Black Jack deck and creates the deck in play
def createDeck():
    """
    Creates a deck of cards and shuffles them.
    """
    nominals = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
                'Nine', 'Ten', 'Jack', 'Queen', 'King')
    suits = ("Clubs", "Hearts", "Spades", "Diamonds")

    cardsAll = [f"{nominal} of {suit}" for nominal in nominals for suit in suits]
    cardsAll *= 8
    random.shuffle(cardsAll)

    placement = 209 + random.randint(-18, 18)
    cardsInPlay = cardsAll[416 - placement:]

    return cardsInPlay

## Assigns the cardsInPlay variable from the previous function to a global variable
cardsInPlay = createDeck()

 ## Announces the game and takes user input for the number of players, their names, and their bets
def announceGame():

    print("::| Welcome to Black Jack!                                    |::")
    print("::| Four decks are used out of a total of eight.              |::")
    print("::| The payouts for Black Jack are 3 to 2.                    |::")
    print("::| The payout for insurance is 2 to 1.                       |::")
    print("::| Beating the Dealer will payout 1 to 1.                    |::")
    print("::| Before we begin, how many will join us for our next hand? |::")

    while True:
        try:
            numPlayers = int(input("Number of players (max 6): "))
            if 1 <= numPlayers <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

    nameList = [input(f"Player {i + 1}, please tell us your name: ") for i in range(numPlayers)]

    mainBetList = [float(input(f"{name}, please give us your Main Bet for this round: ")) for name in nameList]
    sideBetList = [float(input(f"{name}, please give us your Side Bet for this round: ")) for name in nameList]

    print("All bets are now closed. Let the games begin.\n")

    return nameList, mainBetList, sideBetList


nameList, mainBetList, sideBetList = announceGame()

## Class constructor of Better including their relevant attributes
class Better:
    def __init__(self, name, mainBet, sideBet, hand):
        self.name = name
        self.main_bet = mainBet
        self.side_bet = sideBet
        self.hand = hand


betters = [Better(name, mainBet, sideBet, []) for name, mainBet, sideBet in zip(nameList, mainBetList, sideBetList)]

## This is where the core game mechanics are finally built after creating the various dictionaires, user input collection, and class construction
def dealInitialCards():
    for better in betters:
        better.hand = [cardsInPlay.pop(), cardsInPlay.pop()]

    dealerHand = [cardsInPlay.pop(), cardsInPlay.pop()]

    return dealerHand


def calculateScore(hand):
    score = 0
    aces = 0

    cardValues = {
        'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
        'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10
    }

    for card in hand:
        cardNominal = card.split()[0]
        value = cardValues[cardNominal]
        score += value

        if cardNominal == 'Ace':
            aces += 1

    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score


def playerTurn(better):
    while True:
        print(f"{better.name}'s hand: {better.hand} (score: {calculateScore(better.hand)})")
        action = input(f"{better.name}, do you want to hit or stand? ").lower()

        if action == 'hit':
            better.hand.append(cardsInPlay.pop())

            if calculateScore(better.hand) > 21:
                print(f"{better.name} has busted with a score of {calculateScore(better.hand)}")
                return
        elif action == 'stand':
            return
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")


def dealerTurn(dealerHand):
    while calculateScore(dealerHand) < 17:
        dealerHand.append(cardsInPlay.pop())

    return dealerHand


def determineWinners(dealerHand):
    dealerScore = calculateScore(dealerHand)
    print(f"Dealer's hand: {dealerHand} (score: {dealerScore})")

    for better in betters:
        playerScore = calculateScore(better.hand)

        if playerScore > 21:
            print(f"{better.name} has lost (busted).")
        elif dealerScore > 21 or playerScore > dealerScore or (playerScore == 21 and len(better.hand) == 2):
            print(f"{better.name} has won with a score of {playerScore}.")
        elif playerScore == dealerScore:
            print(f"{better.name} has pushed (tied) with a score of {playerScore}.")
        else:
            print(f"{better.name} has lost with a score of {playerScore}.")


if __name__ == "__main__":
    dealerHand = dealInitialCards()

    for better in betters:
        playerTurn(better)

    dealerHand = dealerTurn(dealerHand)

    determineWinners(dealerHand)