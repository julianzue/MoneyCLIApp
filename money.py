import time
from colorama import Fore, init
from pyfiglet import Figlet
import os

init()

c = Fore.LIGHTCYAN_EX
y = Fore.LIGHTYELLOW_EX
r = Fore.LIGHTRED_EX
g = Fore.LIGHTGREEN_EX
re = Fore.RESET

class Money():
    def __init__(self):

        t = Figlet()
        print(y + t.renderText("MONEY") + re)

        self.main()

    
    def help(self):
        print("")
        print("HELP")
        print("")
        print(c + "add" + re + "\tAdds a positive Value to the list.")
        print(c + "sub" + re + "\tAdds a negative Value to the list.")
        print(c + "list" + re + "\tShows the list.")
        print(c + "edit" + re + "\tEdits a line of the list.")
        print(c + "del" + re + "\tDeletes a line of the list.")

        print("")

        self.main()


    def main(self):

        

        x = input(y + "--> " + re)

        if x == "add":
            print("")
            price = input(y+ "[+] " + re + "Price: ")
            what = input(y + "[+] " + re + "What:  ")

            self.add(price, what)

        elif x == "sub":
            print("")
            price = input(y+ "[+] " + re + "Price: ")
            what = input(y + "[+] " + re + "What:  ")

            self.sub(price, what)

        elif x == "list":
            self.list()

        elif x == "help":
            self.help()

        elif x == "exit" or x == "q":
            print("")
            print(r + "[*] " + re + "Program closed!")
            print("")
            quit()

        elif x == "clear":
            os.system("clear")
            self.main()

        elif x == "edit":
            self.edit()

        elif x == "del":
            self.delete()

        else:
            print("")
            print(r + "[!] " + re + "Unknown command. Try again!")
            print("")
            self.main()


    def add(self, price, what):
        file = open("data.txt", "a")
        file.write(time.strftime("%Y-%m-%d %H:%M") + " | " + "{:7.2f}".format(float(price)) + " | " + what + "\n")
        file.close()

        print(c + "[*] " + re + "Successfully written to " + c + "data.txt" + re + "!")

        print("")
        
        self.main()


    def sub(self, price, what):
        file = open("data.txt", "a")

        new_price = float(price) * -1

        file.write(time.strftime("%Y-%m-%d %H:%M") + " | " + "{:7.2f}".format(new_price) + " | " + what + "\n")
        file.close()

        print(c + "[*] " + re + "Successfully written to " + c + "data.txt" + re + "!")

        print("")

        self.main()


    def list(self):

        print("")

        if not os.path.exists("data.txt"):
            os.system("touch data.txt")
            print(c + "[*] " + re + "Successfully created " + c + "data.txt" + re + "!")
            print("")

        file = open("data.txt", "r")
        
        total = 0.0

        print("ID  | Date & Time      | Price     | Subtotal  | What")
        print("----+------------------+-----------+-----------+----------------------")

        for index, line in  enumerate(file.readlines(), 1):
            if line != "":
                sp = line.strip("\n").split(" | ")

                if float(sp[1]) < 0:
                    color = r
                else:
                    color = re

                total += float(sp[1])

                if float(total) < 0:
                    color_total = r
                else:
                    color_total = re

                print("{:03d}".format(index) +" | " + sp[0] + " | " + color + sp[1] + " €" + re + " | " + color_total + "{:7.2f}".format(total) + " €" + re + " | " + sp[2] + re)

            else:
                print(c + "[*] " + re + "No entries!")

        print("")

        if float(total) < 0:
            color_total = r
        else:
            color_total = g

        print(color_total + "[*] " + re + "Total: " + color_total + "{:7.2f}".format(total) + " €"+ re)

        print("")

        self.main()

    def edit(self):
        
        print("")

        if not os.path.exists("data.txt"):
            os.system("touch data.txt")
            print(c + "[*] " + re + "Successfully created " + c + "data.txt" + re + "!")
            print("")

        file = open("data.txt", "r")
        
        total = 0.0

        get_line = []

        print("ID  | Date & Time      | Price     | Subtotal  | What")
        print("----+------------------+-----------+-----------+----------------------")

        for index, line in  enumerate(file.readlines(), 1):
            if line != "":
                sp = line.strip("\n").split(" | ")

                if float(sp[1]) < 0:
                    color = r
                else:
                    color = re

                total += float(sp[1])

                if float(total) < 0:
                    color_total = r
                else:
                    color_total = re

                print("{:03d}".format(index) +" | " + sp[0] + " | " + color + sp[1] + " €" + re + " | " + color_total + "{:7.2f}".format(total) + " €" + re + " | " + sp[2] + re)

                get_line.append(line)

            else:
                print(c + "[*] " + re + "No entries!")

        print("")

        while True:
            get_id = input(y + "[+] " + re + "Enter ID: ")

            if get_id.isnumeric():
                self.doEdit(int(get_id))
                break
            else:
                print(r + "[!] " + re + "No number! Try again.")


    def doEdit(self, line):

        print("")

        file = open("data.txt", "r")

        lines = file.readlines()

        l = lines[line - 1]

        sp = l.strip("\n").split(" | ")

        #date

        checkDate = input(y + "[+] " + re + "Date: " + y + sp[0] + re + ". Correct? [Y|n]: ")

        if checkDate == "n" or checkDate == "N":
            new_date = input(y + "[+] " + re + "New Date & Time: ")
        else:
            new_date = sp[0]

        #price
        print("")

        checkPrice = input(y + "[+] " + re + "Price: " + y + sp[1] + re + ". Correct? [Y|n]: ")

        if checkPrice == "n" or checkPrice == "N":
            new_p = input(y + "[+] " + re + "New Price: ")
            new_price = "{:7.2f}".format(float(new_p))
        else:
            new_price = sp[1]

        #what
        print("")

        checkWhat = input(y + "[+] " + re + "What: " + y + sp[2] + re + ". Correct? [Y|n]: ")

        if checkWhat == "n" or checkWhat == "N":
            new_what = input(y + "[+] " + re + "New What: ")
        else:
            new_what = sp[2]

        lines[line - 1] = new_date + " | " + new_price + " | " + new_what + "\n"
 
        with open('data.txt', 'w') as file:
            file.writelines(lines)
        
        print("")
        print(c + "[*] " + re + "All Done!")
        print("")

        self.main()

    
    def delete(self):
        print("")

        if not os.path.exists("data.txt"):
            os.system("touch data.txt")
            print(c + "[*] " + re + "Successfully created " + c + "data.txt" + re + "!")
            print("")

        file = open("data.txt", "r")
        
        total = 0.0

        get_line = []

        print("ID  | Date & Time      | Price     | Subtotal  | What")
        print("----+------------------+-----------+-----------+-------------------------------")

        for index, line in  enumerate(file.readlines(), 1):
            if line != "":
                sp = line.strip("\n").split(" | ")

                if float(sp[1]) < 0:
                    color = r
                else:
                    color = re

                total += float(sp[1])

                if float(total) < 0:
                    color_total = r
                else:
                    color_total = re

                print("{:03d}".format(index) +" | " + sp[0] + " | " + color + sp[1] + " €" + re + " | " + color_total + "{:7.2f}".format(total) + " €" + re + " | " + sp[2] + re)

                get_line.append(line)

            else:
                print(c + "[*] " + re + "No entries!")

        print("")

        while True:

            get_id = input(y + "[+] " + re + "Enter ID: ")

            if get_id.isnumeric():
                self.doDelete(int(get_id))
                break
            else:
                print(r + "[!] " + re + "No number! Try again.")

    
    def doDelete(self, line):
        with open("data.txt", "r") as f:
            lines = f.readlines()
        with open("data.txt", "w") as f:
            for index, lines in enumerate(lines, 1):
                if index != line:
                    f.write(lines)

        print("")
        print(c + "[*] " + re + "All Done!")
        print("")

        self.main()

Money()