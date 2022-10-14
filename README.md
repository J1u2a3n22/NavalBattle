# NAVAL BATTLE🚀

![Battleship_game_board](https://user-images.githubusercontent.com/110042249/195958617-3cce4b6b-21fb-42c0-889a-ee2f5cf7dbc1.svg)


## NAME 📋
* Canedo Villarroe Juan Luis

## IMPORTANT! HOW TO USE 🔧
* After cloning the repository enter the folder, open a git bash and put the following command: git checkout master, with           this command you will be able to see all the files 
* For the correct functioning of the code you first need to install "colorama" from the console with the following command:                   
             -python -m pip install colorama 
* Insert the command 'python battleshipUI.py' to start the program.
* The program initially displays a menu with two options where if you select the option play, it shows a form where we are asked to enter the two names of the players, after inserting these two names, for test mode, it shows the board of both with the position of their ships in order to verify the correct operation of the program.
If you want to disable this function you can comment 
             -line 134 of the battleshipUI.py class.

## DESCRIPTION ⚙️
The Board
Each board contains a 10 x 10 grid. The horizontal axis is labeled with letters A through J, and the vertical axis is numbered 1 through 10.

Conditions  
* Coordinates: Action to choose a square with letter and number.

* Empty square: It is the representation of water on the board.
* Successful shot: The correct coordinate is mentioned, it means that we hit your ship and it must be marked on the screen, if it is "Sunk" if all the squares of the ship have already been hit. A red marker will be placed.
* Ships: Each player will have 5 ships, an aircraft carrier (five boxes), a battleship (four boxes), a cruiser (three boxes), a submarine (three boxes) and a destroyer (two boxes).

Rules
* Each player has one turn
* The game is won when all ships are sunk.
* The game is not considered a draw
