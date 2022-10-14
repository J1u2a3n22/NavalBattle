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
