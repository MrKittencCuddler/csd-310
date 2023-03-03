#imports 
import sys
import mysql.connector
from mysql.connector import errorcode

# connects to database
config={
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#menu
def show_menu():
    print("___Main Menu___\n")
    print("1. View Books\n 2. View Store Locations\n 3. My Accounts\n 4. Exit")
    try:
        choice= int(input('Enter the number of the category you want: '))
        return choice
    except:
        print("\n Invalid input, please try again...")
        sys.exit(0)

#books
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details from book")
    books=cursor.fetchall()
    print("\n __DISPLAYING BOOKS__\n")
    for book in books:
        print("Book Name: {}\n Author: {} \n Details: {} \n".format(book[0], book[1], book[2]))

#location
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale from store")
    locations =cursor.fetchall()
    print("\n __DISPLAYING STORE LOCATIONS__")
    for location in locations:
        print("Locale: {}\n".format(location[1]))

#user
def validate_user():
    try:
        user_id = int(input("\n Enter a customer ID: "))
        if user_id <0 or user_id >3:
            print("\n Invalid ID, please try again... \n")
            sys.exit(0)
        return user_id
    except:
        print("\n Invalid ID, please try again...\n")
        sys.exit(0)

#account
def show_account_menu():
    try:
        print("\n __Account Menu__\n")
        print("1. Wishlist\n 2. Add Book\n 3. Main Menu\n")
        account_choice=int(input("Enter the number for the category: "))
        return account_choice
    except:
        print("\n Invalid input, please try agian...\n")
        sys.exit(0)

#wishlist
def show_wishlist(cursor, user_id):
    cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))

    wishlist = cursor.fetchall()
    print("\n __DISPLAYING WISHLIST__\n")

    for book in wishlist:
        print("Book Name: {} \n Author: {}\n".format(book[4], book[5]))

#books add show
def show_books_to_add(cursor, user_id):
    bookadd=("SELECT book_id, book_name, author, details "
    "FROM book "
    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id ={})".format(user_id))
    print(bookadd)
    cursor.execute(bookadd)
    books_to_add =cursor.fetchall()
    print("\n __Displaying Books Available__\n")
    for book in books_to_add:
        print("Book ID: {}\n Book Name:{}\n".format(book[0], book[1]))

#books add
def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({},{})".format(user_id, book_id))

    #error handling 
try:
    db = mysql.connector.connect(**config) 
    cursor=db.cursor()
    print("\n WhatABook App!")
    user_select=show_menu() #show menu

    #error handling part
    while user_select != 4:
        if user_select==1:
            show_books(cursor)

        if user_select==2:
            show_locations(cursor)

        #user account options
        if user_select==3:
            my_id=validate_user()
            account_choice=show_account_menu()

            while account_choice !=3:

                if account_choice==1:
                    show_wishlist(cursor, my_id)

                if account_choice==2:
                    show_books_to_add(cursor,my_id)
                    book_id=int(input("\n Enter the book id that being added: "))
                    add_book_to_wishlist(cursor, my_id, book_id)
                    db.commit()
                    print("\n Book id: {} was added to your wishlist".format(book_id))

                if account_choice< 0 or account_choice > 3:
                    print("\n Invalid input, please try again...")
                account_choice=show_account_menu()
        
        if user_select< 0 or user_select > 4:
            print("\n Invalid input, please try again...")

        user_select=show_menu()
    print("\n Program ended...")

except mysql.connector.Error as err: 
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect username or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The database does not exist or is not seen")
    else:
        print(err)

finally:
    db.close()
