user_input = input("Hello, what is your name? ")

first_letter = user_input[0].upper()

everything_else = user_input[1:].lower()

correct_name = first_letter + everything_else

print("Hello,", correct_name)

# name part finished

name_question = input("What is your favorite brand? ")


# stock = {
#     "name": "Freeruns",
#     "brand": "Nike",
#     "year": 2021,
#     "brand": True,
# }
shoes = [{
    "name": "Freeruns",
    "year": 2020,
    "brand": True,
},
    {
    "name": "Air",
    "year": 2018,
    "brand": True,
},
    {
    "name": "High-Top",
    "year": 2021,
    "brand": True,
},
    {
    "name": "Oldschool",
    "year": 2016,
    "brand": False
}
]


if(name_question == shoes[0].get("name")):
    print(shoes[0].get("name"), "is currently in stock!")
else:
    print("Sorry, piss off!")


# food = ["Apple", "Banana", "Coconut"]

# if("apple" in food): 
#     print("We got Apple")


# if(freeruns.get("year") > 2020):
#     print(freeruns.get("name"), "is a new shoe" )


# elif(freeruns.get("year") == 2020):
#     print(freeruns.get("name"), "is a used shoe")


# else:
#     print(freeruns.get("name"), "is an old shoe")
# #
# if(freeruns.get("brand") == True):
#         print("Also, it is brand!")
# else:
#     print("It is not a brand..")
