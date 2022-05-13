from PyQt5.QtWidgets import *
from P2blackjack import Ui_MainWindow
import random
from PyQt5 import QtCore, QtGui, QtWidgets





class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.startButton.clicked.connect(lambda: self.start())
        self.player_list = []
        self.computer_list = []
        self.player_sum = 0
        self.computer_sum = 0
        self.submitButton.clicked.connect(lambda: self.submit1())
        self.submitButton_2.clicked.connect(lambda: self.submit2())
        self.submitButton_3.clicked.connect(lambda: self.submit3())

    def checkover(self):
        player_sum = sum(self.player_list)
        dealer_sum = sum(self.computer_list)
        if player_sum > 21:
            self.description2.setText("Dealer has {}. You have {}. Dealer Wins".format(dealer_sum, player_sum))
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        else:
            pass



    def player21(self):
        dealer_sum = sum(self.computer_list)
        self.description2.setText("You have 21. Dealer's turn.")

        if self.computer_list[1] == 2:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
        elif self.computer_list[1] == 3:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
        elif self.computer_list[1] == 4:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
        elif self.computer_list[1] == 5:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
        elif self.computer_list[1] == 6:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
        elif self.computer_list[1] == 7:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
        elif self.computer_list[1] == 8:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
        elif self.computer_list[1] == 9:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
        elif self.computer_list[1] == 10:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
        elif self.computer_list[1] == 11:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
        elif self.computer_list[1] == 12:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
        elif self.computer_list[1] == 13:
            self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
        elif self.computer_list[1] == 1:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

        if sum(self.computer_list) == 21:
            self.description2.setText("Dealer has 21. You have 21.The round ends in a push")
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        elif sum(self.computer_list) > 15:
            self.description2.setText("Dealer has {}. You have 21. You win the round".format(dealer_sum))
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        elif dealer_sum <= 15:
            self.computer_list.append(random.randint(1, 13))

            if self.computer_list[2] == 2:
                    self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[2] == 3:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[2] == 4:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[2] == 5:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[2] == 6:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[2] == 7:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[2] == 8:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[2] == 9:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[2] == 10:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[2] == 11:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[2] == 12:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[2] == 13:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[2] == 1:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

            if self.computer_list[2] == 1:
                self.computer_list[2] = 11
            elif self.computer_list[2] > 10:
                self.computer_list[2] = 10

            dealer_sum = sum(self.computer_list)

            if dealer_sum == 21:
                self.description2.setText("Dealer has 21. You have 21.The round ends in a push")
                self.description1.setText('')
                self.hitButton.hide()
                self.stayButton.hide()
                self.submitButton.hide()
                self.submitButton_2.hide()
                self.submitButton_3.hide()

            elif sum(self.computer_list) > 15:
                self.description2.setText("Dealer has {}. You have 21. You win the round".format(dealer_sum))
                self.description1.setText('')
                self.hitButton.hide()
                self.stayButton.hide()
                self.submitButton.hide()
                self.submitButton_2.hide()
                self.submitButton_3.hide()

            elif dealer_sum <= 15:
                self.computer_list.append(random.randint(1, 13))

                if self.computer_list[3] == 2:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
                elif self.computer_list[3] == 3:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
                elif self.computer_list[3] == 4:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
                elif self.computer_list[3] == 5:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
                elif self.computer_list[3] == 6:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
                elif self.computer_list[3] == 7:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
                elif self.computer_list[3] == 8:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
                elif self.computer_list[3] == 9:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
                elif self.computer_list[3] == 10:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
                elif self.computer_list[3] == 11:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
                elif self.computer_list[3] == 12:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
                elif self.computer_list[3] == 13:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
                elif self.computer_list[3] == 1:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

                if self.computer_list[3] == 1:
                    self.computer_list[3] = 11
                elif self.computer_list[3] > 10:
                    self.computer_list[3] = 10

                dealer_sum = sum(self.computer_list)

                if dealer_sum == 21:
                    self.description2.setText("Dealer has 21.You have 21. The round ends in a push")
                    self.description1.setText('')
                    self.hitButton.hide()
                    self.stayButton.hide()
                    self.submitButton.hide()
                    self.submitButton_2.hide()
                    self.submitButton_3.hide()

                elif sum(self.computer_list) > 15:
                    self.description2.setText("Dealer has {}. You have 21. You win the round".format(dealer_sum))
                    self.description1.setText('')
                    self.hitButton.hide()
                    self.stayButton.hide()
                    self.submitButton.hide()
                    self.submitButton_2.hide()
                    self.submitButton_3.hide()

                elif dealer_sum <= 15:
                    self.computer_list.append(random.randint(1, 13))

                    if self.computer_list[4] == 2:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
                    elif self.computer_list[4] == 3:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
                    elif self.computer_list[4] == 4:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
                    elif self.computer_list[4] == 5:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
                    elif self.computer_list[4] == 6:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
                    elif self.computer_list[4] == 7:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
                    elif self.computer_list[4] == 8:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
                    elif self.computer_list[4] == 9:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
                    elif self.computer_list[4] == 10:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
                    elif self.computer_list[4] == 11:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
                    elif self.computer_list[4] == 12:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
                    elif self.computer_list[4] == 13:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
                    elif self.computer_list[4] == 1:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

                    if self.computer_list[4] == 1:
                        self.computer_list[4] = 11
                    elif self.computer_list[4] > 10:
                        self.computer_list[4] = 10

                    dealer_sum = sum(self.computer_list)

                    if dealer_sum == 21:
                        self.description2.setText("Dealer has 21. You have 21. The round ends in a push")
                        self.description1.setText('')
                        self.hitButton.hide()
                        self.stayButton.hide()
                        self.submitButton.hide()
                        self.submitButton_2.hide()
                        self.submitButton_3.hide()

                    else:
                        self.description2.setText("Dealer has {}. You have 21. You win the round".format(dealer_sum))
                        self.description1.setText('')
                        self.hitButton.hide()
                        self.stayButton.hide()
                        self.submitButton.hide()
                        self.submitButton_2.hide()
                        self.submitButton_3.hide()


    def check(self):
        dealer_sum = sum(self.computer_list)
        player_sum = sum(self.player_list)
        if  player_sum == dealer_sum:
            if self.computer_list[1] == 2:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[1] == 3:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[1] == 4:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[1] == 5:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[1] == 6:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[1] == 7:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[1] == 8:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[1] == 9:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[1] == 10:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[1] == 11:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[1] == 12:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[1] == 13:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[1] == 1:
                self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))
            self.description2.setText("Dealer has {}. You have {}. The round is a push".format(dealer_sum, player_sum))
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        elif player_sum > 21:
            if self.computer_list[1] == 2:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[1] == 3:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[1] == 4:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[1] == 5:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[1] == 6:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[1] == 7:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[1] == 8:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[1] == 9:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[1] == 10:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[1] == 11:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[1] == 12:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[1] == 13:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[1] == 1:
                self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))
            self.description2.setText("Dealer has {}. You have {}. Dealer wins".format(dealer_sum, player_sum))
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        elif dealer_sum > player_sum and dealer_sum <= 21:
            if self.computer_list[1] == 2:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[1] == 3:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[1] == 4:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[1] == 5:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[1] == 6:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[1] == 7:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[1] == 8:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[1] == 9:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[1] == 10:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[1] == 11:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[1] == 12:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[1] == 13:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[1] == 1:
                self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))
            self.description2.setText("Dealer has {}. You have {}. Dealer wins".format(dealer_sum, player_sum))
            self.description1.setText('')
            self.hitButton.hide()
            self.stayButton.hide()
            self.submitButton.hide()
            self.submitButton_2.hide()
            self.submitButton_3.hide()

        elif player_sum > dealer_sum and dealer_sum < 16:
            if self.computer_list[1] == 2:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[1] == 3:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[1] == 4:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[1] == 5:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[1] == 6:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[1] == 7:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[1] == 8:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[1] == 9:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[1] == 10:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[1] == 11:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[1] == 12:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[1] == 13:
                self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[1] == 1:
                self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))
            self.computer_list.append(random.randint(1, 13))

            if self.computer_list[2] == 2:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.computer_list[2] == 3:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.computer_list[2] == 4:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.computer_list[2] == 5:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.computer_list[2] == 6:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.computer_list[2] == 7:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.computer_list[2] == 8:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.computer_list[2] == 9:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.computer_list[2] == 10:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.computer_list[2] == 11:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.computer_list[2] == 12:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.computer_list[2] == 13:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.computer_list[2] == 1:
                self.computer_card_3.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

            if self.computer_list[2] == 1:
                self.computer_list[2] = 11
            elif self.computer_list[2] > 10:
                self.computer_list[2] = 10

            dealer_sum = sum(self.computer_list)

            if dealer_sum > 21:
                self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))
                self.description1.setText('')
                self.hitButton.hide()
                self.stayButton.hide()
                self.submitButton.hide()
                self.submitButton_2.hide()
                self.submitButton_3.hide()

            elif dealer_sum > player_sum:
                self.description2.setText("Dealer has {}. You have {}. Dealer wins".format(dealer_sum, player_sum))
                self.description1.setText('')
                self.hitButton.hide()
                self.stayButton.hide()
                self.submitButton.hide()
                self.submitButton_2.hide()
                self.submitButton_3.hide()

            elif dealer_sum > 15 and player_sum > dealer_sum:
                self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))
                self.description1.setText('')
                self.hitButton.hide()
                self.stayButton.hide()
                self.submitButton.hide()
                self.submitButton_2.hide()
                self.submitButton_3.hide()

            else:
                self.computer_list.append(random.randint(1, 13))

                if self.computer_list[3] == 2:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
                elif self.computer_list[3] == 3:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
                elif self.computer_list[3] == 4:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
                elif self.computer_list[3] == 5:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
                elif self.computer_list[3] == 6:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
                elif self.computer_list[3] == 7:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
                elif self.computer_list[3] == 8:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
                elif self.computer_list[3] == 9:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
                elif self.computer_list[3] == 10:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
                elif self.computer_list[3] == 11:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
                elif self.computer_list[3] == 12:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
                elif self.computer_list[3] == 13:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
                elif self.computer_list[3] == 1:
                    self.computer_card_4.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

                if self.computer_list[3] == 1:
                    self.computer_list[3] = 11
                elif self.computer_list[3] > 10:
                    self.computer_list[3] = 10

                dealer_sum = sum(self.computer_list)

                if dealer_sum > 21:
                    self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))
                    self.description1.setText('')
                    self.hitButton.hide()
                    self.stayButton.hide()
                    self.submitButton.hide()
                    self.submitButton_2.hide()
                    self.submitButton_3.hide()

                elif dealer_sum > player_sum:
                    self.description2.setText("Dealer has {}. You have {}. Dealer wins".format(dealer_sum, player_sum))
                    self.description1.setText('')
                    self.hitButton.hide()
                    self.stayButton.hide()
                    self.submitButton.hide()
                    self.submitButton_2.hide()
                    self.submitButton_3.hide()

                elif dealer_sum > 15 and player_sum > dealer_sum:
                    self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))
                    self.description1.setText('')
                    self.hitButton.hide()
                    self.stayButton.hide()
                    self.submitButton.hide()
                    self.submitButton_2.hide()
                    self.submitButton_3.hide()


                else:
                    self.computer_list.append(random.randint(1, 13))

                    if self.computer_list[4] == 2:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
                    elif self.computer_list[4] == 3:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
                    elif self.computer_list[4] == 4:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
                    elif self.computer_list[4] == 5:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
                    elif self.computer_list[4] == 6:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
                    elif self.computer_list[4] == 7:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
                    elif self.computer_list[4] == 8:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
                    elif self.computer_list[4] == 9:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
                    elif self.computer_list[4] == 10:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
                    elif self.computer_list[4] == 11:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
                    elif self.computer_list[4] == 12:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
                    elif self.computer_list[4] == 13:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
                    elif self.computer_list[4] == 1:
                        self.computer_card_5.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

                    if self.computer_list[4] == 1:
                        self.computer_list[4] = 11
                    elif self.computer_list[4] > 10:
                        self.computer_list[4] = 10

                    dealer_sum = sum(self.computer_list)

                    if dealer_sum > 21:
                        self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))
                        self.description1.setText('')
                        self.hitButton.hide()
                        self.stayButton.hide()
                        self.submitButton.hide()
                        self.submitButton_2.hide()
                        self.submitButton_3.hide()

                    elif dealer_sum > player_sum:
                        self.description2.setText('')
                        self.description2.setText("Dealer has {}. You have {}. Dealer wins".format(dealer_sum, player_sum))
                        self.description1.setText('')
                        self.hitButton.hide()
                        self.stayButton.hide()
                        self.submitButton.hide()
                        self.submitButton_2.hide()
                        self.submitButton_3.hide()

                    else:
                        self.description2.setText("Dealer has {}. You have {}. You win".format(dealer_sum, player_sum))



    def stay(self):
        self.group.setExclusive(False)
        self.hitButton.setChecked(False)
        self.stayButton.setChecked(False)
        self.group.setExclusive(True)


        self.hitButton.hide()
        self.stayButton.hide()


    def start(self):
        self.startButton.hide()
        self.player_list = []
        self.computer_list = []
        self.description2.setText('')
        self.player_list.append(random.randint(1,13))
        self.player_list.append(random.randint(1, 13))
        self.computer_list.append(random.randint(1, 13))
        self.computer_list.append(random.randint(1, 13))



        if self.player_list[0] == 2:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
        elif self.player_list[0] == 3:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
        elif self.player_list[0] == 4:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
        elif self.player_list[0] == 5:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
        elif self.player_list[0] == 6:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
        elif self.player_list[0] == 7:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
        elif self.player_list[0] == 8:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
        elif self.player_list[0] == 9:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
        elif self.player_list[0] == 10:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
        elif self.player_list[0] == 11:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
        elif self.player_list[0] == 12:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
        elif self.player_list[0] == 13:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
        elif self.player_list[0] == 1:
            self.player_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

        if self.player_list[1] == 2:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
        elif self.player_list[1] == 3:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
        elif self.player_list[1] == 4:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
        elif self.player_list[1] == 5:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
        elif self.player_list[1] == 6:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
        elif self.player_list[1] == 7:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
        elif self.player_list[1] == 8:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
        elif self.player_list[1] == 9:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
        elif self.player_list[1] == 10:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
        elif self.player_list[1] == 11:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
        elif self.player_list[1] == 12:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
        elif self.player_list[1] == 13:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
        elif self.player_list[1] == 1:
            self.player_card_2.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

        if self.computer_list[0] == 2:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
        elif self.computer_list[0] == 3:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
        elif self.computer_list[0] == 4:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
        elif self.computer_list[0] == 5:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
        elif self.computer_list[0] == 6:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
        elif self.computer_list[0] == 7:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
        elif self.computer_list[0] == 8:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
        elif self.computer_list[0] == 9:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
        elif self.computer_list[0] == 10:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
        elif self.computer_list[0] == 11:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
        elif self.computer_list[0] == 12:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
        elif self.computer_list[0] == 13:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
        elif self.computer_list[0] == 1:
            self.computer_card_1.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

        self.computer_card_2.setPixmap(QtGui.QPixmap("../Downloads/card_back.jpeg"))


        if self.player_list[0] == 1:
            self.player_list[0] = 11
        elif self.player_list[0] > 10:
            self.player_list[0] = 10
        if self.player_list[1] == 1:
            self.player_list[1] = 11
        elif self.player_list[1] > 10:
            self.player_list[1] = 10

        if self.computer_list[0] == 1:
            self.computer_list[0] = 11
        elif self.computer_list[0] > 10:
            self.computer_list[0] = 10
        if self.computer_list[1] == 1:
            self.computer_list[1] = 11
        elif self.computer_list[1] > 10:
            self.computer_list[1] = 10

        if sum(self.player_list) == 21:
            self.player21()

        else:
            self.hitButton.show()
            self.stayButton.show()
            self.submitButton.show()
            self.description1.setText('Select Hit or Stay')

    def submit1(self):
        self.submitButton.hide()
        if self.hitButton.isChecked():
            self.player_list.append(random.randint(1, 13))

            self.group.setExclusive(False)
            self.hitButton.setChecked(False)
            self.stayButton.setChecked(False)
            self.group.setExclusive(True)

            if self.player_list[2] == 2:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.player_list[2] == 3:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.player_list[2] == 4:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.player_list[2] == 5:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.player_list[2] == 6:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.player_list[2] == 7:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.player_list[2] == 8:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.player_list[2] == 9:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.player_list[2] == 10:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.player_list[2] == 11:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.player_list[2] == 12:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.player_list[2] == 13:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.player_list[2] == 1:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

            if self.player_list[2] == 1:
                self.player_list[2] = 11
            elif self.player_list[2] > 10:
                self.player_list[2] = 10



            if sum(self.player_list) == 21:
                self.player21()
            else:
                self.hitButton.show()
                self.stayButton.show()
                self.submitButton_2.show()
                self.description1.setText('Select Hit or Stay')
                self.checkover()

        elif self.stayButton.isChecked():
            self.stay()
            self.check()

        else:
            self.hitButton.show()
            self.stayButton.show()
            self.submitButton.show()


    def submit2(self):
        self.submitButton_2.hide()
        if self.hitButton.isChecked():
            self.player_list.append(random.randint(1, 13))

            self.group.setExclusive(False)
            self.hitButton.setChecked(False)
            self.stayButton.setChecked(False)
            self.group.setExclusive(True)

            if self.player_list[3] == 2:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.player_list[3] == 3:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.player_list[3] == 4:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.player_list[3] == 5:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.player_list[3] == 6:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.player_list[3] == 7:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.player_list[3] == 8:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.player_list[3] == 9:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.player_list[3] == 10:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.player_list[3] == 11:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.player_list[3] == 12:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.player_list[3] == 13:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.player_list[3] == 1:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

            if self.player_list[3] == 1:
                self.player_list[3] = 11
            elif self.player_list[3] > 10:
                self.player_list[3] = 10



            if sum(self.player_list) == 21:
                self.player21()
            else:
                self.hitButton.show()
                self.stayButton.show()
                self.submitButton_3.show()
                self.description1.setText('Select Hit or Stay')
                self.checkover()

        elif self.stayButton.isChecked():
            self.stay()
            self.check()

    def submit3(self):
        self.submitButton3.hide()
        if self.hitButton.isChecked():
            self.player_list.append(random.randint(1, 13))

            self.group.setExclusive(False)
            self.hitButton.setChecked(False)
            self.stayButton.setChecked(False)
            self.group.setExclusive(True)

            if self.player_list[4] == 2:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/2_card.png"))
            elif self.player_list[4] == 3:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/3_card.png"))
            elif self.player_list[4] == 4:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/4_card.png"))
            elif self.player_list[4] == 5:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/5_card.png"))
            elif self.player_list[4] == 6:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/6_card.png"))
            elif self.player_list[4] == 7:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/7_card.png"))
            elif self.player_list[4] == 8:
                self.player_card_5.setPixmap(QtGui.QPixmap("../Downloads/8_card.png"))
            elif self.player_list[4] == 9:
                self.player_card_3.setPixmap(QtGui.QPixmap("../Downloads/9_card.png"))
            elif self.player_list[5] == 10:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/10_card.png"))
            elif self.player_list[5] == 11:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/jack_card.png"))
            elif self.player_list[5] == 12:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/queen_card.jpeg"))
            elif self.player_list[5] == 13:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/king_card.png"))
            elif self.player_list[5] == 1:
                self.player_card_4.setPixmap(QtGui.QPixmap("../Downloads/ace_card.png"))

            if self.player_list[5] == 1:
                self.player_list[5] = 11
            elif self.player_list[5] > 10:
                self.player_list[5] = 10



            if sum(self.player_list) == 21:
                self.player21()
            else:
                self.check()

        elif self.stayButton.isChecked():
            self.stay()
            self.check()


            













