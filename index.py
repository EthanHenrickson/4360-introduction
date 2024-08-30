import sys

option = sys.argv[1].lower()

if option == "/name":
    print("My name is Ethan Henrickson")
elif option == "/why":
    print("I was fascinated by computers growing up and I always wanted to do something in STEM")
elif option == "/what":
    print("I would like to start my own business on the side as I work a regular development job")
elif option == "/fact":
    print("I do photography in my free time")
else:
    print("Sorry that option is not available, please try another option")