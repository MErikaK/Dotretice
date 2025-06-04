
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Miloslava Erika Kadeřábková
email: miloslava.kaderabkova@gmail.com
"""
key = input("Who are you?" )
the_known = {"bob":"123", "ann":"pas123", "mike":"password123", "liz":"pass123"}
the_known_keys = the_known.keys()
the_known_values = the_known.values()

if key not in the_known_keys:
   print("I don´t know you. You are an unregistered user! Terminating the program...")
   quit()
else:
    item = input("Do you know the password?" )

if the_known[key] == item:
    print(f"name: {key}")
    print(f"password: {item}")
    print("- - - - - - - - - - - - - - - - - -")
    print(f"Well, it´s you {key}?  Now you can analyse {len(TEXTS)} texts. Choose a number between 1 and {len(TEXTS)}.")
    numero = input("Choose your number and choose it wisely!")
    print("- - - - - - - - - - - - - - - - - -")
elif item == "no" or item == "yes":
    print("The true initiate is the one who knows that the most powerful secret is the one that has no content, because no enemy can force him to reveal it, and no rival can take it from him.")
    quit()
else:
    print("Well, obviously, you don´t know the password, do you?")
    quit()

if numero.isnumeric == False or int(numero) > len(TEXTS):
   print("That wasn´t wise! You shall not pass!")
   exit()
else:
    print(f"You have choosen number {numero}")
    print("- - - - - - - - - - - - - - - - - -")

text = TEXTS[int(numero)-1]

new_text = text.split(" ")
new_text = [x for x in new_text if x != " "]
new_text = [x for x in new_text if x != ""]

titles = 0
upper = 0
lower = 0

for word in new_text:
    if word.istitle():
        titles += 1
    elif word.isupper():
        upper += 1
    elif word.islower():
        lower += 1

numbres = []
for word in new_text:
    if word.isnumeric():
        numbres.append(int(word))

len_word_dictionary = {}
for word in new_text:
    delka = len(word)
    len_word_dictionary[delka] = len_word_dictionary.get(delka,0) + 1

len_word_keys = len_word_dictionary.keys()

print(f"There are {len(new_text)} words in the selected text.")
print(f"There are  {titles} titlecase words.")
print(f"There are  {upper} uppercase words.")
print(f"There are  {lower} lowercase words.")
print(f"There are {len(numbres)} numeric strings.")
print(f"The sum of all the numbers 8 {sum(numbres)}")
print("- - - - - - - - - - - - - - - - - -")
print("LEN|       OCCURENCES       |NR.")
print("- - - - - - - - - - - - - - - - - -")

for key in (sorted(len_word_keys)):
    print(f"{(3-len(str(key)))*" "}{key}|{len_word_dictionary[key]*"*"}{(24-len_word_dictionary[key])*" "}|{len_word_dictionary[key]}")
