
def calculator_app():
    # Ask for 1st number
    input_is_number = False
    first_number = None
    while not input_is_number:
        first_number = input('? Number 1 : ')
        try:
            first_number = int(first_number)
            input_is_number = True
        except ValueError:
            print('Please enter whole numbers only\n')

    # Ask for operation (-+\*)
    operations = ('+', '-', '*', '/')
    valid_operation = False
    operation = None
    while not valid_operation:
        operation = input('Choose operation? ( - + / * ) : ')
        if operation not in operations:
            print('Not valid operation')
        else:
            valid_operation = True
    # Ask for 2nd number

    input_is_number = False
    second_number = None
    while not input_is_number:
        second_number = input('? Number 2 : ')
        try:
            second_number = int(second_number)
            input_is_number = True
        except ValueError:
            print('Please enter whole numbers only\n')

    print(f'\nRequired calculation:\n{first_number} {operation} {second_number}\n')

    # Make calculation
    function_result = None
    if operation == '+':
        function_result = first_number + second_number
    elif operation == '-':
        function_result = first_number - second_number
    elif operation == '*':
        function_result = first_number * second_number
    elif operation == '/':
        function_result = first_number / second_number

    # Display results
    print(f'Calculation ended.\nThe result is: {function_result}')
    return function_result

greetings = ('''
╔═╗┌─┐┌─┐┌┬┐  ╔╗ ┬ ┬┌─┐
║ ╦│ ││ │ ││  ╠╩╗└┬┘├┤ 
╚═╝└─┘└─┘─┴┘  ╚═╝ ┴ └─┘
''', '''
╔═╗┌─┐┬  ┌─┐┬ ┬┬  ┌─┐┌┬┐┌─┐┬─┐
║  ├─┤│  │  │ ││  ├─┤ │ │ │├┬┘
╚═╝┴ ┴┴─┘└─┘└─┘┴─┘┴ ┴ ┴ └─┘┴└─
┌┐ ┬ ┬  ╦ ╦╔╗╔╦╗╦╔═╗╔╦╗       
├┴┐└┬┘  ║║║╠╩╗║ ║╚═╗ ║        
└─┘ ┴   ╚╩╝╚═╝╩ ╩╚═╝ ╩        
''')

print(greetings[1])

final_result = 0

keep_calculating = True
while keep_calculating:
    result = calculator_app()
    final_result = final_result + result
    answers = ('y', 'n')
    correct_answer = False
    while not correct_answer:
        print(f'The current total is {final_result}')
        answer = input('\nKeep calculating? ( y / n ) : ')
        if answer not in answers:
            print('Please answer correctly (y/n)')
        elif answer == 'n':
            print(f'\nCalculation ended.\nFinal result: {final_result}\n\nThank You for using this app!\nHave a great day!')
            print(greetings[0])
            correct_answer = True
            keep_calculating = False
        else:
            correct_answer = True

