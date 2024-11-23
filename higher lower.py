import random

# def get_numbers():
#  user_num=random.randint(1,100)
#  computer_num=random.randint(1,100)
   
def game(guess):
    if guess=="higher" and user_num > computer_num:
     return True
    elif guess=="lower" and user_num > computer_num:
     return False   
    elif guess=="higher" and user_num < computer_num:
     return False
    elif guess=="lower" and user_num < computer_num:
     return True
    elif guess=="lower" and user_num==computer_num:
     return True 
    elif guess=="higher" and user_num==computer_num:
     return False
    else:
     return False

def getUserGuess():
    while True:
         guess= input("Do you think your number is higher or lower than the computer's?")
         if guess != "lower" and guess != "higher":
            print ("Re-enter your choice")
            continue
         else:
            break
    return guess
   
        
number_of_rounds=10
score=0


def final_msg ():
   final_msg = "I loved playing with you."
   print(f"""You did well, today.
{final_msg}, Thanks.""")


index=0
for rounds in range(1,number_of_rounds,+1):
    index=index+1
    user_num=random.randint(1,100)
    computer_num=random.randint(1,100)
    print(f"Round {index}")
    print(f"Your number is {user_num}")
    guess=getUserGuess()
   
    result=game(guess)
    if result:
        print(f"You were right! The computer's number was {computer_num}")
        score+=1
        print(f"Your score is now {score}")
    else:
        print(f"Oh,You were wrong! The computer's number was {computer_num}")
        score-=1
        print(f"Your score is now {score}")

    final_msg ()
        
    
    
    
        
