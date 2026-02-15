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
    print(f"There are {sticks_total} stick(s) left.")
    print(current_player)
    sticks_taken = int(input("How many sticks do you want? "))
    while sticks_taken > sticks_max or sticks_taken < sticks_min or sticks_taken > sticks_total:
        print(f"You can't take {sticks_taken} sticks")
        sticks_taken = int(input("How many sticks do you want? "))
    sticks_total -= sticks_taken
    if sticks_total > 0:
        if current_player == "Player One":
            current_player = "Player Two"
        else:
            current_player = "Player One"
    else:
        print(f"{current_player} wins!")
        print("Press the enter key to quit. ")
        input()
        break
    current_player = "Player Two"
