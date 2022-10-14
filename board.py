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
   