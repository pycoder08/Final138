# Filename: finalSection2.py
# Author: Muhammad Conn
# Description: A program that checks the popularity of names

# Algorithm:
# 1. Read the top 100 boy names and their counts from boynames.txt
# 2. Read the top 100 girl names and their counts from girlnames.txt
# 3. Store the names and counts in separate dictionaries for boys and girls using our Name class
# 4. Prompt the user to enter a name and check its rank in both dictionaries
# 5. Display the results

from name import *

def main():
    boy_file = open("boynames.txt", "r")
    girl_file = open("girlnames.txt", "r")

    boy_dict = {}
    girl_dict = {}

    boy_rank = 1
    for line in boy_file:
        name, count = line.split()
        boy_dict[name] = Name(count, boy_rank)
        boy_rank += 1

    girl_rank = 1
    for line in girl_file:
        name, count = line.split()
        girl_dict[name] = Name(count, girl_rank)
        girl_rank += 1

    boy_file.close()
    girl_file.close()


    while True:
        name = input("Enter a name (or 'exit' to quit): ").strip().lower().capitalize() #lowercase then capitalize to ensure it matches the dictionary keys
        if name == 'exit':
            break
        else:
            if name in boy_dict:
                print(f"{name} is ranked {boy_dict[name].rank} among boys.")
            else:
                print(f"{name} is not in the top 1000 boy names.")
            
            if name in girl_dict:
                print(f"{name} is ranked {girl_dict[name].rank} among girls.")
            else:
                print(f"{name} is not in the top 1000 girl names.")

main()