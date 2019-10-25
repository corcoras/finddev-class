import os
from sys import argv

script, dealer_name = argv

#dealer_name = "MCL Motors"

def make_dir(dealer_name):
    pwd = os.getcwd()
    print(f"Your currently here {pwd}")
    #navigate to directory
    dealer_folder = dealer_name[:1]
    #got to folder
    os.chdir('/Users/shaun/dev/')
    os.mkdir(dealer_folder)
    os.chdir(dealer_folder)
    print(os.getcwd())
    if os.path.exists(dealer_name):
        pass
    else:
        os.mkdir(dealer_name)
        os.chdir(dealer_name)
        os.mkdir("config")
        os.mkdir("original")
        os.mkdir("final")

make_dir(dealer_name)


