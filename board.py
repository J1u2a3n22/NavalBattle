from calendar import c
from enum import Enum
import random
import os


#Global variables
#Represent the sea
SEA=" "
 
# This enum represents the values and quantity of each boats
class Ships(Enum):    
    A = 5    #Represents a aircraft carrier boat
    B = 4    #Represents a battleship boat
    C = 3    #Represents a cruiser boat
    S = 1    #Represents a submarine boat
    D = 2    #Represents a destroyer boat
    

class Board:
    def __init__(self,rows,columns,number_of_ships):
        self.board=[]
        self.rows=rows
        self.columns=columns
        self.number_of_ships=number_of_ships
        self.missed_shoot="-"
        self.successful_shoot="*"

    def get_initial_board(self):
        for y in range(self.rows):
            #Add a new row
            self.board.append([])
            for x in range(self.columns):
                #Add into the new row a variable to identify is a sea
                self.board[y].append(SEA)
        return self.board

    def get_random_x(self):
        return random.randint(0, self.columns-1)

    def get_random_y(self):
        return random.randint(0, self.rows-1)

    def is_in_range(self,x,y):
        return x >= 0 and x <= self.columns-1 and y >= 0 and y <= self.rows-1

    def is_sea(self,x,y):
        return self.board[y][x]==SEA

    def is_sea_with_board(self,x,y,board):
        return board[y][x]==SEA
    
    def put_ships_horizontally(self,enum_boat):
        count=0
        answer=True
        filled_board=False
        enum_value=enum_boat.value
        if enum_boat.name=="S":
           enum_value=3
        while filled_board==False:
            answer=True
            x=self.get_random_x()
            y=self.get_random_y()
            x1=x
            y1=y
            while count<enum_value:
                if self.is_in_range(x1,y1) and self.is_sea(x1,y1):
                    x1=x1+1
                    answer=answer and True
                else:
                    answer=answer and False
                    break
                count=count+1
            if answer==True:
                count=0
                x1=x
                y1=y
                while count<enum_value:
                    if self.is_in_range(x1,y1) and self.is_sea(x1,y1):
                        self.board[y1][x1]=enum_boat.name
                        x1=x1+1
                    count=count+1
                filled_board=True
            else:
                count=0
        return self.board

    def put_ships_vertically(self,enum_boat):
        count=0
        answer=True
        filled_board=False
        enum_value=enum_boat.value
        if enum_boat.name=="S":
           enum_value=3
        while filled_board==False:
            answer=True
            x=self.get_random_x()
            y=self.get_random_y()
            x1=x
            y1=y
            while count<enum_value:
                if self.is_in_range(x1,y1) and self.is_sea(x1,y1):
                    y1=y1+1
                    answer=answer and True
                else:
                    answer=answer and False
                    break
                count=count+1
            if answer==True:
                count=0
                x1=x
                y1=y
                while count<enum_value:
                    if self.is_in_range(x1,y1) and self.is_sea(x1,y1):
                        self.board[y1][x1]=enum_boat.name
                        y1=y1+1
                    count=count+1
                filled_board=True
            else:
                count=0
        return self.board

    def randomly_assign_ships(self):
        self.board=self.put_ships_horizontally(Ships.D)
        self.board=self.put_ships_horizontally(Ships.S)
        self.board=self.put_ships_vertically(Ships.C)
        self.board=self.put_ships_vertically(Ships.B)
        self.board=self.put_ships_vertically(Ships.A)
        return self.board

    def shoot(self,x,y,enemy_board):
        is_repeated=False
        if self.is_sea_with_board(x,y,enemy_board):
            enemy_board[y][x]=self.missed_shoot
            return False,is_repeated
        #If you shoot before, that counts as a failure
        elif enemy_board[y][x] == self.missed_shoot or enemy_board[y][x] == self.successful_shoot:
            is_repeated=True
            return False,is_repeated
        else:
            enemy_board[y][x] = self.successful_shoot
            return True,is_repeated

    def all_sunken_ships(self,enemy_board):
        for y in range(self.rows):
            for x in range(self.columns):
                cell = enemy_board[y][x]
                # If it's not sea or a gunshot, it means there's still a ship out there.
                if cell != SEA and cell != self.successful_shoot  and cell != self.missed_shoot:
                    return False
        # We just went through the whole matrix and did not return on the previous line. Then all the ships have been sunk
        return True
