# TASK 4 - ROCK-PAPER-SCISSORS GAME
import random 

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    while True:
       choice = input("Enter your choice (Rock / Paper/ Scissors) : ").strip().lower()
       if choice in ['rock', 'paper', 'scissors']:
        return choice
       else:
        print ("Invalid choice! Please choose Rock, Paper or Scissors.")

def determine_winner(user, computer):
    user = user.lower()
    computer = computer.lower()
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"
    
def play_game():
   user_score = 0
   computer_score = 0
   round_number = 1
   print ("🎮 WELCOME TO ROCK-PAPER-SCISSORS GAME!")

   while True:
      print (f"\n🔁 Round {round_number}")
      user_choice = get_user_choice()
      computer_choice = get_computer_choice()
      print (f"🧒 You chose : {user_choice.capitalize()}")
      print (f"💻 Computer chose : {computer_choice.capitalize()}")

      result = determine_winner(user_choice, computer_choice)
      if result == "tie":
         print ("🤝 It's a Tie!")
      elif result == "user":
         print ("🎉 You win this round!")
         user_score += 1
      else:
         print ("😞 Computer wins this round!")
         computer_score += 1

      print (f"📊 Score - You : {user_score} | Computer : {computer_score}")
      play_again = input ("Do you want to play another round? (Yes / No) : ").lower()
      if play_again != 'yes':
         print ("\n🏁 Final Score : ")
         print (f"🧒 You : {user_score}")    
         print (f"💻 Computer : {computer_score}")
         print ("Thanks for playing! 🤝")
         break
      round_number += 1

# Run the game 
play_game()     



    