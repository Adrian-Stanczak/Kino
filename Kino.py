import json

file_path = 'data/kino.json'

seats = [None]*11

def main():
    while True:
        enter = int(input('Enter, what you wanna do: '))
        match enter:
            case 1 : print_seats(seats)
            case 2 : add_reservation(seats)
            case 3 : remove_reservation(seats)
            case 4 : modify_reservation(seats)
            case 5 : check_availbility(seats)
            case 6 : add_multiple_reservations(seats)
            case 7 : add_multiple_reservations(seats)
            case 8 : cancell_all_reservations(seats)
            case 9 : save_seats_to_file(seats)
            case 10 : load_seats_to_file(seats)
            case 11 : break
    
    

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
    seat_numbers = list(map(int, input('Enter some seats you wanna know that they are available: ').split()))

    result = {"ready to order":[], "reservatited": []}

    for seat_number in seat_numbers:
        if  seat_number >= 1 and seat_number <= 10:
            if seats[seat_number] == None:
                result['ready to order'].append[seat_number]
            else:
                result['reservatited'].append[seat_number]
        else:
            print('Enter correct seat numbers!')

        print(result)


def add_multiple_reservations(seats:list):
    seat_numbers = list(map(int, input('Enter some seats you wanna reservate: ').split()))
    name = str(input('Enter your name: '))
    for seat_number in seat_numbers:
        if seat_number >= 1 and seat_number <= 10:
            if seats[seat_number] == None:
                seats[seat_number] = name
            else:
                print('Enter correct seat number!')
                break
        
    print(seats)

def save_seats_to_file(seats):

    with open(file_path, 'w')as file:
        json.dump(seats, file, indent=4)

def load_seats_to_file(seats):
    pass

def cancell_all_reservations(seats:list):
    name = str(input('Enter your name: '))

    for i, seat in enumerate(seats):
        for seat in seats:
            if seat == name:
                seats[i] = None

    print(seats)

main()


