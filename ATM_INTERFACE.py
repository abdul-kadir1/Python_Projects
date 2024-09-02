import time

print("Please Enter your CARD...")
time.sleep(4)

password = 1234
pin = int(input("Enter your ATM Pin: "))
balance = 5000
transaction_history = []

if pin == password:
    while True:
        print("""
        1 == Balance
        2 == Withdraw Balance
        3 == Deposit Balance
        4 == Transaction History
        5 == Quit
        """)
        
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if option == 1:
             print("====================================================")
             print(f"Your Current Balance is {balance}")
             print("====================================================")


        elif option == 2:
            withdraw_amount = int(input("Please enter amount to withdraw: "))
            if withdraw_amount <= balance:
                balance =   balance - withdraw_amount
                transaction_history.append(f"Withdrew {withdraw_amount}")

                print("====================================================")
                print(f"Withdrawal successful. Your new balance is {balance}")
                print("====================================================")

            else:
                print("Insufficient balance.")

        elif option == 3:
            deposit_amount = int(input("Please enter amount to deposit: "))
            balance += deposit_amount
            transaction_history.append(f"Deposited {deposit_amount}")
            print("====================================================")
            print(f"Deposit successful. Your new balance is {balance}")
            print("====================================================")

        elif option == 4:
            print("\nTransaction History:")
            if transaction_history:
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
                
        elif option == 5:
            print("====================================================")
            print("Thank you for using the ATM. Goodbye!")
            print("====================================================")

            break

        else:
            print("Invalid option. Please try again.")

else:
    print("Wrong pin. Please try again.")


