def start():
    print('Welcome!')
    people_dictionary = {'brett' : ['Male', 'Weight 175'],
                         'nancy' : ['Female', 'Weight 125'],
                         'patrick':['Male', "Weight 195"],
                         "adam":["Male","Weight 215"]}
    Name = input('Please type in a name: ').lower()
    print("You typed in the name " + Name.capitalize())
    try:
        Persons_Data=people_dictionary[Name]
        print('Name: ' +Name.capitalize())
        print("Sex: " + Persons_Data[0])
        print("Weight: " + Persons_Data[1])
        more()
    except:
        print('That name, ' + Name + ', was not found in the dictionary.')
        more()
def more():
    More = input('Would you like to search for another name?: ')
    if More == 'No':
        quit()
    if More == 'Yes':
        start()
    else:
        print('Please enter Yes or No.')
        more()
start()
