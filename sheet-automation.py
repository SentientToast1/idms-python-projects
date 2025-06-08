import openpyxl as opx

wb = opx.load_workbook('intern_list.xlsx')

sheet = wb.active

def searchFunc(name):
    for i in range(2, sheet.max_row + 1):
        if sheet['A'+str(i)].value == name:
            return str(i)
    print("name doesnt exist")
    return None
    


def invokeSearch():
    while True:
        name = input("Enter Name: ")
        searched = searchFunc(name)
        if searched != None:
            return searched
        else:
            option = input("do u want to exit y/n: ")
            if option == 'y' or option == 'Y':
                return None

def dispActive(cell):
    if cell != None:
        print("Name: " + sheet['A'+cell].value)
        print("Join Date: " + str(sheet['B'+cell].value))
        print("Duration: "+ sheet['C'+cell].value)
        print("Project: " + sheet['D'+cell].value)
    else:
        print("object does not exist")

