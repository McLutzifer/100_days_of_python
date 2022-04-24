PLACEHOLDER = "[name]"
# in Ready to send leter_for_[name].txt

# import names
all_names = []

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        name = name.strip("\n")
        all_names.append(name)

# import starting starting_letter
with open("./Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    print(letter[0])

    for name in all_names:
        personal_letter = letter.replace(PLACEHOLDER, name)
        
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as completed_letter:
            completed_letter.write(personal_letter)
