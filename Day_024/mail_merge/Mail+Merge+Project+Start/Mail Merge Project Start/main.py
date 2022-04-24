
# in Ready to send leter_for_[name].txt

# import names
all_names = []

with open("/home/lukas/Documents/GitLab/100_days_of_python/Day_024/mail_merge/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    names = data.readlines()
    for name in names:
        name = name.strip("\n")
        all_names.append(name)

# import starting starting_letter
with open("/home/lukas/Documents/GitLab/100_days_of_python/Day_024/mail_merge/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as starting_letter:
    test = starting_letter.readlines()
    print(test[0])






print(all_names)