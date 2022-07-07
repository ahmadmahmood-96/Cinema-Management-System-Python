
print("Welcome to Our Cinema")                #Printing the name of system
def main():                                   #Defining the main function
    check = "Y"                               #Initializing the variable
    while check == "Y":                       #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data = int(input("1)Current Shows, 2)Bookings, 3)Exit: ")) #Taking input from user  
                break                         #Loop ends
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data == 1:                         #If data is equal to 1
            Current_Shows()                   #Call out the function of workshop Shows
            check = "a"                       #changing the value of check
        elif data == 2:                       #If data is equal to 2
            Bookings()                        #Call out the function of Customer Shows
            check = "a"                       #changing the value of check
        elif data == 3:                       #If data is equal to 4
            print("Program Ends")             #Print this statement
            check = "a"                       #changing the value of check
            break                             #Break the loop
        else:                                 #If data is equal to any number
            print("Invalid Input. Enter from the given choices")

def Current_Shows():                          #Defining the Current shows function
    check = "Y"                               #Initializing the variable
    while check == "Y":                       #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data1 = int(input("1)Add Shows, 2)View Shows, 3)Search Shows, 4)Edit Shows, 5)Delete Shows, 6)Back: ")) #Taking input from user
                break                         #breaking the loop
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data1 == 1:                        #If data1 is equal to 1
            Add_Shows()                       #Call out the function of add Shows
            break                             #breaks the loop
        elif data1==2:                        #If data1 is equal to 2
            View_Shows()                      #Call out the functio of view  Shows
        elif data1==3:                        #If data1 is equal to 3
            Search_Shows()                    #Call out the function of search Shows
        elif data1==4:                        #If data1 is equal to 4
            Edit_Shows()                      #Call out the function of edit Shows
        elif data1==5:                        #If data1 is equal to 5
            Delete_Shows()                    #Call out the function of delete Shows
        elif data1==6:                        #If data1 is equal to 6
            main()                            #Call out the main function
            break                             #loop breaks
        else:                                 #If data1 is equal to any number
            print("Invalid Input. Enter from the given choices")

Shows = {}                                    #Creating empty dictionary
def Add_Shows():                              #Defining add shows function
    while True:                               #Applying while loop
        Name = input("Enter movie name in caps: " )                      #Taking input from the user
        break                                 #Loop breaks
    if Name in Shows.keys():                  #Cheking ID exist in keys of dictionary or not
        print("Movie Already Exists. Please Enter another movie name")   #If already exist print this statement
        Add_Shows()                           #Call out the funtion of add Workshop records
    else:                                     #If not exist
        Hall = input("Enter the cinema hall number: ")                   #Taking input from user
        Time = input("Enter the time of the show: ")                     #Taking input from user
        Tickets = int(input("Enter the number of tickets available: "))    #Taking input from the user
        Date = input("Enter the date(DD/MM/YYYY): ")                     #Taking input from the user

        Shows[Name] = [Hall, Time, Tickets, Date]                        #Appending attributes in dictionary
        option = input("Enter Yes to Add Further Record: ")              #Taking input for entering further records or not
        if option == "Yes":                   #Applying condition                
            Add_Shows()                       #Calling out the function
        else:                                 #If option != Yes
            Current_Shows()                   #Calling out the function

def View_Shows():                             #Defining view Workshop record function
    if len(Shows)>0:                          #Applying condition
        print("Name   \tHall   \tTime    \tTickets    \tDate")                      #Print this statement
        for k in Shows.keys():                #Assigning ID's to k
            val = Shows[k]                    #Assigning variable
            print(k,"\t",val[0], "\t",val[1],"\t",val[2], "\t" , val[3]) #Print all records
    else:                                     #If condition id false
        print("Enter records first")          #Print this statement

def Search_Shows():                           #Defining search Workshop record function
    if len(Shows)>0:                          #Applying condition
        while True:                           #Applying while loop
            Name = input("Enter movie name in caps: " )                  #Taking input fron the user
            break                             #Loop breaks
        if Name in Shows.keys():              #If id exist in keys of dictionary
            print("Name   \tHall\tTime\tTickets\tDate")                  #Print this statement
            val = Shows[Name]                 #Assigning ID's to k
            print(Name,"\t", val[0],"\t", val[1],"\t", val[2],"\t", val[3])                         #Print records
        else:                                 #If condition is false
            print("Movie not Found. Please Enter Correct movie name and in caps to Search Records") #Print this statement
            Search_Shows()                    #Call out the function
    else:                                     #If condition is false
        print("Enter record first")           #Print this statement

def Edit_Shows():                             #Defining the funtion of edit Workshop records
    if len(Shows)>0:                          #Applying condition
        while True:                           #Applying while loop
            Name = input("Enter movie name in caps: " )                      #Taking input from the user
            break                             #Loop breaks
        if Name in Shows.keys():              #Cheking ID exist in keys of dictionary or not
            Hall = input("Enter the cinema hall number: ")                   #Taking input from user
            Time = input("Enter the time of the show: ")                     #Taking input from user
            Tickets = int(input("Enter the number of tickets available: "))  #Taking input from the user
            Date = input("Enter the date(DD/MM/YYYY): ")                     #Taking input from the user

            Shows[Name] = [Hall, Time, Tickets, Date]                        #Appending attributes in dictionary
        else:                                 #If condition is false
            print("Please Enter Correct movie name and in caps to Edit Records")
            Edit_Shows()                      #Call out the function
    else:                                     #If coditions false  
        print("Enter Record first")           #Print this statement

def Delete_Shows():                           #Defining the function of delete Workshop records
    if len(Shows)>0:                          #Applying condition
        while True:                           #Applying while loop
            Name = input("Enter movie name in caps: " )                      #Taking input fron the user
            break                             #Loop breaks
        if Name in Shows.keys():              #Applying condition
            del Shows[Name]                   #Deleting id
            print("Deleted Successfully")     #Print this statement
        else:                                 #If coditions false
            print("Movie not Found. Please Enter Correct movie name and in caps to Search Records") #Print this statement
            Delete_Shows()                    #Call out the function
    else:                                     #If coditions false
        print("Enter Record first")           #Print this statement
        
Booking = {}
def Bookings():                               #Defining the function of reservations
    check = "Y"                               #Initializing the variable
    while check == "Y":                       #Applying while loop
        while True:                           #Applying while loop
            try:                              #Checking
                data3 = eval(input("1)Add Bookings, 2)View Bookings, 3)Back: ")) #Taking input from the user
                break                         #Loop breaks
            except:                           #Checking
                print("Enter digits only")    #Print this statement
        if data3 == 1:                        #If input is equal to 1
            Add_Bookings()                    #Call out the function of add reservation
        elif data3 == 2:                      #If input iss equal to 2
            View_Bookings()                   #Call out the function of view reservation
        elif data3 == 3:                      #If input is equal to 3
            main()                            #Call out the main function
            break                             #Loop breaks
        else:                                 #If input is equal to any value
            print("Invalid Input. Enter from given choices") #Print this statement
            Bookings()                        #Call out the function of reservations

def Add_Bookings():
    if len(Shows) > 0:
        View_Shows()
        Name = input("Enter movie name in caps: " )                              #Taking input from the user
        if Name in Shows.keys():              #Cheking ID exist in keys of dictionary or not
            Dt = Shows[Name][3]
            Hal = Shows[Name][0]
            Tim = Shows[Name][1]
            Available_Tickets = Shows[Name][2]#Creating variable of available tickets which are at 4 index
            if Available_Tickets == 0:        #Applying condition
                print("No Tickets are available for the movie!")                 #Print this statement
            else:
                print(Available_Tickets,"Tickets are available for this movie",end=". ") #Print this statement
            name = input("Enter the name of the customer: ")
            while True:                       #Applying while loop
                try:                          #Checking
                    ticket = eval(input("How many tickets you want to book: "))      #Taking input from the user
                    break                     #Loop breaks
                except:                       #Checking 
                    print("Enter digits only")                           #Print this statement
            if ticket <= Available_Tickets:                              #If ticket booked is less than available tickets
                Left = (Available_Tickets) - (ticket)                    #Subtract available tickets from booked tickets
                print(ticket, "Tickets are confirmed")                   #Print this statement
                Shows[Name][2]= Left                                     #Creating variable of left tickets
                Booking[name] = [Name, Dt, Hal, Tim,ticket]              #Appending the attributes to key
            else:                                                        #If tickets are not available
                print("Sorry", ticket,"Tickets are not available")       #Print this statement
        else:                                 #If condition is false
            print("Movie not Found. Please Enter Correct movie name and in caps for Bookings")      #Print this statement
    else:
        print("Sorry there is no show available.")

def View_Bookings():
    if len(Booking) > 0:
        print("Name\tMovie name\tHall\tTime\tTickets")                           #Print this statement
        for k in Booking.keys():              #Applying loop for printing the records
            val = Booking[k]                  #Determining the index of key
            print(k,"\t" , val[0], "\t" ,val[2],"\t",val[3],"\t",val[4])             #Print all records
    else:                                     #If coditions false
        print("No Record is Available")       #Print this statement
main()                                        #Call out the main funtion

