
from NATO_alphabet import alphabet

user_name = list(input('Enter your name: '))
name_NATO = [alphabet[letter.lower()] for letter in user_name]


print(user_name)
print(name_NATO)
