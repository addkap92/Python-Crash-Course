favorite_languages = {
    'jen': 'c',
    'james': 'python',
    'el': 'java'
}

poll_takers = ['jen', 'james', 'el', 'erin']

for person in poll_takers:
    if person in favorite_languages.keys():
        print("Thank you " + person.title() + " for taking the poll!")
    else:
        favorite_languages[person] = input(person.title() + " please take our poll. What is your favorite language? ")
print("\n")
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + "!")

    # if 'erin' not in favorite_languages.keys():
    #     favorite_languages ['erin'] = input("Erin please take our poll: ")
    #
    # print(favorite_languages)
    # print("Languages mentioned: ")
    # for languages in set(favorite_languages.values()):
    #
    #     print(languages.title())
