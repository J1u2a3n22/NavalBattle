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
    
    def player_opponent(self,player):
        answer=" "
        if player==self.first_player_name:
            answer=self.second_player_name
        else:
            answer=self.first_player_name
        return answer
            

    def print_horizontal_divider(self):
        #Print a line depending on the columns
        for _ in range(self.columns+1):
            print("----", end="")
        print("-")

    def increase_letter(self,letter):
        return chr(ord(letter)+1)

    def print_numbers_row(self):
        print(Fore.CYAN+"|   ", end="")
        for x in range(self.columns):
            print(f"| {x+1} ", end="")
        print(Fore.CYAN+"|")

    def print_board(self,board,show_boats,current_player):
        print(Fore.RESET+f" {current_player}'s Sea: ")
        self.print_numbers_row()
        letter="A"
        for y in range(self.columns):
            self.print_horizontal_divider()
            print(Fore.CYAN+f"| {letter} ", end="")
            for x in range(self.columns):
                cell=board[y][x]
                real_value=cell
                if not show_boats and real_value != SEA and real_value !=  self.missed_shoot  and real_value!=self.successful_shoot:
                    real_value=" "
                if real_value==self.successful_shoot:
                    print(Fore.CYAN+f"| {Fore.RED+real_value} ", end="")  
                else:
                    print(Fore.CYAN+f"| {Fore.YELLOW+real_value} ", end="") 
            letter=self.increase_letter(letter)
            print(Fore.CYAN+"|",)  # Line jump
        self.print_horizontal_divider()

    def print_boards_with_boats(self,board_player1, board_player2):
        print(Fore.RESET+"Showing location of both players' ships:")
        self.print_board(board_player1, True, self.first_player_name)
        self.print_board(board_player2, True, self.second_player_name)


    def request_coordinates(self,player):
        print(Fore.RESET+f"Requesting shot coordinates from player {player}")
        # Infinite loop. Breaks when a correct row is entered
        y = None
        x = None
        while True:
            row_letter = input(Fore.RESET+"Enter the letter of the row:")
            # We need a 1 character letter. If it is not 1 character we use continue to repeat this loop
            if len(row_letter) != 1:
                print(Fore.RESET+"You must enter only 1 letter")
                continue
            # Convert the letter to an index to access the array.
            # A equals ASCII 65, B equals ASCII 66, and so on. To convert the letter to index
            # we convert the letter to its ASCII and subtract 65 (65 is the ASCII of A, so A is 0)
            self.auxiliary_y=row_letter
            y = ord(row_letter) - 65
            # Check if it is valid. If yes, we break the loop
            if self.first_board_game.is_in_range(0, y):
                break
            else:
                print("Invalid row")
        # We do the same but for the column
        while True:
            try:
                x = int(input(Fore.RESET+"Enter the column number: "))
                if self.first_board_game.is_in_range(x-1, 0):
                    x = x-1 # We want the index, so we subtract a 1 always.
                    break
                else:
                    print(Fore.RESET+"Invalid column")
            except:
                print(Fore.RESET+"Enter a valid number.")
        return x, y

    def print_aditional_data(self,x,name_player):
        print(Fore.RED+"----------------------------------------------------------------------------------------------------------------------")
        print(Fore.RED+"                                                    SCORE BOARD                                                       ")
        print(Fore.WHITE+f"{name_player}'s Scoreboard: {self.players_data[name_player]}")
        print(Fore.WHITE+f"{name_player}'s currently coordinates = column: {self.auxiliary_y}, row: {x+1}")
        print(Fore.RED+"----------------------------------------------------------------------------------------------------------------------")


    def indicate_win(self,player):
        print(Fore.GREEN+f"End of game {player} is the winner")

    def play(self,first_player_name,second_player_name):

        self.players_data[first_player_name]=0
        self.players_data[second_player_name]=0

        list_of_key = list(self.players_data.keys())

        name_first_player=list_of_key[0]
        name_second_player=list_of_key[1]
        self.first_player_name=name_first_player
        self.second_player_name=name_second_player
        board_first_player,board_second_player=self.first_board_game.get_initial_board(),self.second_board_game.get_initial_board()
        board_first_player=self.first_board_game.randomly_assign_ships()
        board_second_player=self.second_board_game.randomly_assign_ships()
        self.print_boards_with_boats(board_first_player,board_second_player)
        current_shift=name_first_player
        while True:
            print(Fore.RESET+f" {current_shift} Turn ")
            enemy_board=board_first_player
            if current_shift==name_first_player:
                enemy_board=board_second_player
            self.print_board(enemy_board,False,self.player_opponent(current_shift))
            x,y=self.request_coordinates(current_shift)
            successful,is_repeated=self.first_board_game.shoot(x,y,enemy_board)
            self.print_board(enemy_board,False,self.player_opponent(current_shift))
            if is_repeated==True:
                print(Fore.RESET+"This Position shot before, Please insert new coordinates again")
            else:    
                if successful:
                    print(Fore.RESET+"successful shot")
                    self.players_data[current_shift]= self.players_data[current_shift]+1
                    self.print_aditional_data(x,current_shift)
                    if self.first_board_game.all_sunken_ships(enemy_board):
                        self.indicate_win(current_shift)
                        self.print_boards_with_boats(board_first_player,board_second_player)
                        break
                    current_shift=self.player_opponent(current_shift)
                else:
                    print(Fore.RESET+"Failure shoot")
                    current_shift=self.player_opponent(current_shift)


    def show_menu(self):
        print("\n")
        choice,sub_choise="",""
        count=0
        aux_list=list()
        while choice !="2":
            menu=Fore.BLUE+"""
                                    Welcome to Battle Ship Console Game
                                            Please Choice your option:
                                            1. Play
                                            2. Exit
                                            Your choice: 
            """
            #While don't choice any option the menu will show
            choice=input(menu)
            if choice=="1":
                count=0
                self.__init__(10,10,5,"p1","p2")
                while count<2 and True:
                    sub_menu=Fore.BLUE+f"""
                                        Please insert your name for the {count+1} player:                     
                    """
                    sub_choise=str(input(sub_menu))
                    if len(sub_choise)==0:
                        print(Fore.BLUE+"               You must enter an one value letter               " )
                        continue
                    else:    
                        aux_list.append(sub_choise)
                        count=count+1
                self.play(aux_list[0],aux_list[1])

new_game=BattleShipUI(10,10,5,"p1","p2")
new_game.show_menu()
