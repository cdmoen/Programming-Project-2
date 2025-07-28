#!

# Colin Moen
# 7/27/25
# Dev 108 11226 SU25
# Programming Project 2

import random


# Function to determine if user input is a number, while also allowing for common typed-out numbers
def not_number(phrase: str) -> bool:
    spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 
               'twelve', 'rteen','fteen','xteen','nteen','hteen','neteen','twenty','thirty','forty','fifty',
               'sixty','seventy','eighty','ninety','hundred', 'thousand', 'illion',]
    for item in spelled_numbers:
        if item in phrase:  # If it contains a spelled-out number, it's a number
            return False
    if phrase.isnumeric():  # If it contains digits, it's a number
        return False
    else:
        return True  # True = NOT a number

# Function to get words from the user. Uses random.choice to
# mix up the input so that the player can play multiple times and not know
# the result.
def get_word_input(word_list):
    word_indices = list(range(len(word_list)))  # creates a temporary numeric list for randomization [0,1,2 etc...]
    for i in range(0, len(word_indices)):    
        index = random.choice(word_indices)  #  pick a random index in the list
        while True:
            word = input(f"give me {word_list[index][0]}:  ")  # matches the index to the word list for the story
            if word.isnumeric():
                print(f"Not a number, silly! {word_list[index][0]}!  ")  # screen for invalid number input
                continue
            else:
                word_list[index][1] = word  # User's input is stored in the word list
                break
        word_indices.remove(index)  # remove the index that was just used, so it can't be picked twice 

# Function to get number input from user. Works very similarly to get_word_input()
def get_num_input(number_list):
        num_indices = list(range(len(number_list)))  # Creates temporary numeric list 
        for i in range(0, len(num_indices)):
            index = random.choice(num_indices)   # picks random index in the list
            while True:
                num = input(f"give me a {number_list[index][0]}:   ")
                if not_number(num):
                    print("please enter a number:  ")   # screens for number
                    continue
                else:
                    number_list[index][1] = num   # adds number to the story
                    num_indices.remove(index)     # and removes index from temp. list
                    break
            
# Function to do the first MadLib.  word_list for each story is hard-coded, takes different inputs
def begin_story_1():
    word_list = [
        ["a noun", ''], ["an adjective", ""], ["a verb", ""], ["a plural noun", ""], ["a noun", ""],
        ["a verb", ""], ["an adjective", ""], ["a noun", ""], ["a verb", ""], ["a plural noun", ""]
    ]  # each 'child' list inside this parent list has 2 indices: 0 is for the word type, 1 is to store the user's input

    get_word_input(word_list)  # get all the words from the user

    print(  # print out the story using f strings.
f"""
        BILL'S FIRST DRAFT
          
"Shall I compare thee to a {word_list[0][1]}?
Thou art more lovely and more {word_list[1][1]}:
Rough winds do {word_list[2][1]} the {word_list[3][1]} of May,
And summer's lease hath all too short a date:
Sometime too hot the {word_list[4][1]} of heaven {word_list[5][1]},
And often is his gold dimm'd;
And every fair from fair sometime declines,
By chance or nature's {word_list[6][1]} course untrimm'd;
But thy eternal {word_list[7][1]} shall not fade
Nor lose possession of that fair thou ow'st;
Nor shall Death brag thou wander'st in his shade,
When in eternal lines to time thou grow'st:
So long as men can {word_list[8][1]} or {word_list[9][1]} can see,
So long lives this, and this gives life to thee."
""")

 # Function for the second MadLib.  Works essentially the same, except it also takes number input
def begin_story_2():

    word_list = [  # word list is hard-coded, tailored to this particular story
        ["an emotion", ""], ["a verb", ""],["a plural noun", ""],["an adjective", ""],
        ["a verb ending with '-ing'", ""],["a unit of time", ""],["an animal", ""],
        ["a plural food item", ""]
        ]
    number_list = [["number", ""], ["number", ""]]  # List for the 2 number inputs for this story
    
    get_word_input(word_list)  # Get words from user
    get_num_input(number_list)  # Get numbers from user
    
    print(  # Print the story
f"""
                            A VERY STRANGE CAMPING TRIP
"This weekend I am going camping with my cousin Jake. I packed my lantern, sleeping bag, and a bag of trail mix. 
I am so {word_list[0][1]} to {word_list[1][1]} in a tent. Last year we saw {number_list[0][1]} {word_list[2][1]}! 
I have heard that the {word_list[3][1]} lake is great for {word_list[4][1]}. Then we will hike through the forest 
for {number_list[1][1]} {word_list[5][1]}s. If I see a {word_list[6][1]} while hiking, I am going to bring it home 
as a pet! At night we will tell creepy ghost stories and roast {word_list[7][1]} around the campfire!!"
""")

def main():
    play_again = True  # Set initial boolean for repeat play-throughs
    counter = 0  # Initialize counter to track how many stories have been created
    print("Welcome to the MadLibs story generator!")  # Greet user, get name.
    player_name = input("What is your name?  ")
    print(f"Hello, {player_name}!  Glad to have you.\nI have two MadLibs to pick from today:")

    while True:
        if play_again == False:   # Before starting, check if user tried to exit.
            break
        while True:
            try:  # Display options for two stories and get selection from user
                print("\n1. Shakespeare's Silliest Sonnet\n2. A Very Strange Camping Trip\n")
                selection = int(input("Which would you like to do? (Enter 1 or 2):  "))
                if selection == 1:
                    begin_story_1()  # start story 1, if selected
                    break
                elif selection == 2:
                    begin_story_2()  # start story 2, if selected
                    break
                else:
                    print("Please select 1 or 2")  # screen for invalid numeric input
            except ValueError:  # screen for invalid strings
                print("Please select 1 or 2")
        
        counter += 1
        if counter == 1:
            print(f"You've created 1 story!\n")
        else:
            print(f"You've created {counter} stories!\n")
        while True:  # Ask if user wants to play again
            go_again = input("Would you like to do another? (y/n)   ")
            if go_again.lower() == "y":  # Boolean remains true, back to main menu
                play_again = True
                break
            elif go_again.lower() == "n":  # Boolean set to False, program ends
                play_again = False
                break
            else:
                print("Please enter y or n")
    print("Thanks for playing!\nGoodbye!")  # Farewell message

if __name__ == "__main__":
    main()