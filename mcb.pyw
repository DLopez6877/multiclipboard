#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw delete <keyword> - Deletes content from clipboard.
#        py.exe mcb.pyw clear - Resets clipboard.

import shelve, pyperclip, sys

mcb_shelf = shelve.open('C:/Users/daniellopez/Tools/multiclipboard/mcbtemp')

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

def already_exists():
    # TODO: add logic to loop through terms and see if it is prexisting
    return True

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    if already_exists():
        user_input = input("Are you sure? Y/n ")
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

# Delete content from clipboard
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        del mcb_shelf[sys.argv[2]]
        print(sys.argv[2], 'has been deleted')
    else:
        print('unable to delete. keyword not found')

elif len(sys.argv) == 2:
    # List keywords
    if sys.argv[1].lower() == 'list' or sys.argv[1].lower() == 'ls':
        print(str(list(mcb_shelf.keys())))

    # Load content
    elif sys.argv[1] in mcb_shelf:
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        print('loaded to clipboard')
    
    # Clear clipboard
    elif sys.argv[1].lower() == 'clear':
        user_input = input("Are you sure? Y/n ")
        if user_input == 'Y':
            mcb_shelf.clear()
            print('clipboard cleared')
        elif user_input.lower() == 'n':
            print('operation canceled')
        else:
            ask_again()

    else:
        print('keyword not found')

mcb_shelf.close()
