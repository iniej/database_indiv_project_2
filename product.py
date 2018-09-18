import ui

# A function to handle items on the menu.
def handle_choice(choice):

    if choice == '1':
        ui.create_table()
        print("Table created successfully")

    elif choice == '2':
        ui.add_new_product()

    elif choice == '3':
        ui.update_a_row()

    elif choice == '4':
        ui.delete_a_row()

    elif choice == '5':
        ui.display_all_rows()

    elif choice == '6':
        ui.display_a_row()

    elif choice == 'q':
        print('Bye!')
        quit()

    else:
        ui.message('Please enter a valid selection\n')

# The program is run from the main function.
def main():

    quit = 'q'
    choice = None

    while choice != quit:
        choice = ui.display_menu_get_choice()
        handle_choice(choice)


if __name__ == '__main__':
    main()
