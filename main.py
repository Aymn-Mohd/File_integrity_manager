import hashlib
import os
import time


def baseline():
    # creates new baseline or updates baselines for textfiles
    root = "./"
    s = str(input("Enter the text file name for the baseline: ")) + '.txt'
    path = root + s
    hashpath = root + 'hash/' + s[0:-4] + 'hash.txt'
    if os.path.exists(path):
        # if file exist it will chk for an existing file hash in the hash folder
        print(hashpath)
        if os.path.exists(hashpath):
            # this allows the user to update baseline hash
            print('Hash file exists for ' + s)
            choice = str(input("Do you wish to update baseline, Enter Yes [y] or No [n]: "))
            if choice == 'y':
                # this updates the baseline hash
                hfilen = hashpath[0:-4] + '.txt'
                sopen = open(path, 'r+')
                hopen = open(hfilen, 'w+')
                data = sopen.read()
                hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
                hopen.write(hash)
                print('Baseline for text file updated')
                print(f"hash file saved to {hfilen}")
                print('')
                main()
            else:
                # this will exit the user to the main menu
                print('')
                main()
        else:
            # if hash file does not exist the user this method allows the user to create a baseline
            print('Hash file does not exists for ' + s)
            choice = str(input("Do you wish to create baseline, Enter Yes [y] or No [n]: "))
            if choice == 'y':
                hfilen = hashpath[0:-4] + 'hash.txt'
                sopen = open(path, 'r+')
                hopen = open(hfilen, 'w+')
                data = sopen.read()
                hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
                hopen.write(hash)
                print('Baseline for text file created')
                print(f"hash file saved " + path)
                print('')
                main()
            else:
                # this will exit the user to the main menu
                print('')
                main()



    else:
        newtext(s, root, path)


def newtext(s, root, path):
    # if file does not exist the user can create a text file or exit the baseline mode
    print("The file at " + s + " does not exist.")
    choice = str(input("Do you wish to create a new text file, Enter Yes [y] or No [n] "))

    if choice == 'y':
        try:
            # Open the file in write mode
            with open(path, 'w+') as file:
                # Allow the user to input text
                print("Enter text. Type 'exit' on a new line to save and exit.")

                while True:
                    user_input = input()

                    # Check for the exit condition
                    if user_input.lower() == 'exit':
                        break

                    # Write the user input to the file
                    file.write(user_input + '\n')

            print(f"Text saved to" + path)
            print('Creating a baseline for new text file.......')
            # creates a baseline file
            hashpath = root + 'hash/' + s[0:-4] + 'hash.txt'
            sopen = open(path, 'r+')
            hopen = open(hashpath, 'w+')
            data = sopen.read()
            hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
            hopen.write(hash)
            print('Baseline for new text file created')
            print(f"hash file saved to" + hashpath)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        # this will exit the user to the main menu
        print('')
        main()


def monitor():
    # this method monitors the given text file integrity using the hash file
    root = "./"
    s = str(input("Enter the text file name to monitor ")) + '.txt'
    path = root + s
    hashpath = root + 'hash/' + s[0:-4] + 'hash.txt'
    if os.path.exists(path):
        # if text file exist it will monitor by comparing to the baseline hash
        while True:
            ts = str(time.time())
            print(ts + '/ monitoring file at ' + path)
            sread = open(path, 'r+')
            hread = open(hashpath, 'r+')
            data = sread.read()
            uhash = hread.read()
            hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
            if uhash == hash:
                print('Data is safe')
                continue
            else:
                # if data is changed the loop will break
                print('Data is changed')
                d = str(input('Do you want to quit [q] or back to menu [m]: ')).lower()
                if d == 'm':
                    # this will exit the user to the main menu
                    print('')
                    main()
                elif d == 'q':
                    # this will exit the user
                    break
    else:
        print("The file at " + s + " does not exist.")
        e = str(input('would you to create a text file, yes [y] or no [n] ')).lower()
        if e == 'y':
            newtext(s, root, path)
        else:
            # this will exit the user to the main menu
            main()


def main():
    print('### Welcome to Text File Integrity Manager ###')
    print('Mode:')
    print('Create new or update baseline for text file [A]')
    print('Monitor text file [B]')
    u = str(input('Enter Mode: ')).lower()
    if u == 'a':
        baseline()
    elif u == 'b':
        monitor()


if __name__ == '__main__':
    main()
