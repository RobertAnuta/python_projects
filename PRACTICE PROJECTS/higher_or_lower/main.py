''' Famouse game Higher and Lower where you have to compare the number of followers in this example between 2 accounts'''


from art import *

from game_data import data

from random import choice


def low_high():
    print(logo)
    # define the {data_1} and {data_2} with random values from data
    data_1 = choice(data)
    data_2 = choice(data)
    if data_1 == data_2:
        data_2 = choice(data)
    score = 0
    game_on = True

    # Game on Loop
    while game_on:
        # structure the message to show using the data
        print(
            f"{data_1['name']} \nhas \n{data_1['follower_count']} followers \n{data_1['description']} from {data_1['country']}"
        )
        print(vs)
        print(f"{data_2['name']} \nhas")
    
        # ask the user to choose between the 2 with "lower" or "higher"
        while True:
            use_choice = input(f"HIGHER or LOWER number of followers then {data_1['name']}?  ").lower()
            if use_choice == "higher" or use_choice == "lower":
                break
            else:
                print("Please enter type HIGHER or LOWER!")
            # compare the 2 data and return the result
    
        if use_choice == "higher":
            if data_1['follower_count'] < data_2['follower_count']:
                score += 1   
                print(f"Correct! Your score is {score}!")
            else:
                print("You LOST! That was a good try!")
                print(f"Your score is {score}!")
                
                game_on = False
        elif use_choice == "lower":
            if data_1['follower_count'] > data_2['follower_count']:
                score += 1
                print(f"Correct! Your score is {score}!")
            else:
                print("You LOST! That was a good try!")
                print(f"Your score is {score}!")
                game_on = False

        # if the user choose the right answer, then the {data_1} becomes {data_2}
        data_1 = data_2
        data_2 = choice(data)  
    
    while True:
        if input("Would you like to play again? Y or N  ").lower() == "y":
            low_high()
        else:
           break


if __name__ == "__main__": 
    low_high()
