# USAGE:
* Save keyword to multiclipboard -- mcb save {{keyword}}
* Load keyword to clipboard -- mcb {{keyword}}
* View value of keyword -- mcb view {{keyword}}
* View all values saved in multiclipboard -- mcb list OR mcb ls
* Delete keyword from multipclipboard -- mcb delete {{keyword}} OR mcb rm {{keyword}}
* Reset multiclipboard -- mcb reset OR mcb clear
* Help menu -- mcb help OR mcb -h OR mcb --help

# SETUP
1. Change the path in mcb.bat to the correct path for mcb.pyw (ex: ''C:/Users/dlope/Code/multiclipboard/mcbtemp.pyw')
2. Change the value of mcb_folder_location in mcb.pyw to where this directory is location (ex: 'C:/Users/dlope/Code')
3. Run 'python -m pip install pyperclip' (you may need to install python).
4. (Optional) Add /multiclipboard to your path in Environment Variables.
