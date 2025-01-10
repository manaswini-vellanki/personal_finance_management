from user import User
from transaction import Transaction
from budget import Budget


# creating the class for the required app
class PersonalFinanceApp:
    def __init__(self):
        User.initialize_database()
        self.current_user = None

    # run() function to run the application for tracking and registerng users
    def run(self):
        """Run the application."""
        print("Welcome to the Personal Finance Management Application!")
        while True:
            print("\nMenu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            # register user if choice is 1
            if choice == "1":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username)
                user.register(password)

            # login user if choice is 2
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                user = User(username)
                if user.login(password):
                    self.current_user = user
                    self.user_menu()

            # exit the application if choice is 3
            elif choice == "3":
                print("Thank you!")
                break

            else:
                print("Invalid choice. Please try again.")

    # user_menu() function to display the actions or services provided by the app after login
    def user_menu(self):
        """Display the user menu after login."""
        transaction = Transaction(self.current_user.user_id)
        budget = Budget(self.current_user.user_id)

        while True:
            print("\nUser Menu:")
            print("1. Add Transaction")
            print("2. Generate Report")
            print("3. Set Budget")
            print("4. Check Budget")
            print("5. Logout")
            choice = input("Choose an option: ")

            # if choice is 1 . the tansaction is added by taking the required amount and category as input
            if choice == "1":
                type = input("Enter type (income/expense): ").lower()
                category = input("Enter category: ")
                amount = float(input("Enter amount: "))
                transaction.add_transaction(type, category, amount)

            # if choice is 2, the report is generated by taking the required year and month as input
            elif choice == "2":
                year = input("Enter year: ")
                month = input("Enter month (or press Enter for all months): ")
                transaction.generate_report(year, month)

            # if choice is 3, the app will set the budget for the specific category
            elif choice == "3":
                category = input("Enter category: ")
                amount = float(input("Enter budget amount: "))
                budget.set_budget(category, amount)
                
            # if choice is 4, the app will check the budget for the specific category
            elif choice == "4":
                category = input("Enter category: ")
                budget.check_budget(category)

            # if choice is 5, the user will log out and the app will close
            elif choice == "5":
                print("Logging out...")
                self.current_user = None
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = PersonalFinanceApp()
    app.run()