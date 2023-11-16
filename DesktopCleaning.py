import os
import winshell
import time

def DeskClean():
    while True:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
        deskitems = os.listdir(desktop)
        print()
        deskini = deskitems.index('desktop.ini')
        deskitems.pop(deskini)
        items = len(deskitems)
        if items == 0:
            print('No files found on the desktop.')
            time.sleep(2)
            break

        print('Current items on desktop:')
        for item in deskitems:
            print(item)

        print()
        choice = input('Do you want to clean your desktop? y/n: ')
        if choice.lower() == 'y':
            print()
            for item in deskitems:
                print(item)
            print()
            choice2 = input('Confirm deleting the following items from your desktop y/n: ')
            print()
            if choice2.lower() == 'y':
                for item in deskitems:
                    itemfound = os.path.join(desktop, item)
                    if os.path.isfile(itemfound):
                        os.remove(itemfound)
                    elif os.path.isdir(itemfound):
                        os.rmdir(itemfound)
                print('Deletion Complete.')
                time.sleep(2)
                break
            elif choice2.lower() == 'n':
                print('Cancelling Deletion.')
                time.sleep(2)
                break
        elif choice.lower() == 'n':
            print('Cancelling Action.')
            time.sleep(2)
            break
        else:
            print()
            print('Unspecified Command.')
            print('Please answer with either y/n.')
            time.sleep(2)
            continue
def BinClean(): 
    while True:
        BinItems = list(winshell.recycle_bin())
        print(len(BinItems), "items are present in recycle bin") 
        print()
        for item in BinItems: 
            print(item) 
        print()
        choice = input('Do you want to empty the Recycle Bin? y/n ')
        if choice.lower() == 'y':
            try:
                winshell.recycle_bin().empty(confirm=False)
                print()
                print('Recycle Bin has been emptied.') 
                time.sleep(2)
                break
            except Exception:
                print()
                print('Unexpected Error or Recycle Bin is already empty.')
                time.sleep(2)
                break
        elif choice.lower() == 'n':
            print()
            print('Action Cancelling.')
            time.sleep(2)
            break
        else:
            print('Invalid input expected y/n')
            time.sleep(2)
            continue
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print()
print('Cleaning Service, how may I help?')
while True:
    Clear()
    print()
    print('Please select of the either choices.')
    print('1 - exit\n2 - DeskClean\n3 - BinClean')
    print()
    mainchoice = input()
    print()
    if mainchoice == '1':
        exit()
    elif mainchoice == '2':
        DeskClean()
    elif mainchoice == '3':
        BinClean()
    else:
        print()
        continue