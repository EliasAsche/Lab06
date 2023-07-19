# Elias Aschenbrenner 
def encoder(string):
    new_string = ''
    for i in range(len(string)):
        if string[i] == '0':
            new_string += '3'
        elif string[i] == '1':
            new_string += '4'
        elif string[i] == '2':
            new_string += '5'
        elif string[i] == '3':
            new_string += '6'
        elif string[i] == '4':
            new_string += '7'
        elif string[i] == '5':
            new_string += '8'
        elif string[i] == '6':
            new_string += '9'
        elif string[i] == '7':
            new_string += '0'
        elif string[i] == '8':
            new_string += '1'
        elif string[i] == '9':
            new_string += '2'
        else:
            pass
    return new_string


def decode(string):
    new_password = ''
    for num in string:
        num = int(num)
        if num == 0:
            new_password += '7'
        elif num == 1:
            new_password += '8'
        elif num == 2:
            new_password += '9'
        else:
            new_password += str(num - 3)
    return new_password


program = True
while program:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print('')
    selection = int(input('Please enter an option: '))
    complete_program = True
    while complete_program:
        if selection == 1:
            original_password = input('Please enter your password to encode: ')
            password_encoded = encoder(original_password)
            print('Your password has been encoded and stored!')
            print('')
            complete_program = False
        elif selection == 2:
            password_decoded = decode(password_encoded)
            print(f'The encoded password is {password_encoded}, and the original password is {password_decoded}.')
            print('')
            complete_program = False
        else:
            complete_program = False
            program = False
