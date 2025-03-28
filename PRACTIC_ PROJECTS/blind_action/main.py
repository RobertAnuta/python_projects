import os
from art import logo

print(logo)

def clear_console():
    os.system('cls')

action_bidders = {}  

# Function to add the bidder and find the highest Bid
def bid_generator():
    # Define global dictionary with Bidders details
    global action_bidders 
    # Format the name to have 2 or more letters
    while True:        
        name = str(input("What is your name?: "))

        if len(name) >= 2:
            break
        else:
            print("Please type a name with more 2 or more letters")

    # Bid can't be 0 or negative
    while True:             
        bid = int(input("What's your bid?: $"))
        if bid > 0:
            break
        else:
            print("The Bid can't be 0 or negative! ")

    # Add bidder to the dictionary
    action_bidders[name] = bid

    while True:
        additional_bid = str(input("Are there any other bidders? Type Yes or No \n")).lower()
        if additional_bid == "yes" or additional_bid == "no":
            break
        else:
            print("Please make sure you type Yes or No! \n")

    # Additional bidder or end the bid
    if additional_bid == "yes" or additional_bid == "y":
        clear_console()
        bid_generator() 

    elif additional_bid == "no" or additional_bid == "n":
        highest_bid = 0
        bid_winner = {}

        # Find the highes bid
        for value in action_bidders.values():            
            if value > highest_bid:
                highest_bid = value
        # Find the highest Bidder
        for key, value in action_bidders.items():
            if value == highest_bid:
                bid_winner[key] = value


        # If we have 2 equal values ask to increase
        # Loop to check if we have only 1 high value
        if len(bid_winner) > 1:
            equal_bid = True
            while equal_bid:           
                # Sorted values to compare
                listed_values = list(sorted(bid_winner.values()))
                
                for key, value in bid_winner.items():
                    # Condition if the last value is higher then second last
                    if listed_values[-1] > listed_values[-2]:
                        if value == listed_values[-1]:
                            print(f"The highest bidder is {key} with ${value}")
                            equal_bid = False
                    else:
                        print(f"\n{key},")
                        while True:
                            increase_bid = str(input("We have 2 or more bidders with the same bid, would you like to increase the bid? Yes or No\n")).lower()
                            if increase_bid == "yes" or increase_bid == "no":
                                break
                            else:
                                print("Please make sure you type Yes or No! \n")

                        if increase_bid == "yes" or increase_bid == "y":
                            # Loop if the new bid is less or the same with the previes one                        
                            while True:
                                new_bid = int(input("Please enter your new bid: \n"))
                                if value >= new_bid:
                                    print(f"The new bid must be higher then ${value}!\n")
                                else:
                                    bid_winner[key] = new_bid
                                    clear_console()
                                    break
                        elif increase_bid == "no" or increase_bid == "n":
                            bid_winner.pop(key, None)
                            print(f"{key} You have been withdrawn from this auction! \n")   
                            
                        else:
                            equal_bid = False     
        if len(bid_winner) == 1:
            for key, value in bid_winner.items():              
                print(f"The highest bidder is {key} with ${value}")   

    bid_again = str(input("\nWhould you like to bid again? Yes or No\n "))
    
    if bid_again == "yes" or bid_again == "y":
        bid_generator()
        action_bidders = {}    
    else:
        print("Thank you for bidding!\n")

if __name__ == "__main__":
    bid_generator()