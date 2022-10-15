"""
Welcome to the first Virtual Tour Guide in Nigeria. If you are looking for a place to visit in Nigeria,
# and maybe have decided to visit Nigeria, this Virtual AI Chatbox will guide you through things to expect
and places to visit in Nigeria to make your visit to Africa one of the best.

Other cities will soon be added once app is fully developed.
"""
print("Nigeria is the largest black nation in the world with over 200 million population.")
print("60% of the entire population is young.")
firstname = input("What is your firstname? ")
lastname = input("What is your lastname?")
print("Hello " + firstname + ", What would you like to do in Nigeria this time")
purpose = input("Business or Pleasure? ")
try:
    value = "Business"
except ValueError:
    print("Please choose")
if purpose == "Business":
    print("Cool! So " + firstname + ",if you are in Nigeria for business,you would want to visit Lagos and Abuja.")
    print("Let's start with " + " Lagos. This state boast of about 40 million total population and often tagged as ")
    print("the 'New York' of Africa.")
elif purpose == "Pleasure":
    print("Lagos is an extremely versatile State in Nigeria and also ")
    print("a top destination for visitors seeking pleasure in Africa.")
    print("Here are the list of must visit places in Lagos to make your visit super worthwile.")
    print("Elegushi Beach, Quilox Bar, Eko Atlantic, and lots more.")
else:
    print("I can't understand what you typed " + firstname + ".")




