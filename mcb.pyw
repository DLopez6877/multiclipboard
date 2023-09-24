import shelve, pyperclip, sys

mcb_folder_location = 'C:/Users/dlope/Code'
mcb_shelf = shelve.open(mcb_folder_location + '/multiclipboard/mcbtemp.ndbm', writeback=True)

# Hoisted helper functions
def ask_again():
    user_input = input('enter "Y" to clear, or "n" to cancel ')
    if user_input == 'Y':
        mcb_shelf.clear()
        print('clipboard cleared')
    elif user_input.lower() == 'n':
        print('operation canceled')
    else:
        ask_again()

def already_exists(input):
    terms_list = list(mcb_shelf.keys())
    for term in terms_list:
        if term == input:
            return True
    return False

def display_help_menu():
    print('USAGE:\nSave keyword to multiclipboard -- mcb save <keyword>\nLoad keyword to clipboard -- mcb <keyword>\nView value of keyword -- mcb view <keyword>\nView all values saved in multiclipboard -- mcb list OR mcb ls\nDelete keyword from multipclipboard -- mcb delete <keyword> OR mcb rm <keyword>\nReset multiclipboard -- mcb reset OR mcb clear\nHelp menu -- mcb help OR mcb -h OR mcb --help')


if len(sys.argv) == 2:
################ View all values saved in multiclipboard ################
    if sys.argv[1].lower() == 'list' or sys.argv[1].lower() == 'ls':
        print(str(list(mcb_shelf.keys())))

################ Load keyword to clipboard ################
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('loaded to clipboard')
    
################ Reset multiclipboard ################
    elif sys.argv[1].lower() == 'reset' or sys.argv[1].lower() == 'clear':
        user_input = input("Are you sure? Y/n ")
        if user_input == 'Y':
            mcb_shelf.clear()
            print('clipboard cleared')
        elif user_input.lower() == 'n':
            print('operation canceled')
        else:
            ask_again()

################ Help menu ################
    elif sys.argv[1].lower() == 'help' or sys.argv[1].lower() == '--help' or sys.argv[1].lower() == '-h':
        display_help_menu()

    else:
        print('Command not recognized.')


elif len(sys.argv) == 3:
################ Save keyword to multiclipboard ################
    if sys.argv[1].lower() == 'save':
        if already_exists(sys.argv[2].lower()):
            user_input = input("Keyword already exists. Override? Y/n ")
            if user_input == 'Y':
                mcb_shelf[sys.argv[2]] = pyperclip.paste()
                print('saved as:', sys.argv[2])
            elif user_input.lower() == 'n':
                print('operation canceled')
            else:
                ask_again()
        else:
            mcb_shelf[sys.argv[2]] = pyperclip.paste()
            print('saved as:', sys.argv[2])

################ Delete keyword from multipclipboard ################
    elif sys.argv[1].lower() == 'delete' or sys.argv[1].lower() == 'rm':
        if sys.argv[2] in mcb_shelf:
            del mcb_shelf[sys.argv[2]]
            print(sys.argv[2], 'has been deleted')
        else:
            print('unable to delete. keyword not found')

################ View value of keyword ################
    elif sys.argv[1].lower() == 'view':
        if sys.argv[2] in mcb_shelf:
            print(sys.argv[2], "=", mcb_shelf[sys.argv[2]])
        else:
            print('unable to view. keyword not found')

    else:
        print('Command not recognized.')

else:
        print('Command not recognized.')

mcb_shelf.close()
