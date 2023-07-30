import random

#You can change these values
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#This decides how many times a symbol can appear in a coloumn
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#These are the points alloted to each symbol
symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#This is for the spin
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet. Your current balance is {balance}")
        else:
            break
    print(f"You bet ${bet} on {lines} lines. Total bet is {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winnings}")
    print(f"You won on lines: ", *winning_lines)

    return winnings - total_bet

#This is the math behind calculating the winnings
def check_winnings(coloumns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines): 
        symbol = coloumns[0][line] 
        for coloumn in coloumns:
            symbol_to_check = coloumn[line] #This takes the first symbol in every row
            if symbol != symbol_to_check:
                break
        else:
            winnings = winnings + values[symbol] * bet #This takes the help of symbol_values dictionary to allocate points
            winning_lines.append(line + 1)
    if winning_lines == []:
        winning_lines = ["None"]
    return winnings, winning_lines

#This gets the symbols ready in all the coloumns for the spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #Using the .items method in dictionaries we get both symbol and the count associated with it
        for _ in range (symbol_count):
            all_symbols.append(symbol) #This prepares the all_symbols list

    coloumns = []
    for _ in range(cols): #This is for every coloumn in the spin. _ is used instead of a variable to save up space 
        coloumn = []
        current_symbols = all_symbols[:] #making a duplicate of all_symbols
        for _ in range(rows): #This is for every row in that particular coloumn
            value = random.choice(current_symbols) #Using random function
            current_symbols.remove(value) #This prevents duplicates
            coloumn.append(value)

        coloumns.append(coloumn) #This adds one coloumn to the nested list "coloumns"
    return coloumns

#Printing the actual slot machine
def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])): #This is because all the coloumns are of the same length
        for i,coloumn in enumerate(coloumns):
            if i == len(coloumns)-1:
                print(coloumn[row], end=" ") #This prints the values of each coloumn in a given row
            else:
                print(coloumn[row], end=" | ")
        print()

#This prompt asks the player for the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input("How many lines do you wanna bet on (" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Lines must be between 0 and "+ str(MAX_LINES) +"!!")
        else:
            print("Enter a number")
    return lines

#This prompt asks the player for the bet amount
def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $$  ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:  
            print("Enter valid amount")
    return bet

#This is the first prompt asking for the deposit
def deposit():
    while True:
        amount = input("What would like to deposit? $$  ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!!")
        else:
            print("Enter valid amount")
    return amount

def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press ENTER to play (q to quit)")
        if answer == "q":
            break
        balance = balance + spin(balance)
    print(f"You left with {balance}")

main()