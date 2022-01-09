from models.board import Board
from services.diceservice import DiceService

class SnakeAndLadderService:

    def __init__(self,size=100):
        self.board=Board(size)

    def setPlayers(self,players):
        self.playerQueue=[]
        self.initialNumberOfPlayers = len(players)
        playerPositions = {}
        for player in players:
            self.playerQueue.append(player)

            playerPositions[player.getId()]=0
        self.board.playersCurrentPositions = playerPositions

    def setSnakes(self,snakrs):
        self.board.snakeList=snakrs

    def setLadders(self,ladders):
        self.board.ladderList=ladders

    def getTotalValueAfterDiceRolls(self):
        return DiceService().roll()

    def getNewPositionAfterGoingThroughtSnakesAndLadders(self,player,position):
        print("Processing Position " + str(position) + " for " + player.getName())
        while 1:
            for ladder in self.board.ladderList:
                if ladder.getStart() == position:
                    print(player.getName() + " Ladder Alert at:" + str(position) + " moved from " + str(
                        position) + " to " + str(ladder.getEnd()))
                    position = ladder.getEnd()
                    continue

            for snake in self.board.snakeList:
                if snake.getStart() == position:
                    print(player.getName() + " Snake Alert at:" + str(position) + " moved from " + str(
                        position) + " to " + str(snake.getEnd()))
                    position = snake.getEnd()
                    continue
            break
        return position

    def movePlayer(self,player,diceValue):
        oldpos = self.board.playersCurrentPositions[player.getId()]
        newpos = oldpos + diceValue
        boardSize = self.board.getSize()
        if(newpos>boardSize):
            newpos=oldpos
        else:
            newpos=self.getNewPositionAfterGoingThroughtSnakesAndLadders(player,newpos)
        self.board.playersCurrentPositions[player.getId()]=newpos

    def hasPlayerWon(self, player):
        return self.board.getPlayersCurrentPositions().get(player.getId()) == self.board.getSize()

    def isGameCompleted(self):
        # we pop player after he win from playerQueue
        return self.initialNumberOfPlayers > len(self.playerQueue)

    def startGame(self):
        while (self.isGameCompleted() == False):
            diceValue = self.getTotalValueAfterDiceRolls()
            player = self.playerQueue.pop(0)  # fifo
            self.movePlayer(player, diceValue)
            if self.hasPlayerWon(player):
                print(player.getName() + " wins the game")
                self.board.getPlayersCurrentPositions().pop(player.getId())
            else:
                self.playerQueue.append(player)  # append player for next turn
