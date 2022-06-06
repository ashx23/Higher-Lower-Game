from game_data import data
import random
from art import logo, vs
from replit import clear

def format_data(com_data):
  account_name = com_data["name"]
  account_descr = com_data["description"]
  account_country = com_data["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, followers1, followers2):
  if followers1 > followers2:
    return guess == "a"
  else:
    return guess == "b"
  
#Display Art.
print(logo)
score = 0
game_should_con = True
com_data2 = random.choice(data)

while game_should_con:
  #show two random names. 
  
  com_data1 = com_data2
  
  if com_data1 == com_data2:
    com_data2 = random.choice(data)
  
  print(f"Compare A: {format_data(com_data1)}.")
  
  print(vs)
  
  print(f"Against B: {format_data(com_data2)}.")
  
  #Check the user data. 
  guess = input("Who has more followers? Type 'A' or 'B' : ").lower()
  
  #Get follower count of each account.
  follower_count_1 = com_data1["follower_count"]
  follower_count_2 = com_data2["follower_count"]
  
  is_correct = check_answer(guess, follower_count_1, follower_count_2)
  
  clear()
  print(logo)
  #Score keeping.
  if is_correct:
    score += 1
    print(f"Your are right! Current score : {score}")
  else:
    game_should_con = False
    print(f"Sorry, that's wrong. Final score : {score}")
  
  #Repeat