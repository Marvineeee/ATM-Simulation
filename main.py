balance = 0
cash = 200

def main(balance, cash):
    name = str(input("Hello, Welcome Too ETX Banking!\n Enter User Name: ")).strip().capitalize()
    print("Thank you for banking with ETX, ", name)
    _bank_menu(balance, cash)


def _bank_menu(balance, cash):
    menu = str(input("Display, Deposit, Withdraw, Exit: ")).strip().lower()


    match menu:
        case "deposit":
            amount = int(input("Deposit Amount: "))
            deposit(amount, balance, cash)
        case "withdraw":
            amount = int(input("Withdraw Amount: "))
            withdraw(amount, balance, cash)
        case "display":
            _balance_displayed = display(balance)
            print("Bank Balance: ", _balance_displayed)
            _bank_menu(balance, cash)
        case _:
            print("Exiting System")

def deposit(amount, balance, cash):
    if amount <= cash:
        print("Sufficent Amount")
        cash = cash - amount
        balance = balance + amount
        
        print("Cash InHands: ", cash)
        print("Bank Balance: ", balance)
        _bank_menu(balance, cash)
    else:
        print("Insufficent Amount, Try Again!")
        _bank_menu(balance, cash)

def withdraw(amount, balance, cash):
    if amount <= balance:
        balance = balance - amount
        cash = cash + amount
        print("Cash InHands: ", cash)
        print("Bank Balance: ", balance)
        _bank_menu(balance, cash)
    else:
        print("Took Out More Than You Have, Try Again!")
        _bank_menu(balance, cash)

def display(balance):
    return balance

main(balance, cash)