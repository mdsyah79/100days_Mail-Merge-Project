# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
TEXT_TO_REPLACE = "[name]"

# TODO: readlines() names from file and store as namelist
with open("./Input/Names/invited_names.txt") as fnamelist:
    namelist = fnamelist.readlines()

# TODO: file open as write, replace() keyword with name
with open("./Input/Letters/starting_letter.txt") as startletter:
    content = startletter.read()

for name in namelist:
    name = name.strip()
    content = content.replace(TEXT_TO_REPLACE, name)

    # TODO: save file with name of the person and save in output folder
    sendingletter = open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w")
    sendingletter.write(content)
