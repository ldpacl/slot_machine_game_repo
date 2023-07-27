import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

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

def check_winnings(coloumns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = coloumns[0][line]
        for coloumn in coloumns:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings = winnings + values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    coloumns = []
    for _ in range(cols):
        coloumn = []
        current_symbols = all_symbols[:] #making a duplicate of all_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            coloumn.append(value)

        coloumns.append(coloumn)
    return coloumns

def print_slot_machine(coloumns):
    for row in range(len(coloumns[0])):
        for i,coloumn in enumerate(coloumns):
            if i == len(coloumns)-1:
                print(coloumn[row], end=" ")
            else:
                print(coloumn[row], end=" | ")
        print()

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