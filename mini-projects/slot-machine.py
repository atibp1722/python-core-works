import random

max_lines=3
max_bet_amt=100
min_bet_amt=1

rows=3
cols=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def slotMachineSpin(rows, cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def printSlotMachine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amt=input("Enter amount to deposit: ")
        if amt.isdigit():
            amt=int(amt)
            if amt>0:
                break
            else:
                print("Amount cannot be 0")
        else:
            print("Enter a valid positive number")
    return amt

def getNumberOfLines():
    while True:
        lines=input("Enter number of lines to bet (1-"+str(max_lines)+")?: ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Enter a valid positive number")
    return lines

def getBet():
    while True:
        amt=input("Enter amount to bet: ")
        if amt.isdigit():
            amt=int(amt)
            if min_bet_amt <= amt <= max_bet_amt:
                break
            else:
                print(f"Bet amount must be {min_bet_amt}-{max_bet_amt}")
        else:
            print("Enter a valid positive number")
    return amt

def checkForWin(columns, lines, bet, value):
    amt_won=0
    win_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            amt_won+=value[symbol]*bet
            win_line.append(line+1)
    return amt_won, win_line

def playGame(balance):
    line=getNumberOfLines()
    while True:
        bet=getBet()
        total_bet=bet*line
        if total_bet>balance:
            print("Not enough amount to bet, current balance is",balance)
        else:
            break
    print(f"You bet on {line} lines. Amount to bet {bet} total bet amount is {total_bet}")
    slots=slotMachineSpin(rows, cols, symbol_count)
    printSlotMachine(slots)
    won,won_line=checkForWin(slots, line, bet, symbol_value)
    print(f"You won: {won}")
    print(f"You won on lines:",*won_line)
    return won-total_bet

def main():
    balance=deposit()
    while True:
        print(f"Current balance: {balance}")
        play=input("Hit (enter) to play slot machine game OR (q) to quit: ")
        if play=='q':
            break
        balance+=playGame(balance)
    print(f"You left the game with {balance}")
main()