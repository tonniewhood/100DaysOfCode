# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = '[name]'


def main():

    with open('./Input/Names/invited_names.txt', mode='r') as infile:

        for line in infile:
            name = line.strip('\n')
            file_name = f'./Output/ReadyToSend/letter_for_{name}.txt'

            with open('./Input/Letters/starting_letter.txt', mode='r') as template, open(file_name, mode='w') as out_file:

                temp_contents = template.read()
                out_file.write(temp_contents.replace(PLACEHOLDER, name))


main()
