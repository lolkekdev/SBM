import os

print("""░██████╗██╗███╗░░░███╗██████╗░██╗░░░░░███████╗  ██████╗░░█████╗░░█████╗░████████╗
██╔════╝██║████╗░████║██╔══██╗██║░░░░░██╔════╝  ██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░██║██╔████╔██║██████╔╝██║░░░░░█████╗░░  ██████╦╝██║░░██║██║░░██║░░░██║░░░
░╚═══██╗██║██║╚██╔╝██║██╔═══╝░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║██║░░██║░░░██║░░░
██████╔╝██║██║░╚═╝░██║██║░░░░░███████╗███████╗  ██████╦╝╚█████╔╝╚█████╔╝░░░██║░░░
╚═════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚══════╝╚══════╝  ╚═════╝░░╚════╝░░╚════╝░░░░╚═╝░░░

███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
████╗░████║██╔════╝████╗░██║██║░░░██║
██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░""")
name = "urnamehere"  # put your name here
license = "GNU GPL V2"  # change type of license if you want
mod = "m"  # remove this line if you wouldn't modify this program'
print("Created by lolkekdev")
print(f"Modified by {name}")
print(f"Version: 1.0{mod}")
print(f"License: {license}")

progpath = ""  # enter path to your program here

main = input("Awaiting input...\ntype 'off' to turn down the program\n")

while main != "":
    if main == "launch":
        print("Starting the program...")
        os.system(progpath)
    elif main == "off":
        exit(0)
    elif main == "info":
        print("=" * 10, "Information", "=" * 10)  # Write your info below
        print("test")
    elif main == "help":  # Write your commands here
        print("launch - launch the program")
        print("modhelp - SBM modding manual")
        print("off - shutdown program")
    elif main == "modhelp":
        qstn = input("Open modding.txt [Y/N]")
        qstn.lower()
        if qstn == "y":
            print("Opening modding.txt")
            modfile = open("modding.txt", "r")
            data = modfile.read()
            print(data)
        elif qstn == "n":
            print("Operation aborted!")
        else:
            print("Incorrect answer, operation aborted!")
    elif main == "license":
        print("""
                 SIMPLE BOOT MENU (Factory license)
                 Copyright (C) 2022  lolkekdev
                
                 This program is free software; you can redistribute it and/or
                 modify it under the terms of the GNU General Public License
                 as published by the Free Software Foundation; either version 2
                 of the License, or (at your option) any later version.
                
                 This program is distributed in the hope that it will be useful,
                 but WITHOUT ANY WARRANTY; without even the implied warranty of
                 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
                 GNU General Public License for more details.
                
                 You should have received a copy of the GNU General Public License
                 along with this program; if not, write to the Free Software
                 Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
                 You also received full copy of GNU license. You can red it in license.txt""")

    main = input("Awaiting input...\ntype 'off' to turn down the program\n")
