user_input = input("Hello, what is your name? ")

first_letter = user_input[0].upper()

everything_else = user_input[1:].lower()

correct_name = first_letter + everything_else

print("Hello,", correct_name)

# name part finished

brand_question = input("What is your favorite brand? ")


shoes = [{
    "name": "Freeruns",
    "year": 2020,
    "brand": "nike",
    "stock": True,
},
    {
    "name": "Air",
    "year": 2018,
    "brand": "jordan",
    "stock": False,
},
    {
    "name": "High-Top",
    "year": 2021,
    "brand": "sketchers",
    "stock": True,
},
    {
    "name": "oldschool",
    "year": 2016,
    "brand": "Vans",
    "stock": False
}
]



for i in range(4):
    if(brand_question.lower() == shoes[i].get("brand") and shoes[i].get("stock")):
        print(shoes[i].get("brand"), "is currently in stock!")



# found = False


# for i in range(4):
#     if(name_question == shoes[i].get("name")):
#         print(shoes[i].get("name"), "is currently in stock!")
#         found = True
    
    
# if(not found):
#         print("Sorry, piss off!")


# if(name_question == shoes[i].get("name")):
#     print(shoes[i].get("name"), "is currently in stock!")
# else:
#     print("Sorry, piss off!")




