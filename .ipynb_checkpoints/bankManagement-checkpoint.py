import matplotlib.pyplot as plt

class Customer:
    def __init__(self, name, acc_number, balance):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance
        self.transactions = []

    def deposit(self):
        try:
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            self.balance += amount
            self.transactions.append(("Deposit", amount))
            print(f"\nDeposited ₹{amount}. New Balance: ₹{self.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self):
        try:
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient Balance!")
            self.balance -= amount
            self.transactions.append(("Withdraw", amount))
            print(f"\nWithdrawn ₹{amount}. New Balance: ₹{self.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def check_balance(self):
        print(f"\nAccount Balance: ₹{self.balance}")

    def transfer_funds(self, receiver):
        try:
            amount = float(input("Enter Transfer Amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.balance:
                raise ValueError("Insufficient Balance!")
            self.balance -= amount
            receiver.balance += amount
            self.transactions.append(("Transfer Out", amount))
            receiver.transactions.append(("Transfer In", amount))
            print(f"\nTransferred ₹{amount} to {receiver.name}. Your New Balance: ₹{self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
            

    def plot_balance(self, receiver, amount, stage):
        names = [self.name, receiver.name]
        if stage == "Before Transfer":
            balances_before = [self.balance + amount, receiver.balance - amount]
        else:
            balances_before = [self.balance, receiver.balance]
            

        plt.pie(balances_before, labels=names, colors=['blue', 'green'],autopct="%1.1f%%")
        plt.title(f"Account Balances {stage}")
        plt.show()


    def display_info(self):
        print(" ╒══════════════════════════════════════╕")
        print(f" |  Customer Name : {self.name}                 |")
        print(f" |  Account Number: {self.acc_number}          |")
        print(f" |  Balance       : ₹{self.balance}              |")
        print(" ╘══════════════════════════════════════╛")
class Loan:
    loan_types = {
        "Home Loan": 10.5,
        "Car Loan": 13.0,
        "Personal Loan": 15.5,
        "Education Loan": 14.0,
        "Business Loan": 17.0,
        "Credit-Card Loan": 12.5
    }

    def __init__(self, loan_type, amount):
        self.loan_type = loan_type
        self.amount = amount
        self.interest_rate = Loan.loan_types.get(loan_type, 0)
        self.interest_amount = self.calculate_interest()
        self.total_amount = self.amount + self.interest_amount
        
    def calculate_interest(self):
        return (self.amount * self.interest_rate) / 100

    def display_loan_details(self):
        print("╔═══════════════════════════════════════════")
        print(f"║             Loan Details:                ")
        print(f"║ Loan Type: {self.loan_type}                     ")
        print(f"║ Loan Amount: ₹{self.amount:.2f}                      ")
        print(f"║ Interest Rate: {self.interest_rate}%                     ")
        print(f"║ Interest Amount: ₹{self.interest_amount:.2f}                   ")
        print(f"║ Total Amount Payable: ₹{self.total_amount:.2f}             ")
        print("╚═══════════════════════════════════════════")


def plot_loan_distribution():
    labels = list(Loan.loan_types.keys())
    rates = list(Loan.loan_types.values())

    plt.pie(rates, labels=labels, autopct='%1.1f%%')
    plt.title("Loan Interest Rate Distribution")
    plt.axis('equal')
    plt.show()

def main():
    customers = {}
    sender_acc = None
    receiver_acc = None

    while True:
        print("╔═══════════════════════════════════════════╗")
        print("║   1. Create Account                       ║")
        print("║   2. Delete Account                       ║")
        print("║   3. Select Loan                          ║")
        print("║   4. Deposit Money                        ║")
        print("║   5. Withdraw Money                       ║")
        print("║   6. Check Balance                        ║")
        print("║   7. Transfer Funds                       ║")
        print("║   8. View Loan Interest Rates Graph       ║")
        print("║   9. Plot Balance (Before/After Transfer) ║")
        print("║   10. Exit                                ║")
        print("╚═══════════════════════════════════════════╝")
        choice = input("Select an option: ")

        if choice == "1":
            try:
                name = input("Enter Customer Name: ")
                if not name.isalpha():
                    raise ValueError("Name must contain only letters.")
                print(f"Welcome, {name}!")

                acc_number = input("Enter Account Number: ")
                if not acc_number.isdigit():
                    raise ValueError("Account number must contain only digits.")
                if len(acc_number) != 10:
                    raise ValueError("Account number must be exactly 10 digits.")
                print(f"Account Number: {acc_number}")

                balance = float(input("Enter Account Balance: "))
                if balance < 0:
                    raise ValueError("Account balance cannot be negative.")
                print(f"Account Balance: ₹{balance}")

                customers[acc_number] = Customer(name, acc_number, balance)
                print("\nAccount Created Successfully!")
            except ValueError as e:
                print(f"Error: {e}")
                break

        elif choice == "2":
            try:
                acc_number = input("Enter Account Number: ")
                if acc_number not in customers:
                    raise KeyError("Account Not Found!")
        
                del customers[acc_number]
                print("\nAccount Deleted Successfully!")

            except KeyError as e:
                print(f"\nError: {e}")
                break
            except Exception as e:
                print(f"\nUnexpected Error: {e}")
                break

        elif choice == "3":
            acc_number = input("Enter Account Number: ")
            if acc_number in customers:
                print("\nAvailable Loan Types:")
                for loan_type in Loan.loan_types.keys():
                    print(f"- {loan_type} ({Loan.loan_types[loan_type]}% interest)")

                selected_loan = input("Enter Loan Type: ")
                try:
                    amount = float(input("Enter Loan Amount: "))
                    loan = Loan(selected_loan, amount)
                    loan.display_loan_details()
                except ValueError as e:
                    print(f"Error: {e}")
                    break
            else:
                print("\nAccount Not Found!")

        elif choice == "4":
            try:
                acc_number = input("Enter Account Number: ")
                if acc_number not in customers:
                    raise KeyError("Account Not Found!")

                customers[acc_number].deposit()

            except KeyError as e:
                print(f"\nError: {e}")
                break
            except ValueError as e:
                print(f"\nError: {e}")
                break
            except Exception as e:
                print(f"\nUnexpected Error: {e}")
                break


        elif choice == "5":
            try:
                acc_number = input("Enter Account Number: ")
                if acc_number not in customers:
                    raise KeyError("Account Not Found!")

                customers[acc_number].withdraw()

            except KeyError as e:
                print(f"\nError: {e}")
                break
            except ValueError as e:
                print(f"\nError: {e}")
                break
            except Exception as e:
                print(f"\nUnexpected Error: {e}")
                break

        elif choice == "6":
            try:
                acc_number = input("Enter Account Number: ")
                if acc_number not in customers:
                    raise KeyError("Account Not Found!")
        
                customers[acc_number].display_info()
            except KeyError as e:
                print(f"\nError: {e}")
                break
            except Exception as e:
                print(f"\nUnexpected Error: {e}")
                break


        elif choice == "7":
            try:
                sender_acc = input("Enter Your Account Number: ")
                receiver_acc = input("Enter Receiver's Account Number: ")

                if not sender_acc.isdigit() or not receiver_acc.isdigit():
                    raise ValueError("Both account numbers must contain only digits.")
    
                if sender_acc == receiver_acc:
                    raise ValueError("Sender and receiver account numbers cannot be the same.")
    
                if len(sender_acc) != 10 or len(receiver_acc) != 10:
                    raise ValueError("Both account numbers must be exactly 10 digits long.")
    
                print(f"Sender Account Number: {sender_acc}")
                print(f"Receiver Account Number: {receiver_acc}")

            except ValueError as e:
                print(f"Error: {e}")
                break

            if sender_acc in customers and receiver_acc in customers:
                customers[sender_acc].transfer_funds(customers[receiver_acc])
            else:
                print("\nOne or both accounts not found!")

        elif choice == "8":
            plot_loan_distribution()

        elif choice == "9":
            sender_acc = input("Enter Sender Account Number: ")
            receiver_acc = input("Enter Receiver Account Number: ")
            amount = float(input("Enter Transfer Amount: ₹"))
            stage = input("Enter 'before' to plot before transfer or 'after' for after transfer: ").strip().lower()

            if sender_acc in customers and receiver_acc in customers:
                sender = customers[sender_acc]
                receiver = customers[receiver_acc]
                if stage == 'before':
                    sender.plot_balance(receiver, amount, "Before Transfer")
                elif stage == 'after':
                    sender.plot_balance(receiver, amount, "After Transfer")
                else:
                    print("Invalid input for balance stage.")
            else:
                print("\nOne or both accounts not found!")

        elif choice == "10":
            print("\nThank you for using Bank Management System!")
            break

        else:
            print("\nInvalid Option! Try Again.")

if __name__ == "__main__":
    main()
