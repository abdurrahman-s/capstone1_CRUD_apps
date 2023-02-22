# CAPSTONE PROJECT
# Creator       :   Abdurrahman Saleh Adijaya
# Created on    :   Feb 14, 2023
# Program       :   JCDSOL-009
# Topic         :   CRUD Application - Rental Mobil
# Last Revision :   Feb 22, 2023

# function
def nav01(x): # for user to selection in menu
    a = input(f'Enter selection (1-{x}): ')
    if a.isnumeric():
        a = int(a)
        if a<1 or a>x:a = nav02(x)
    else:
        a = nav02(x)
    return a

def nav02(x): # to prevent user when entering value not in the selection
    a = ''
    while not a.isnumeric():
        print('\n>>>ALERT: Your input is not in the selection.')
        a = input(f'Enter selection (1-{x}): ')
        if a.isnumeric():
            a = int(a)
            if a<1 or a>x:
                a = ''
            else:break
    return a

def nav03(x): # to choose menu display
    if x == 0:print(mainMenu)
    elif x == 1:print(menuRead)
    elif x == 2:print(menuCreate)
    elif x == 3:print(menuUpdate)
    elif x == 4:print(menuDelete)

def menu01(): # to show all data in car database
    if len(carDB)>0:
        print('*** Car Database ***')
        print("ID\t| Brand\t\t\t| Year\t| Transmission\t| Rental Price(Rp)\t| Rental Status")
        for i in range(len(carDB)):
            menu02(i)
    else:
        print(f'\n>>>INFO: Car database is empty')
        print('>>>TIP: Select [2] in main menu to create new data')

def menu02(x): # to show selected data (by ID)
    print(carDB[x]['ID'], '\t|', carDB[x]['Brand'], '\t|', carDB[x]['Year'], 
          '\t|',carDB[x]['Transmission'],'\t|',carDB[x]['Rental Price'],'\t\t|',carDB[x]['Rental Status'])

def sel01(x,y):
    a = ind(x)
    if a != None and y == 1: # menu update if selected ID exist
        print(f'\n* Data with car ID {x} *')
        print("ID\t| Brand\t\t\t| Year\t| Transmission\t| Rental Price(Rp)\t| Rental Status")
        menu02(a)
    elif a != None and y == 2: # menu create if selected ID exist
        print(f'\n>>>INFO: Data with car ID {x} already exist')
        print('>>>TIP: Select [3] in main menu to update existing data')
        return a
    # continue create or update if condition satisfied
    elif (a == None and y == 2) or (a!= None and y == 3):
        return a
    else: # menu update if selected ID doesn't exist
        print(f'\n>>>INFO: Data with car ID {x} does not exist')
        print('>>>TIP: Select [2] in main menu to create new data')

def ind(x): # to check index position of ID entered by user
    for i,d in enumerate(carDB):
        if d['ID'] == x:
            return i
    return None

def dict0(x,y): # to reset temporary dictionary
    global dictTemp
    dictTemp.clear()
    if x == 0:dictTemp = {'ID':'','Brand':'','Year':0,'Transmission':'','Rental Price':0,'Rental Status':''}
    else:dictTemp = carDB[y].copy()

def add0(x): # to update or create data
    a = list(dictTemp.keys())
    if x == 3:print('\n>>>INFO: Enter y for Manual, n for Automatic Transmission')
    elif x == 5:print('\n>>>INFO: Enter y for On Rent, n for Available')
    b = input(f"Enter Car's {a[x]}: ")
    if b == '': 
        print('\n>>>ALERT: Data cannot be empty')
        return 1 # to prevent user from entering empty input
    elif x == 1:
        if len(b)>20: 
            print('\n>>>ALERT: Brand must be less than 20 characters')
            return 1 # to limit user brand input max 20 characters
        else:
            b = ' '.join(i.capitalize() for i in b.lower().split())
            # to add extra space characters if brand input < 20 characters
            if len(b)<20:
                c = ''
                for i in range(20-len(b)):c+=' '
                b = b+c
            dictTemp[a[x]] = b # to insert user brand input to temporary dictionary
    elif x == 3:
        # to choose transmission
        if b.upper() == 'Y':dictTemp[a[x]] = 'Manual'
        elif b.upper() == 'N':dictTemp[a[x]] = 'Automatic'
        else:
            print('>>>ALERT: Enter y/n only to choose transmission')
            return 3
    elif x == 5:
        # to choose rental status
        if b.upper() == 'Y':dictTemp[a[x]] = 'On Rent'
        elif b.upper() == 'N':dictTemp[a[x]] = 'Available'
        else:
            print('>>>ALERT: Enter y/n only to choose rental status')
            return 5
    else:
        # to make sure user only enter number for year and rental price
        if not (b.isnumeric()):
            print(f'\n>>>ALERT: {a[x]} can only be number')
            return 2
        elif x == 2 and (int(b)<1990 or int(b)>2023):
            print(f'\n>>>ALERT: {a[x]} is only valid in range 1990-2023')
            return 2
        else:dictTemp[a[x]] = int(b)

def save(x): # to save or delete data
    a = ''
    if x == 0:a='Save new data?'
    elif x == 1:a='Continue update?'
    elif x == 2:a='Continue delete selected data?'
    while True:
        b = input(f'{a} (y/n): ').upper()
        if b != 'Y' and b != 'N':
            print('\n>>>ALERT: Type y/n only for confirmation.')
        else:
            return b

# variables
mainMenu = '''
        ***** Welcome to Fast Car Rental *****

        You are in the main menu.

        [1] Show cars database
        [2] Create new car data
        [3] Update car data
        [4] Delete existing car data
        [5] Exit program

'''

menuRead = '''
        *** You are in database menu ***

        [1] Show all database
        [2] Input data to show
        [3] Back to main menu

'''

menuCreate = '''
        *** You are in create new data to database menu ***

        [1] Create new data to car database
        [2] Back to main menu

'''

menuUpdate = '''
        *** You are in update database menu ***

        [1] Update existing data in car database
        [2] Back to main menu

'''

menuUpdate1 = '''
        [1]Brand\t\t[4]Rental Price/Day(Rp)
        [2]Year \t\t[5]Rental Status
        [3]Transmission\t\t[6]Save Update
'''

menuDelete = '''
        *** You are in delete data from database menu ***

        [1] Delete existing data in car database
        [2] Back to main menu

'''

carDB = [
    {'ID':'TA1','Brand':'Toyota Avanza  ','Year':2015,'Transmission':'Manual','Rental Price':500000,'Rental Status':'On Rent'},
    {'ID':'HC1','Brand':'Honda Civic    ','Year':2020,'Transmission':'Automatic','Rental Price':1000000,'Rental Status':'Available'},
]

dictTemp = {}

while True:
    nav03(0)
    userNav0 = nav01(5)

    # navigate to menu read [1]
    if userNav0 == 1:
        while True:
            nav03(1)
            userNav1 = nav01(3)
            if userNav1 == 1: # show all data
                menu01()
            elif userNav1 == 2: # show selected data by user
                if len(carDB)<1:
                    print(f'\n>>>INFO: Car database is empty')
                    print('>>>TIP: Select [2] in main menu to create new data')
                else:
                    userInput1 = input('Enter car ID to show data: ').upper()
                    if userInput1 == '':print('\n>>>ALERT: ID cannot be empty')
                    else:sel01(userInput1,1)
            else:break
    
    # navigate to menu create [2]
    elif userNav0 == 2:
        while True:
            nav03(2)
            userNav2 = nav01(2)
            if userNav2 == 1:
                userInput2 = input('Enter car ID to check if data exist: ').upper()
                if userInput2 == '':print('\n>>>ALERT: ID cannot be empty')
                elif len(userInput2) > 4:print('\n>>>ALERT: ID must be less than 4 characters')
                else:
                    ind2 = sel01(userInput2,2)
                    if ind2 == None:
                        print(f'>>>INFO: Car ID {userInput2} does not exist, can continue create.')
                        print(f'\nInput data for car ID {userInput2}')
                        dict0(0,1)
                        dictTemp['ID'] = userInput2
                        counter1 = 1
                        while counter1 < 6: # counter is used to make sure user enter all data
                            create1 = add0(counter1)
                            if create1 == None: counter1+=1
                        userSave = save(0)
                        if userSave == 'Y':
                            carDB.append(dictTemp.copy())
                            print('\n**Save successful**')
            else:break
    
    # navigate to menu update [3]
    elif userNav0 == 3:
        while True:
            nav03(3)
            userNav3 = nav01(2)
            if userNav3 == 1:
                userInput3 = input('Enter car ID to show data: ').upper()
                if userInput3 == '':print('\n>>>ALERT: ID cannot be empty')
                else:
                    ind3 = sel01(userInput3,3)
                    if ind3 != None:
                        print("ID\t| Brand\t\t\t| Year\t| Transmission\t| Rental Price(Rp)\t| Rental Status")
                        menu02(ind3)
                        userConf = save(1)
                        if userConf == 'Y':
                            dict0(1,ind3)
                            while True:
                                print(f'\nChoose data to update on car ID {userInput3}')
                                print(menuUpdate1)
                                userNav3b = nav01(6)
                                if userNav3b != 6:
                                    add0(userNav3b)
                                else: break
                            userSave = save(0)
                            if userSave == 'Y':
                                carDB[ind3] = dictTemp.copy()
                                print('\n**Save successful**')
            else:break
    
    # navigate to menu delete [4]
    elif userNav0 == 4:
        while True:
            nav03(4)
            userNav4 = nav01(2)
            if userNav4 == 1:
                userInput4 = input('Enter car ID to show data: ').upper()
                if userInput4 == '':print('\n>>>ALERT: ID cannot be empty')
                else:
                    ind4 = sel01(userInput4,3)
                    if ind4 != None:
                        print("ID\t| Brand\t\t\t| Year\t| Transmission\t| Rental Price(Rp)\t| Rental Status")
                        menu02(ind4)
                        userDel = save(2)
                        if userDel == 'Y':
                            del carDB[ind4]
                            print('\n**Delete successful**')
            else:break
    else: break