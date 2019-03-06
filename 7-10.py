#Dream Vacation
responses = {}
#makes sure that the program is running
active = True


while active:
    name = input("What is your name: ")
    response = input('Do you like the beach? yes/no: ')
    response = response.lower()

    if response != 'yes' and response != 'no':
        response = input('Do you like the beach? yes/no: ')

    responses[name] = response

    response2= input('If you could go one place where would you go?: ')
    responses['place'] = response2


    again = input('Play again? yes/no: ')
    if again == 'no':
        active = False
for name in responses:
    print (name + ' said ' + responses[name] + ' I would like to go to the beach.')
    print (name + ' wants to go to ' + str(responses['place']))

