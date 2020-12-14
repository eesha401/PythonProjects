from player import Player
from dealer import Dealer


class BlackjackGame:
    def __init__(self, player_names):
        self.dealer = Dealer()
        self.player_list = [Player(i,self.dealer) for i in player_names]
        return

    def play_rounds(self, num_rounds=1):

        player_info = []
        round_info = []

        for round in range (1,num_rounds+1):
            self.dealer.shuffle_deck()

            for i in range(0,2):#deals 2 cards to players and then dealer
                for player in self.player_list:
                    self.dealer.signal_hit(player)
                self.dealer.signal_hit(self.dealer)

            if self.dealer.card_sum == 21: #natural blackjack
                for player in self.player_list:
                    if player.card_sum == 21:
                        player.record_tie()
                    else:
                        player.record_loss()
            else:
                for player in self.player_list:
                    player.play_round()

                    if (self.dealer.card_sum > 21 and player.card_sum < 21) or (player.card_sum > self.dealer.card_sum): #scores
                        player.record_win()
                    elif player.card_sum == self.dealer.card_sum:
                        player.record_tie()
                    else:
                        player.record_loss()

                    player_info.append(str(player))
                    player.discard_hand()

            self.dealer.play_round()

            round_info.append(f'Round {round}' + '\n' + str(self.dealer) + '\n' + '\n'.join(player_info))
            self.dealer.discard_hand()

            player_info.clear()

        return '\n'.join(round_info)



    def reset_game(self):
    
        for player in self.player_list:
            player.discard_hand()
            player.reset_stats()

        return

