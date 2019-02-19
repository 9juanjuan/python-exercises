hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': []
  }
}

empty_room = []
check_in_out = input('Would you like to check in or check out?\n')
floor_number =  str(input('What is your floor number?\n'))
room_number = str(input ('what is your room number?\n'))
if check_in_out == "check in":
  for floor in hotel:
        for room in hotel[floor]:
            if room == room_number and any(hotel[floor][room][0:]):
              print ('Room %s is already occupied. Lets try another room' %(room))
        
#Checking in, takes in occupants and creates empty array of occupants
if check_in_out == "check in":
    num_of_occupants = int(input('How many people checking in?\n'))
    if num_of_occupants == 1 :
        name_of_occupant =  input('What is your name?\n')
        filling_in_room = [name_of_occupant]
    elif num_of_occupants > 1 :
        occupant_one = input('Who is the first person?\n')
        occupant_two = input('Who is the second person?\n')
        occupant_three = input('Who is the third person? If no others, type 0\n')
        occupant_four = input ('Who is the last person? if no last person, type 0\n')
        filling_in_room = [occupant_one, occupant_two, occupant_three, occupant_four]
        print (filling_in_room)
    #Checks for occupied room
    for floor in hotel:
        for room in hotel[floor]:
            if room == room_number and any(hotel[floor][room][0:]):
              print ('Room %s is already occupied. Lets try another room' %(room))
            
            elif room == room_number:
              hotel[floor][room][0:] = filling_in_room
              print ('The following guests are now checked in: {}.'.format(', '.join(filling_in_room)))

                # if room contains empty string, allow check in
                # if hotel[floor[room][0:]== []:
                #     print ("Sorry, Occupied")
                #     continue
elif check_in_out == "check out": 
    for floor in hotel:
        for room in hotel[floor]:
            if room == room_number and any(hotel[floor][room][0:]):
                hotel[floor][room][0:]= empty_room
                print (hotel[floor][room][0:])
            # elif room == room_number and not any(hotel[floor][room][0:]):
            #   print ('You cant check out of an empty room dingus...')
