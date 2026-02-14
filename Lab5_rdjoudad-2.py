"""
Pick Up Sticks Game In Python
Ryma Djoudad
Start with 13 sticks, players alternate trying to remove sticks, player who picks up the last stick wins
No starter code 
2/14/2026
"""
sticks_max = 4
sticks_min = 1
sticks_total = 13
current_player = "Player One"
sticks_in_pile = True

print("Welcome to the Pick Up Sticks game!")
print("There is a pile of 13 sticks presented to you.")
print("You'll be able to pick up sticks, up to 4 at a time!")
print("The player who picks up the last stick wins, good luck!")

while sticks_in_pile:
    sticks_taken = int(input("How many sticks do you want? "))
    while sticks_taken > sticks_max or sticks_taken < sticks_min:
        print("That number of sticks is invalid!")
        sticks_taken = int(input("How many sticks do you want? "))
    
    sticks_total -= sticks_taken
