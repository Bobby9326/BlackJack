import random

class Player:
    def __init__(self,name):
        self.hand = [] 
        self.name = name
        self.score = 0
    def drawCard(self,card):
        self.hand.append(card)
    def showCard(self):
        print(self.name,self.hand)
    def checkScore(self):
        self.score = 0
        for i in self.hand:
            number = i[0:len(i)-1]
            if number in "JQK":
                if self.score == 1:
                    self.score += 20
                else:
                    self.score += 10
            elif number == "A":
                if self.score == 10 and len(self.hand) == 2:
                    self.score += 11
                else:
                    self.score += 1
            else:
                self.score += int(number)
class Dealer(Player):
    def endGame(self,list_names,list_scores):
        for i in range(2):
            list_scores[i] = 0 if list_scores[i]>21 else list_scores[i]
        if list_scores[0] > list_scores[1]:
            print("%s ชนะด้วยคะแนน %s"%(list_names[0],list_scores[0]))
        elif list_scores[0] < list_scores[1]:
            print("%s ชนะด้วยคะแนน %s"%(list_names[1],list_scores[1]))
        else:
            print("%s และ %s เสมอด้วยคะแนน %s"%(list_names[0],list_names[1],list_scores[1]))
class Deck:
    def __init__(self) :
        self.deck = [["A♠","2♠","3♠","4♠","5♠","6♠","7♠","8♠","9♠","10♠","J♠","Q♠","K♠"],["A♥","2♥","3♥","4♥","5♥","6♥","7♥","8♥","9♥","10♥","J♥","Q♥","K♥"],["A♦","2♦","3♦","4♦","5♦","6♦","7♦","8♦","9♦","10♦","J♦","Q♦","K♦"],["A♣","2♣","3♣","4♣","5♣","6♣","7♣","8♣","9♣","10♣","J♣","Q♣","K♣"]]
    def deal(self):
        suit = random.randint(0,len(self.deck)-1) #สุ่มหน้าไพ่
        number = random.randint(0,len(self.deck[suit])-1) #สุ่มหมายเล
        card = self.deck[suit][number]
        self.deck[suit].pop(number)
        if [] in self.deck:
            self.deck.remove([])
        return card

deck = Deck()
player = Player("player")
dealer = Dealer("dealer")
for i in range(2):
    player.drawCard(deck.deal())
    dealer.drawCard(deck.deal())
while True:
    player.showCard()
    player.checkScore()
    dealer.checkScore()
    ans = int(input("ต้องการจั่วการ์ด กด1 /ไม่ กด 2 :"))
    if ans == 1:
        player.drawCard(deck.deal())
    if dealer.score <= 17:
        dealer.drawCard(deck.deal())
        print("dealer จั่ว")
    if ans != 1 and dealer.score > 17:
        break
player.showCard()
dealer.showCard()
dealer.endGame(["player","dealer"],[player.score,dealer.score])
