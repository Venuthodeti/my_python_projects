NAME_CONST="[name]"

with open("input/Names/invited_names.txt", "r") as file:
    names=file.readlines()
with open("input/Letters/starting_letter.txt") as file:
    letter_contents=file.read()
for name in names:
    name_stripped=name.strip()
    new_letter=letter_contents.replace(NAME_CONST,name_stripped)
    with open(f"./Output/ReadyToSend/letter_for_{name_stripped}.txt","w") as letter_file:
        letter_file.write(new_letter)





