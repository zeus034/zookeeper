animals = [camel, lion, deer, goose, bat, rabbit]

# write your code here
while True:
   selection = input("Please enter the number of the habitat you would like to view: ")
   if selection == "exit":
      break
   else:
      print(animals[int(selection)])
   print("See you later!")
