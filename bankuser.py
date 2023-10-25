import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


# table Create
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user
    (
        "User_name" TEXT,
        "Contact_number" INTEGER,
        "Email" TEXT,
        "Address" TEXT,
        "Cash" INTEGER
    )
''')

conn.commit()
def account(user_name, contact_number, email, address):
    cursor.execute("INSERT INTO user('User_name', 'Contact_number', 'Email', 'Address') VALUES (?, ?, ?, ?)", (user_name, contact_number, email, address))
    conn.commit()

    
def withdrawcash(user_name, withdraw_cash):  
    cursor.execute("SELECT Cash FROM user WHERE User_name = ?", (user_name,))
    old_balance = cursor.fetchone()[0]
    new_balance = old_balance - withdraw_cash
    if new_balance >= 0:
        cursor.execute("UPDATE user SET Cash = ? WHERE User_name = ?", (new_balance, user_name))
        conn.commit()
    return new_balance


def depositcash(user_name, cash):
    cursor.execute("SELECT Cash FROM user WHERE User_name = ?", (user_name,))
    old_balance = cursor.fetchone()[0]
    new_balance = old_balance + cash
    cursor.execute("UPDATE user SET Cash = ? WHERE User_name = ?", (new_balance, user_name))

    conn.commit()
    return new_balance


def bank():
 while True:
     print("Enter 1 for create a account : ")
     print("Enter 2 for check the balance : ")
     print("Enter 3 withraw the cash : ")
     print("Enter 4 for deposit the cash : ")
     print("5 Exit")
     choice = input("Enter your choice :")

     if choice == "1":
         print("Create Account")
         user_name = input("Enter the name : ")
         contact_number = int(input("Enter the Contact_number : "))
         email = input("Enter the Email : ")
         address = input("Enter the Address : ")
         print("all your datails have been save successfully")

    

     # Add your create account logic here
     elif choice == "2":
         print("Check Balance")
         user_name = input("Enter your user name : ")
         balance = balancecheck(user_name)
         print("Your balance:", balance) # yaha pr kya ayega)
         
        
        
        
     # Add your check balance logic here
     elif choice == "3":
         print("Withdraw Cash")
         user_name = input("Enter the name : ")
         withdraw_cash = int(input("Enter the cash : "))
         new_balance = withdrawcash(user_name, withdraw_cash)
         print("you are balabce is available", new_balance)
         if new_balance >= 0:
             print("Your balance is available", new_balance)
         else:
             print("Your balance is not available")
  


            

        
     # Add your withdraw cash logic here
     elif choice == "4":
         print("Deposit Cash")
         user_name = input("Enter the name : ")
         cash = int(input("Enter the cash : "))
         new_balance = depositcash(user_name, cash)
         print("your cash is successfully save : ")
        
         
        
     # Add your deposit cash logic here
     elif choice == "5":
         print("Good bye")
         break



bank()
conn.close()
