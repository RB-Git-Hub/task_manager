#=====importing libraries===========
import os
from datetime import date

#====Todays Date====
today = date.today()
todays_date = today.strftime("%d %b %Y")

#====Login============================================
os.system('cls')
lock= True
user = open("user.txt", "r")
user_read = user.read()
user_string = user_read.replace(",","").replace(" ","").replace("\n"," ").split()
print("════════════════ Login ═══════════════════════\n")
while lock==True:
    user_name=input("Please enter your username: ")
    user_password=input("Please enter your password: ")  
    code= (user_name + user_password)
    for p in (user_string):
        if p == code:
            user.close
            lock=False
    if lock == True:
        os.system('cls')
        print("════════════════ Login ═══════════════════════\n")
        print("You're login details were incorrect please try again!\n")   
user.close

#====Main Menu========================================
os.system("cls")
while True:
    print("════════════════ Main Menu ═══════════════════════\n")
    if user_name == "admin":
        print("Select one of the following Options below:\nr \t- Registering a user\na \t- Adding a task\nva \t- View all tasks\nvm \t- view my tasks\nd \t- Display statistics\ne \t- Exit")
    else:
        print("Select one of the following Options below:\na \t- Adding a task\nva \t- View all tasks\nvm \t- view my tasks\ne \t- Exit")
    menu = input("").lower()

    #====Registering a user=====================================================
    if menu == "r" and user_name == "admin":
        os.system("cls")
        print("═════════════ Registering a user ═══════ e=exit ══\n")
        while menu=="r":
            new_user= input("Please enter the new username: ")
            if new_user == "e":
                os.system("cls")
                break
            new_user_pass= input("Please enter the new password: ")
            confirm= input("Please confirm your password : ")
            if new_user_pass == confirm:
                with open("user.txt", "a") as user:
                    user.write(f"\n{new_user}, {new_user_pass}")
                os.system("cls")
                user.close
                print("\nNew user has been added.\n")
                break
            else: 
                os.system("cls")
                print("═════════════ Registering a user ═══════ e=exit ══\n")
                print("Error passwords didn't match, please start again.\n")
   
    #====Adding a task=========================================================
    elif menu == "a":
        os.system("cls")
        print("═════════════ Adding a task ═══════ e=exit ══\n")
        while menu=="a":
            user_id= input("Please enter the username to assign to the task: ")
            if user_id == "e":
                os.system("cls")
                break
            task_title = input("Please enter the title of the task: ")
            description_of_task= input("Please give a task description: ")
            due_date = input("Please enter a task due date: ")
            with open("tasks.txt", "a") as task:
                task.write(f"\n{user_id}, {task_title}, {description_of_task}, {todays_date}, {due_date}, No")
            task.close
            os.system("cls")
            print("\nNew task has been added.\n")
            break

    #====View all tasks=========================================================
    elif menu == "va":
        tasks = open("tasks.txt", "r" )    
        read_tasks = [line.rstrip() for line in tasks]
        os.system('cls')
        print("═════════════ View all tasks ═══════════════\n") 
        for p, line in enumerate(read_tasks):
            split_line = line.split(", ")          
            print(f"\n****************** Task No. {p+1} ***********************************************************************************************\n")       
            print(f"Task\t\t : {split_line[1]}")
            print(f"Assigned to \t : {split_line[0]}")   
            print(f"Date assigned\t : {split_line[3]}")     
            print(f"Due date\t : {split_line[4]}")   
            print(f"Task complete?\t : {split_line[5]}")  
            print(f"Task Description : {split_line[2]}\n\n")
        input("Press enter to go back to the main menu ")   
        task.close
        os.system('cls')

    #====View my tasks==============================================================
    elif menu == "vm":
        tasks = open("tasks.txt", "r" )    
        read_tasks = [line.rstrip() for line in tasks]
        os.system('cls')
        print("═════════════ View my tasks ═══════════════\n") 
        no_task=0
        for p, line in enumerate(read_tasks):
            split_line = line.split(", ")          
            if split_line[0] == user_name:
                print(f"\n****************** Task No. {p+1} ***********************************************************************************************\n")       
                print(f"Task\t\t : {split_line[1]}")
                print(f"Assigned to \t : {split_line[0]}")   
                print(f"Date assigned\t : {split_line[3]}")     
                print(f"Due date\t : {split_line[4]}")   
                print(f"Task complete?\t : {split_line[5]}")  
                print(f"Task Description : {split_line[2]}\n\n")
                no_task = 1
        if no_task == 0:
            print("    *** You have no tasks assigned ***\n")        
        input("Press enter to go back to the main menu ")  
        tasks.close
        os.system('cls')

    #==== Statistics =====================================================
    if menu == "d" and user_name == "admin":
        #Task Counter
        tasks = open("tasks.txt", "r" )    
        read_tasks = [line.rstrip() for line in tasks]
        total_tasks = 0 
        for p in enumerate(read_tasks):
            total_tasks += 1          
        
        #User Counter
        tasks = open("user.txt", "r" )    
        read_tasks = [line.rstrip() for line in tasks]
        total_users = 0
        os.system('cls')
        print("═════════════ Statistics ═══════════════\n") 
        for p in enumerate(read_tasks):    
            total_users += 1

        print(f"The total tasks : {total_tasks}")    
        print(f"The total users : {total_users}")    
        input("\nPress enter to go back to the main menu ")   
        tasks.close

        os.system('cls')  
    
    #====Exit=======================================================================
    elif menu == "e":
        os.system('cls')
        print("Goodbye!\n\nYou are now logged out.\n")
        exit()
            
    else:
        os.system('cls')
        print("You have made a wrong choice, please try again\n")
