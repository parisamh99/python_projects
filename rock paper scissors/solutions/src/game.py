"""author:parisa mahmoodnia
   date:5/10/2025
   description:rock paper scissors game
"""

import random
from typing import List,Tuple

class RockPaperScissors():
  """main class for rock paper scissors game"""
  def __init__(self):
    self.choices:List[str] = ["rock","paper","scissors"]
   

  def get_user_choice(self):
        user_choice:str = input(f"give me your choice {self.choices}")
        if user_choice.lower() in self.choices:
            return user_choice
        else:
            print(f"your choice is out of the range you have to choose from {self.choices}")  
            return self.get_user_choice()

  def get_computer_choice(self):
       """get computer choice randomly from choices:rock,paper,scissors"""
       computer_choice = random.choice(self.choices)
       return computer_choice
    
  def decide_winner(self,user_choice:str,computer_choice:str) -> str:
       """decide the winner of the game based on the user and computer choices
       :param user_choice : the choice of the user
       :param computer_choice : the choice of the computer
       :return: the result of the game(who win)    
       """
       if user_choice == computer_choice:
          return "you are tie"
       win_combinations = [('rock','scissors'),('paper','rock'),('scissors','paper')]
       for win_com in win_combinations:
          if win_com[0] == user_choice and win_com[1] == computer_choice:
             print(computer_choice)
             return "congratulations!! user win"
       else:
            return "oh sorry:( computer win"
             
  def play(self):
        """ paly the game
        - get the user_choice
        - get the computer_choice
        - decide the winner
        - print the result
        """
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        print("user_choice", user_choice)
        print("computer_choice", computer_choice)
        print(self.decide_winner(user_choice,computer_choice))



if __name__ == '__main__':
  game = RockPaperScissors()
  while True:
   game.play()
   continue_game = input("do you want to play again?if you want to play type any word and if you want to quit type q/Q.")
   if continue_game == 'q' or 'Q':
       break

