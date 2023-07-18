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
    return new_string

input()

print(encoder(old))