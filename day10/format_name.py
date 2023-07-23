# Functions with Outputs

def format_name(f_name, l_name):
    formatted_first_name = f_name.capitalize()
    formatted_last_name = l_name.capitalize()
    return f'{formatted_first_name} {formatted_last_name}'


first_name = input('Please enter your first name: ')
last_name = input('Please enter your last name: ')
print(format_name(first_name, last_name))