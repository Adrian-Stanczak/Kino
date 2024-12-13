seats = [None]*11

def main():
    while True:
        enter = int(input('Enter, what you wanna do: '))
        match enter:
            case 1 : print_seats(seats)
            case 2 : add_reservation(seats)
            case 3 : remove_reservation(seats)
            case 5 : break
    
    

def print_seats(seats:list):
    print(seats)

def add_reservation(seats:list):
    #name:str, seat_number:int
    name = str(input('Enter name: '))
    name.capitalize()
    seat_number = int(input('Enter seat number: '))

    while seat_number >= 1 and seat_number <=10:
    
        if seats[seat_number] == None:
            seats[seat_number] = name
            print(seats)
            break
        else:
            print('We got only 10 seats !')
            break

def remove_reservation(seats:list):
    #seat_number:int
    seat_number = int(input('Enter seat number: '))

    while seat_number >= 1 and seat_number <= 10:
        if seats[seat_number] != None:
            seats[seat_number] = None
            print(seats)
            break
        else:
            print('Enter correct seat number! ')
            break
    

def modify_reservation(seats:list):
    #seat_number:int, name:str
    seat_number = int(input('Enter seat number: '))
    name = str(input('Enter correct name: '))

    while seat_number >= 1 and seat_number <= 10:
        if seats[seat_number] != None:
            seats[seat_number] = name
            print(seats)
            break
        else:
            print('Enter correct seat number!')
            break

def check_availbility(seats:list):
    pass
main()


