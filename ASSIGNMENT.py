import datetime
import os

MAX = 100
NOTES = 0  # Define first notes id
notes_ary = [""] * MAX  # Define notes array
notes_title = [""] * MAX  # Define notes title function array
notes_time = [""] * MAX  # Define notes time function array

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
        global NOTES  # Allow NOTES_ID can be appended
        if NOTES < MAX:  # If notes quantity didn't reach maximum = 100
            title = input("Please enter your notes title:\n")  # Notes title
            notes_title[NOTES] = title
            notes = input("Please enter your notes:\n")  # Notes
            notes_ary[NOTES] = notes
            time = datetime.datetime.now().strftime("%D-%H:%M:%S")
            notes_time[NOTES] = time
            NOTES += 1
            clear()
            print("NOTES ADD SUCCESSFUL")
            add_display()

        else:
            clear()
            print("NOTES QUANTITY REACH LIMIT(100)")
            add_display()

    add_display()

def view_function():
    global NOTES
    print("VIEW FUNCTION")
    display_list()
    print("CHOOSE:")
    print("1  -  VIEW NOTE")
    print("2  -  RETURN")
    view_choose = input("\nPLEASE ENTER YOUR CHOOSE[1/2]:")
    if view_choose == "1":
        clear()
        view_notes()

    elif view_choose == "2":
        clear()
        main()

    else:
        clear()
        print("NOT AVAILABLE INPUT")
        view_function()

def view_notes():
    if 0 > NOTES + 1:
        print("NO NOTES CURRENTLY FOUND")

    else:
        ID_INPUT = input("ENTER NOTE ID: ")
        print("NOTES:")
        print(notes_ary[int(ID_INPUT)])
        print("\nCHOOSE:")
        print("1  -  RETURN TO VIEW NOTE")
        print("2  -  RETURN TO MAIN MENU")
        notes_choose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
        if notes_choose == "1":
            view_function()

        elif notes_choose == "2":
            clear()
            main()

        else:
            clear()
            print("NOT AVAILABLE INPUT")
            main()

def edit_function():
    print("EDIT FUNCTION")
    display_list()
    edit_input = int(input("PLEASE INPUT THE NOTE ID:"))
    print("NOTES:")
    print("TITLE:", notes_title[int(edit_input)], "\n")
    print("NOTES:", notes_ary[int(edit_input)])

    editChoose = input("PLEASE ENTER YOUR CHOOSE[1/2]:")
    print("1  -  EDIT TITLE")
    print("2  -  EDIT NOTES")
    if editChoose == "1":
        print("EDIT TITLE")
        NEW_TITLE = input("PLEASE ENTER YOUR NOTE TITLE:")
        notes_title[int(edit_input)] = NEW_TITLE

    elif editChoose == "2":
        print("EDIT NOTES")
        NEW_NOTE = input("PLEASE ENTER YOUR NOTE:")
        notes_ary[int(edit_input)] = NEW_NOTE

    else:
        clear()
        print("NOT AVAILABLE INPUT")
        return()

def delete_function():
    global NOTES
    print("DELETE FUNCTION")
    display_list()
    delete_choose = int(input("PLEASE INPUT THE NOTE ID:"))
    notes_ary.pop(delete_choose)
    notes_title.pop(delete_choose)
    notes_time.pop(delete_choose)

    for i in range(int(delete_choose), int(NOTES - 1)):
        notes_ary[i + 1] = notes_ary[i]

    NOTES -= 1
    main()

def clear_function():
    conform_choose = input("!!!-- DID YOU CONFORM TO CLEAR DATA? --!!! (YES/NO): ").upper()
    if conform_choose == "YES":
        notes_ary.clear()
        notes_title.clear()
        clear()
        main()
    elif conform_choose == "NO":
        clear()
        main()
    else:
        print("WRONG INPUT")
        clear()
        main()

def exit_function():
    exit()  # Quit() in Jupyter Notebook, Exit() in .py / Stop() to stop cell input running

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_list():
    print("NOTES LIST")
    print("ID TITLE TIME")
    for i in range(NOTES):
        print(f"{i} {""} {notes_title[i]} {""} {notes_time[i]}")

def main():
    display_welcome()
    while True:
        command = input("Command: ").lower()  # User input command
        if command == "add":
            add_function()

        elif command == "view":
            view_function()

        elif command == "edit":
            edit_function()

        elif command == "del":
            delete_function()

        elif command == "cls":
            clear_function()

        elif command == "exit":
            exit_function()

        else:
            print("WRONG COMMAND!")
            clear()


main()
