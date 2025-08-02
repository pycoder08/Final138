# File name: finalSection3.py
# Author: Muhammad Conn
# Description: A program to manage faculty data, allowing addition, removal, and paycheck calculation.

# Algorithm:
# 1. Create faculty classes for different types of faculty (Parttime, Salary, Hourly) using inheritance and polymorphism.
# 2. Create a list to store faculty objects.
# 3. Ask user for input to add, remove, or calculate paychecks for faculty.
# 4. Allow loading faculty data from a file and saving current faculty data to a file

from faculty import *

def main():
    faculty_list = []
    while True:
        choice = input("-----------------\nChoose an option:\n1. Add Faculty\n2. Remove Faculty\n3. Calculate Paychecks\n4. Load File\n5. Save to file\n6. Exit ")
    
        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            id = input("Enter ID: ")
            type_of_faculty = input("Enter type of faculty (parttime/salary/hourly): ").strip().lower()

            if type_of_faculty == 'parttime':
                classes = int(input("Enter number of classes: "))
                faculty_list.append(ParttimeFaculty(first_name, last_name, id, classes))
            elif type_of_faculty == 'salary':
                salary = float(input("Enter salary: "))
                faculty_list.append(SalaryFaculty(first_name, last_name, id, salary))
            elif type_of_faculty == 'hourly':
                hours_worked = float(input("Enter hours worked: "))
                hourly_rate = float(input("Enter hourly rate: "))
                faculty_list.append(HourlyFaculty(first_name, last_name, id, hours_worked, hourly_rate))
            else:
                print("Invalid faculty type.")
            
            print(f"{first_name} {last_name} ({id}) added as {type_of_faculty} faculty.")
            print_faculty_list(faculty_list)
            continue

        elif choice == '2':
            id_to_remove = input("Enter ID of faculty to remove: ")
            for faculty in faculty_list:
                if faculty.id == id_to_remove:
                    faculty_list.remove(faculty)
                    print(f"{faculty.first_name} {faculty.last_name} ({faculty.id}) removed.")
                    break
            print_faculty_list(faculty_list)

        elif choice == '3':
            print("Monthly paychecks for all faculty:")
            for faculty in faculty_list:
                print(f"{faculty.first_name} {faculty.last_name} ({faculty.id}) - Pay: ${faculty.calculate_pay()}")
            print_faculty_list(faculty_list)

        elif choice == '4':
            path = input("Enter the path to the faculty data file: ")
            load_file = open(path, "r")
            for line in load_file:
                parts = line.strip().split(", ")
                if parts[0] == 'Parttime':
                    faculty_list.append(ParttimeFaculty(parts[1], parts[2], parts[3], int(parts[4])))
                elif parts[0] == 'Salary':
                    faculty_list.append(SalaryFaculty(parts[1], parts[2], parts[3], float(parts[4])))
                elif parts[0] == 'Hourly':
                    faculty_list.append(HourlyFaculty(parts[1], parts[2], parts[3], float(parts[4]), float(parts[5])))
            load_file.close()
        elif choice == '5':
            out_file = open("faculty_data.txt", "w")
            for faculty in faculty_list:
                if isinstance(faculty, ParttimeFaculty):
                    out_file.write(f"Parttime, {faculty.first_name}, {faculty.last_name}, {faculty.id}, {faculty.classes}\n")
                elif isinstance(faculty, SalaryFaculty):
                    out_file.write(f"Salary, {faculty.first_name}, {faculty.last_name}, {faculty.id}, {faculty.salary}\n")
                elif isinstance(faculty, HourlyFaculty):
                    out_file.write(f"Hourly, {faculty.first_name}, {faculty.last_name}, {faculty.id}, {faculty.hours_worked}, {faculty.hourly_rate}\n")
            out_file.close()
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

def print_faculty_list(faculty_list):
    print("Current Faculty List:")
    for faculty in faculty_list:
        print(f"{faculty.first_name} {faculty.last_name} ({faculty.id}) - Pay: ${faculty.calculate_pay()}")

main()