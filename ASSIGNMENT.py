import datetime
import os

MAX = 100
NOTES_ID = 0  # Define first notes id
NOTES_ARY = [""] * MAX  # Define notes array
NOTES_TITLE_ARY = [" "] * MAX  # Define notes title function array


def display_welcome():
    print("Welcome to Notes Organizer")
    print()
    display_menu()  # Display menu here


def display_menu():
    print("COMMAND MENU")
    print("add   -  ADD  NOTE")
    print("view  -  VIEW NOTE")
    print("edit  -  EDIT NOTE")
    print("del   -  DELETE NOTE")
    print("cls   - !CLEAR ALL NOTE!")
    print("exit  -  EXIT PROGRAM")
    print()


def add_function():
    def add_display():
        print("ADD FUNCTION")
        print("1  -  ADD")
        print("2  -  RETURN")
        choose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
        if choose == "1":
            add_notes()
        elif choose == "2":
            clear()
            main()
        else:
            clear()
            print("NOT AVAILABLE INPUT")
            main()

    def add_notes():
        global NOTES_ID  # Allow NOTES_ID can be appended
        if NOTES_ID < MAX:  # If notes quantity didn't reach maximum = 100
            title = input("Please enter your notes title:\n")  # Notes title
            NOTES_TITLE_ARY[NOTES_ID] = title
            notes = input("Please enter your notes:\n")  # Notes
            NOTES_ARY[NOTES_ID] = notes
            NOTES_ID += 1
            clear()
            print("NOTES ADD SUCCESSFUL")
            add_display()
        else:
            clear()
            print("NOTES QUANTITY REACH LIMIT(100)")
            add_display()

    add_display()


def view_function():
    global NOTES_ID
    print("VIEW FUNCTION  -  NOTE LIST")
    print("ID NOTE-TITLE")
    for i in range(NOTES_ID):
        print(f"{i} {""} {NOTES_TITLE_ARY[i]}")
        view_notes()

def view_notes():
    ID_INPUT = input("ENTER NOTE ID: ")
    print("NOTES:")
    print(NOTES_ARY[int(ID_INPUT)])

def edit_function():
    print("EDIT FUNCTION")


def exit_function():
    exit()  # Quit() in Jupyter Notebook, Exit() in .py / Stop() to stop cell input running


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    display_welcome()
    while True:
        command = input("Command: ").lower()  # User imput command
        if command == "add":
            add_function()

        elif command == "view":
            view_function()

        elif command == "edit":
            edit_function()

        elif command == "exit":
            exit_function()

        else:
            print("WRONG COMMAND!")
            clear()


main()
