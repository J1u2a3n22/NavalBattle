from email.policy import default
from board import * 
from colorama import Fore,init

init() 

class BattleShipUI:
    def __init__(self,rows,columns,number_of_ships,first_player_name="P1",second_player_name="P2"):
        self.first_board_game=Board(10,10,5)
        self.second_board_game=Board(10,10,5)
        self.rows=10
        self.columns=10

        self.first_player_name=first_player_name
        self.second_player_name=second_player_name
        
        self.players_data=dict()
        self.auxiliary_y=""
        
        self.number_attemps_first_player=0
        self.number_attemps_second_player=0
        self.missed_shoot="-"
        self.successful_shoot="*"
        