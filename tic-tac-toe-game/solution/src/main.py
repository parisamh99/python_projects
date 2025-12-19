import random
class Tictactoe:

    def __init__(self,):
        self.board = [' '] * 10
        self.player_turn = self.first_random_player()

    def first_random_player(self):
        return random.choice(['X','O'])


    def show_board(self):
        print('\n')
        print(self.board[1] + '|' + self.board[2] + '|' + self.board[3])
        print('-----')
        print(self.board[4] + '|' + self.board[5] + '|' + self.board[6]) 
        print('-----')
        print(self.board[7] + '|' + self.board[8] + '|' + self.board[9]) 
        print('\n')


    def swap_player_turn(self):
        if self.player_turn == 'X' :
            self.player_turn = 'O'
        else:
            self.player_turn = 'X'
        
    def fix_spot(self,cell,player):
        self.board[cell] = player

    def is_board_filled(self):
        return ' ' not in self.board[1:] 

    def who_won(self,player):
        win_combination = [
            (1,2,3),(4,5,6),(7,8,9),
            (1,4,7),(2,5,8),(3,6,9),
            (1,5,9),(3,5,7)
        ]   
        for comb in win_combination:
            if all(self.board[cell] == player for cell in comb):
                return True
        return False
        
    def start(self):
        while True:
            self.show_board()
            print(f"player {self.player_turn}'s turn")
            cell = int(input("please enter a number between 1 to 10: ")) 
            if self.board[cell] == ' ' and cell in range(1,10):
                self.fix_spot(cell, self.player_turn) 

                if self.who_won(self.player_turn):
                    self.show_board()
                    print(f'player {self.player_turn} won')
                    break

                if self.is_board_filled():
                    print("Draw")
                    break

                self.swap_player_turn() 
                
            else:
                print('cell already occupied')

                    

if __name__ == '__main__':
    game = Tictactoe()
    game.start()