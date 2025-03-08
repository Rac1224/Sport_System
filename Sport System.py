#WAI KEI RACHEL FOONG 

#Functionalities of Main Menu(RCSAS)

        
def main_menu():
    print("\n\t__REAL CHAMPIONS SPORT ACADEMY SYSTEM__\n\n")
    print("Are you an admin or a student?")
    print("1. Admin")
    print("2. Student")
    print("0. Exit System\n")

    while 1: 
        try:
             choice =  int(input("Enter your choice via number: "))
     
             if (choice == 1):
                  admin_function()

             elif(choice == 2):
                  guest_login()

             elif(choice == 0):
                  exit()   
     
             else:
                print("Wrong input!")
                pass
        except:
            print("Please input an integer")
            pass

#Functionalities of Admin
#Admin Login
def admin_function():
    print("\nAdmin Login\nEnter 0 for username and password to go back\n")
    

    while 1:
        admin_username = input("Username: ")
        admin_pwd = input("Password: ")
        if (admin_username=="r") and (admin_pwd=="p"):
            admin_login()
        elif (admin_username=="0") and (admin_pwd=="0"):
            main_menu()
        else:
            print("\nWrong credentials!")
            pass
        
        
def admin_login():
    print("\n__Welcome Admin!__")
    print("\n1. Add Record")
    print("2. Display All Record")
    print("3. Search Specific Record")
    print("4. Sort and Display Record")
    print("5. Modify Record")    
    print("6. Exit")

    while 1:
        try:
            a_choice = int(input("\nEnter your choice: "))
            if(a_choice == 1):
                add_records()
                
            elif(a_choice == 2):
                dis_records()
                
            elif(a_choice == 3):
                search_rec()
                
            elif(a_choice == 4):
                sort_dis_rec()
                
            elif(a_choice == 5):
                mod_rec()
                
            elif(a_choice == 6):
                print("Program has been terminated.")
                exit()
                
            else:
                print("Please enter within the range again.")
                pass

        except:
            print("Please enter a valid number.")
            pass

#Add Record
def add_records():
    print("What would you like to add record to?")
    print("\n1. Coach")
    print("2. Sport")
    print("3. Sport Schedule")
    print("0. Go Back")

    while 1:
        try:
            choice = int(input("\nEnter your choice: ")) 
            if (choice == 1):
                coach()

            elif (choice == 2):
                sport()

            elif (choice == 3):
                sport_sce()

            elif (choice == 0):
                admin_login()
            else:
                print("Please enter a valid input.")
                pass
        except:
            print("Please enter integer input.")
            pass
    
def coach(): 
    add_coach_rec = []
    c_details = []
    
    print("\n___Add Records to Coach___")
    coach_id = input("\nCoach ID: ")
    c_details.append(coach_id)
    
    coach_name = input("Coach Name: ")
    c_details.append(coach_name)
    
    coach_joined = input("Date Joined: ")
    c_details.append(coach_joined)
    
    

    while 1:
        try:
            hourly_rate = input("Hourly Rate(range from RM100-500): ")
            if (float(hourly_rate) >= 100) and (float(hourly_rate) <= 500) and (len(hourly_rate)<=6):
                c_details.append(hourly_rate)
                break
            else:
               print("Please enter within the range RM100-500.")
               pass
               
        except:
            print("Please enter a number.")
            pass

    while 1:
        try:
            coach_phone = input("Phone Number: ")
            if(int(coach_phone)):
                break
            
        except:
            print("Please enter a valid phone number (Without - or +)")
            pass
   
    c_details.append(coach_phone)
    
    coach_add = input("Address: ")
    c_details.append(coach_add)

    coach_sport = input("Specialised sport: ")
    c_details.append(coach_sport)

    coach_sport_name = input("Sport Centre Name: ")
    c_details.append(coach_sport_name)
    
    add_coach_rec.append(c_details)

    try:
        txtf = open('add_records.txt','a')
        for c_details in add_coach_rec:
            for index, fs in enumerate(c_details):
                txtf.write(fs)
                if(index+1<len(c_details)):
                    txtf.write(', ')
            txtf.write('\n')
        txtf.close()
        
    except:
        print("Error editing text file. Returning to main menu...")
        main_menu()

    print("Coach Details Added Successfully! Returning to Admin Menu...")
    

    while 1:
        try:
            conti = int(input("Would you like to add another coach? (\"1-> Retry, 2-> Quit\"): "))
            if (conti == 1):
                coach()
            elif (conti == 2):
                admin_login()
            else:
                print("Please enter a correct option!")
                pass
        except:
            print("Please enter an integer!")
            pass
    
def sport():
    add_sport_rec = []
    s_details = []
    
    print("\n__Add Records to Sport__")
    sport_id = input("\nSport ID: ") 
    s_details.append(sport_id)
    
    sport_name = input("Sport Name: ") 
    s_details.append(sport_name) 

    while 1:
        try:
            sport_fee = input("Sport Fee: RM ")
            if(float(sport_fee)):
                s_details.append(sport_fee)
                break
            else:
                print("Please enter a valid number!")
                pass
            
        except:
            print("Please enter a valid number!")
            pass
    
    add_sport_rec.append(s_details)
    
    txtf = open('sport.txt','a') 
    for s_details in add_sport_rec:
        for index, fs in enumerate(s_details):
            txtf.write(fs)
            if(index+1<len(s_details)):
                txtf.write(', ')
        txtf.write('\n')
    txtf.close()
    print("Sport Added Successfully! Returning to Admin Menu...")
    admin_login()
    
def sport_sce():
    add_sport_sce__rec = []
    s_sce_details = []
    print("\n__Add Records to Sport Schedule__")
    sport_name_sce = input("\nSport Name: ")
    s_sce_details.append(sport_name_sce)
    
    sport_sce_new = input("Sport Schedule: ")
    s_sce_details.append(sport_sce_new)

    add_sport_sce__rec.append(s_sce_details)
    

    txtf = open('sport_sce.txt','a')
    for s_sce_details in add_sport_sce__rec: 
        for index, fs in enumerate(s_sce_details):
            txtf.write(fs)
            if(index+1<len(s_sce_details)):
                txtf.write(', ')
        txtf.write('\n')
    txtf.close()
    print("Sport Schedule Added Successfully! Returning to Admin Menu...")
    admin_login()


#Display Records
def dis_records():
    print("\nWhat records would you like to display?")
    print("\n1. Coach")
    print("2. Sport")
    print("3. Registered Students")
    print("0. Go Back")
    
    try:
        d_choice = int(input("\nEnter your choice: "))
        if (d_choice == 1):
            dis_coach()
            
        elif (d_choice == 2):
            dis_sport()
            
        elif (d_choice == 3): 
            dis_student_resg()
        elif (d_choice == 0): 
            admin_login()

        else:
            print("Please enter a valid input.")
            dis_records()
    except:
        print("Please enter a number.")
        pass

def dis_coach():
    print ("\n___Coach Records___")
    txtf = open('add_records.txt','r')
    content = txtf.read()
    print(content)
    txtf.close()
    print(" Returning to Admin Menu...")
    admin_login()

def dis_sport():
    print ("\n___Sport Records___")
    txtf = open('sport.txt','r')
    content = txtf.read()
    print(content)
    txtf.close()
    print(" Returning to Admin Menu...")
    admin_login()

def dis_student_resg():
    print ("\n___Registered Student Records___")
    txtf = open('student.txt','r') 
    content = txtf.read()
    print(content)
    txtf.close()
    print(" Returning to Admin Menu...")
    admin_login()

#Search Specific Records
def search_rec():
    print("\nWhat would you like to search?")
    print("\n1. Coach by Coach ID")
    print("2. Coach by overall performance")
    print("3. Sport by Sport ID")
    print("4. Student by Student ID")
    
    choice = int(input("\nEnter your choice: "))

    if (choice == 1):
        c_id()
       
    elif (choice == 2):
        c_score()

    elif (choice == 3):
        sp_id()

    elif (choice == 4):
        s_id()

    else:
        print("Please enter a valid input.")
        add_record()

def c_id():
    print("\n___Search Coach by Coach ID___")
    coach_id = input("\nCoach ID: ")
    
    with open('add_records.txt') as txtf:
        
        for line in txtf:
            for word in line.split(", "):
                if (word==coach_id):
                    print(line)
                    print(" Returning to Admin Menu...")
                    admin_login() 
        
          
        print("Coach ID does not exist")

        while 1:
            
            try:
                conti = int(input("Would you like to retry? (\"1-> Retry, 2-> Quit\"): "))

                if (conti == 1):
                    search_rec()
                elif(conti == 2):
                    admin_login()
                else:
                   print("Please enter within range of 1-2.")
                   pass
            except:
                print("Please enter a valid integer!")
                pass
                    
def c_score():
    print("\n___Search Coach by number of stars___")
    stars = input("\nNumber of stars of the Coach: ")
    
    with open('add_records.txt') as txtf:           
        for line in txtf:
            for index, word in enumerate(line.split(", ")):
                if (word==(stars+"\n")) or (word==(stars+" \n")):
                        print(line)
        print(" Returning to Admin Menu...")
        admin_login()

    print('Not found')
    admin_login()

def sp_id():
    print("\n___Search Sport by Sport ID___")
    spo_id = input("\nSport ID: ") 

    with open('sport.txt') as txtf:           
        for line in txtf:
            for word in line.split(", "):
                if (word==spo_id):
                    print(line)
                    print(" Returning to Admin Menu...")
                    admin_login() 
            
              
        print("Sport ID does not exist")

        while 1:
            
            try:
                conti = int(input("Would you like to retry? (\"1-> Retry, 2-> Quit\"): "))

                if (conti == 1):
                    sp_id()
                elif(conti == 2):
                    admin_login()
                else:
                   print("Please enter within range of 1-2.")
                   pass
            except:
                print("Please enter a valid integer!")
                pass

def s_id():
    print("\n___Search Student by Student ID___")
    st_id = input("\nStudent ID: ") 

    with open('student.txt') as txtf:
        for line in txtf:
                for word in line.split(", "):
                    if (word==st_id):
                        print(line)
                        print(" Returning to Admin Menu...")
                        admin_login() 
                          
    print("Sport ID does not exist")

    while 1:
            
        try:
            conti = int(input("Would you like to retry? (\"1-> Retry, 2-> Quit\"): "))

            if (conti == 1):
                s_id()
            elif(conti == 2):
                admin_login()
            else:
               print("Please enter within range of 1-2.")
               pass
        except:
            print("Please enter a valid integer!")
            pass


#Sort and display Record
def sort_dis_rec():
    print("\nPlease select one option of how you would like to sort and display the coaches' records.")
    print("1. Coaches in ascending order by names")
    print("2. Coaches Hourly Pay Rate in ascending order")
    print("3. Coaches Overall Performance in ascending order")

    choice = int(input("\nEnter your choice: "))
    
    if(choice == 1):
        ascen_alpha()
        
    elif(choice == 2):
        ascen_hourly_rate()

    elif(choice == 3):
        ascen_score()
        
    else:
        print("Please enter within the range again.")
        admin_login()

def ascen_alpha():
    index_array = []
    print ("\n___Coach Records___")

    with open('add_records.txt') as txtf:
            
            for line in txtf:
                for index, word in enumerate(line.split(", ")):
                    if (index == 1):
                        index_array.append(word)
            index_array = sorted(index_array)
            print(index_array)
            admin_login()

def ascen_hourly_rate():
    index_array = []
    print ("\n___Coach Records___")
    
    with open('add_records.txt') as txtf:
            
            for line in txtf:
                for index, word in enumerate(line.split(", ")):
                    if (index == 3):
                        index_array.append(word)
            index_array = sorted(index_array)
            print(index_array)
            admin_login()
            
## not done
def ascen_score():
    print ("\n___Coach Records___")
    txtf = open('add_records.txt','r')
    content = txtf.read()
    print(content)
    txtf.close()
    admin_login()

#Modify Record
def mod_rec():
    print("\nWhich record would you like to modify?")
    print("1. Coach")
    print("2. Sport")
    print("3. Sport Schedule")

    choice = int(input("\nEnter your choice: "))
    
    if(choice == 1):
        modify_coach()
        
    elif(choice == 2):
        modify_sport()

    elif(choice == 3):
        modify_sport_sce()
        
    else:
        print("Please enter within the range again.")
        mod_rec()

def modify_coach():
  

    coach_id= input("Enter the coach ID who you want to modify:")
    choice=int(input("Which detail would you like to modify?\n1. Coach Name\n2. Date Joined\n3. Hourly Pay\n4. Phone Number\n5. Address\n6. Specialised Sport\n7. Sport Center Name\nChoice: "))
    new =  input("Enter the new value:")
    empty_array=[]
    old_array=[]
    string1=""
    string2=""
    savetheindex=0
    flag_found=False
    with open('add_records.txt') as txtf:
         
            for index1, line in enumerate(txtf):
                for index, word in enumerate(line.split(", ")):
                    if (word==coach_id) and (index==0):
                        flag_found=True
                        savetheindex=index1
                        for index, word in enumerate(line.split(", ")):
                            old_array.append(word)
                            if(index == choice):
                                if("\n" in word):
                                    new=new+"\n"
                                empty_array.append(new)
                            else:
                                empty_array.append(word)
            if(flag_found==True):
                for index, word in enumerate(empty_array):
                    if(index==0):
                        string1=word
                    elif(index==len(word)-1):
                        string1=string1+" "+word
                    else:
                        string1=string1+", "+word

                for index, word in enumerate(old_array):
                    if(index==0):
                        string2=word
                    elif(index==len(word)-1):
                        string2=string2+" "+word
                    else:
                        string2=string2+", "+word

          
                a_file = open("add_records.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[savetheindex] = string1

                a_file = open("add_records.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()

                print("Done")
            else:
                print("Error, coach not found")
            admin_login()

def modify_sport():

    sport_id= input("Enter the sport ID who you want to modify:")
    choice=int(input("Which detail would you like to modify?\n1. Sport Name\n2. Sport Fee\nChoice: "))
    new =  input("Enter the new value:")
    empty_array=[]
    old_array=[]
    string1=""
    string2=""
    savetheindex=0
    flag_found=False
    with open('sport.txt') as txtf:
         
            for index1, line in enumerate(txtf):
                for index, word in enumerate(line.split(", ")):
                    if (word==sport_id) and (index==0):
                        flag_found=True
                        savetheindex=index1
                        for index, word in enumerate(line.split(", ")):
                            old_array.append(word)
                            if(index == choice):
                                if("\n" in word):
                                    new=new+"\n"
                                empty_array.append(new)
                            else:
                                empty_array.append(word)
            if(flag_found==True):
                
                for index, word in enumerate(empty_array):
                    if(index==0):
                        string1=word
                    elif(index==len(word)-1):
                        string1=string1+" "+word
                    else:
                        string1=string1+", "+word

                for index, word in enumerate(old_array):
                    if(index==0):
                        string2=word
                    elif(index==len(word)-1):
                        string2=string2+" "+word
                    else:
                        string2=string2+", "+word
                print(string1)
                print(string2)  
                a_file = open("sport.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[savetheindex] = string1

                a_file = open("sport.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()

                print("Done")
            else:
                print("Error, coach not found")
            admin_login()

def modify_sport_sce():
  
    sport_sce= input("Enter the Sport which you want to modify:")
    new =  input("Enter the new sport schedule:")
    empty_array=[]
    old_array=[]
    string1=""
    string2=""
    savetheindex=0
    flag_found=False
    with open('sport_sce.txt') as txtf:
         
            for index1, line in enumerate(txtf):
                for index, word in enumerate(line.split(", ")):
                    if (word==sport_sce) and (index==0):
                        flag_found=True
                        savetheindex=index1
                        for index, word in enumerate(line.split(", ")):
                            old_array.append(word)
                            if (word==sport_sce):
                                new=new+"\n"
                                empty_array.append(word)
                                empty_array.append(new)
                            
                                
            if(flag_found==True):
                for index, word in enumerate(empty_array):
                    if(index==0):
                        string1=word
                    elif(index==len(word)-1):
                        string1=string1+" "+word
                    else:
                        string1=string1+", "+word

                for index, word in enumerate(old_array):
                    if(index==0):
                        string2=word
                    elif(index==len(word)-1):
                        string2=string2+" "+word
                    else:
                        string2=string2+", "+word

          
                a_file = open("sport_sce.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[savetheindex] = string1

                a_file = open("sport_sce.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()

                print("Done")
            else:
                print("Error, coach not found")
            admin_login()

#Functionalities of All Student(Registerd/ Not-Registered)
def guest_login():
    print("\n__Welcome Student!__")
    print("\nWhat would you like to do today?")
    print("1. View details")
    print("2. Registered/ Not-Registered Student access")
    print("3. Exit")

    choice = int(input("\nEnter your choice: "))
    
##    try:
    if(choice == 1):
        v_details()
        
    elif(choice == 2):
        check_std()

    elif(choice == 3):         
        print("Program has been terminated.")
        exit()
        
    else:
        print("Please enter within the range again.")
        guest_login()

##    except:
##        print("Please enter a valid number.")
##        guest_login()
        
#View Details
def v_details():
    print("\n__Welcome Student!__")
    print("\nWhat details would you like to view?")
    print("1. Sport")
    print("2. Sport Schedule")

    choice = int(input("\nEnter your choice: "))
    
##    try:
    if(choice == 1):
        dis_sport_std()
        
    elif(choice == 2):
        dis_sport_sce_std()

    else:
        print("Please enter within the range again.")
        guest_login()

##    except:
##        print("Please enter a valid number.")
##        v_details()


def dis_sport_std():
    print ("\n___Sport Records___")
    txtf = open('sport.txt','r')
    content = txtf.read()
    print(content)
    txtf.close()
    guest_login()
    
def dis_sport_sce_std():
    print ("\n___Sport Schedule Records___")
    txtf = open('sport_sce.txt','r')
    content = txtf.read()
    print(content)
    txtf.close()
    guest_login()


#Registerd/ Not- Registered Student
def check_std():
    print("Are you a registered student?")
    print("1. Yes")
    print("2. No")

    while 1:
        
        try:
            choice = int(input("\nEnter your choice: "))
            if (choice == 1):
                student_function()
                
            elif int((choice == 2)):
                std_reg()

            else:
                print("Please enter within the range again.")
                pass

        except:
            print("Please enter a valid number.")
            pass
    
#New Student Registration
def std_reg():
##    try:
    print("Enter your details here:\n")
    std_name = input("Student Name: ")
    std_id = input("Student ID: ")
    std_email = input("Email Address: ")
    std_sport = input("Sport: ")
    std_sport_sce = input("Sport Scehdule: ")
    username = str(input("Enter a username: "))
    password = str(input("Enter a password: "))
    password1 = str(input("Confirm password: "))
    

    if (password == password1):
        txtf = open('student.txt','a')
        txtf.write(username+', '+password+', '+std_id+', '+std_name+', '+std_email+', '+std_sport+', '+std_sport_sce)
        txtf.write('\n')
        txtf.close()
        print("Registration Successful!")
        check_std()

    else:
        print("Please ensure that the password and confirm password are the same.")
        guest_login()


##    except:
##        print("Please do not enter numbers or symbols.")
##        std_reg()


##f = open("students.txt", "a")
##f.write("\n"+student_name+","+student_id+","+student_email)
##f.close()

    
##    f = open("student.txt", "a")
##    f.write("\n"+student_name+","+student_id+","+student_email+","+student_password)
##    f.close()

#Functionalities of Registerd Student
#Student Login 
def student_function():
    print("\n__Student Login__\n")
    std_username = str(input("Username: "))
    std_pwd = str(input("Password: "))

    found = False
    with open('student.txt') as txtf: 
        for line in txtf:
            # get username
            std_username1 = line.split(", ")[0]
            # get password
            std_pwd1 = line.split(", ")[1] #[0:-1] # ady gives list [1] -> 2nd obj, [0:-1] -> from obj, extract word excluding. last letter (\n)
            if ((std_username ==  std_username1) and (std_pwd == std_pwd1)):
                    found = True
                    std_main_menu(std_username)
 
    if (not found):
        print ("\nWrong credentials!")
        conti = int(input("Would you like to retry? (\"1-> Retry, 2-> Quit\"): "))
        if (conti == 1):
            student_function()
        else:
            conti == 2
            guest_login()
    else:
        print("Please enter within range of 1-2.")
        conti = int(input("Would you like to retry? (\"1-> Retry, 2-> Quit\"): "))

        
#Registered Student Access of System - Main Menu
def std_main_menu(std_username):
    print("__Student Main Menu__")
    print("\n1. View Coaches")
    print("2. View Self-Record")
    print("3. View Registered Sport Schedule")
    print("4. Modify Self-Record")
    print("5. Provide Feedback and rate the coach")
    print("6. Exit")

    s_choice = int(input("\nEnter your choice: "))
   
    
    if (s_choice == 1):
        dis_coach_std(std_username)
    
    elif (s_choice == 2):
        dis_std_rec(std_username)

    elif (s_choice == 3):
        dis_sport_sce(std_username)

    elif (s_choice == 4):
        modify_self_rec(std_username)

    elif (s_choice == 5):
        rate_coach(std_username)

    elif (s_choice == 6):
        print("Program has been terminated.")
        exit()

    else:
        print("Please enter a valid input.")
        student_function()

def dis_coach_std(std_username):
    print ("\n___Coach Records___")
    txtf = open('add_records.txt','r')
    
    content = txtf.read()
    print(content)
    txtf.close()
    std_main_menu(std_username)

def dis_std_rec(std_username):
    print ("\n___Student Records___")
    with open('student.txt') as txtf:
            
            for line in txtf:
                for index, word in enumerate(line.split(", ")):
                    if(word==std_username):
                        for index, word in enumerate(line.split(", ")):
                            if (index>1):
                                print(word, end = '     ')
                print("\n")
            std_main_menu(std_username)          

def dis_sport_sce(std_username):
    print ("\n___View Registered Sport Schedule Records___")
    txtf = open('sport_sce.txt','r')
    
    content = txtf.read()
    print(content)
    txtf.close()
    std_main_menu(std_username)
                
#Modify Self Record   
def modify_self_rec(std_username):

    choice=int(input("Which detail would you like to modify?\n1. Name\n2. Email\n3. Registered Sport\n4. Sport Schedule\nChoice: "))
    new =  input("Enter the new value:")
    empty_array=[]
    old_array=[]
    string1=""
    string2=""
    savetheindex=0
    flag_found=False
    with open('student.txt') as txtf:
         
            for index1, line in enumerate(txtf):
                for index, word in enumerate(line.split(", ")):
                    if (word==std_username) and (index==0):
                        flag_found=True
                        savetheindex=index1
                        for index, word in enumerate(line.split(", ")):
                            old_array.append(word)
                            if(index == choice+2):
                                if("\n" in word):
                                    new=new+"\n"
                                empty_array.append(new)
                            else:
                                empty_array.append(word)
                                
            if(flag_found==True):
                for index, word in enumerate(empty_array):
                    if(index==0):
                        string1=word
                    elif(index==len(word)-1):
                        string1=string1+" "+word
                    else:
                        string1=string1+", "+word

                for index, word in enumerate(old_array):
                    if(index==0):
                        string2=word
                    elif(index==len(word)-1):
                        string2=string2+" "+word
                    else:
                        string2=string2+", "+word

         
                a_file = open("student.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[savetheindex] = string1

                a_file = open("student.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()

                print("Done")
            else:
                print("Error, coach not found")
            std_main_menu(std_username)

#Provide feedback and rate the coach
def rate_coach(std_username):

    coach_id= input("Which coach would you like to rate and provide feedback?\nCoach ID: ")
    new=input("Enter Coach Score (range between 1-5): ")
   
    empty_array=[]
    old_array=[]
    string1=""
    string2=""
    savetheindex=0

    
    if (int(new) < 1) or (float(new) > 5):
    
       print("Please enter within the range 1-5.")
       rate_coach(std_username)
       
    flag_found=False
    with open('add_records.txt') as txtf:
             
            for index1, line in enumerate(txtf):
                for index, word in enumerate(line.split(", ")):
                    if (word==coach_id) and (index==0):
                        flag_found=True
                        savetheindex=index1
                        for index, word in enumerate(line.split(", ")):
                            if( "\n" in word):
                                newword=word.replace("\n","")
                                empty_array.append(newword)
                            else:
                                empty_array.append(word)                 

            if(flag_found==True):
                empty_array.append(new)
                empty_array.append("\n")
                print(empty_array)
                for index, word in enumerate(empty_array):
                    if(index==0):
                        string1=word
                    elif(index==len(empty_array)-1):
                        string1=string1+" "+word
                    else:
                        string1=string1+", "+word

                for index, word in enumerate(old_array):
                    if(index==0):
                        string2=word
                    elif(index==len(old_array)-1):
                        string2=string2+" "+word
                    else:
                        string2=string2+", "+word

                print(string1)
                print(string2)
                a_file = open("add_records.txt", "r")
                list_of_lines = a_file.readlines()
                list_of_lines[savetheindex] = string1

                a_file = open("add_records.txt", "w")
                a_file.writelines(list_of_lines)
                a_file.close()

                print("Done. \n Returning to Student Main Menu...")
            else:
                print("Error, coach not found")
            std_main_menu(std_username)              

# Calling defs
main_menu()
