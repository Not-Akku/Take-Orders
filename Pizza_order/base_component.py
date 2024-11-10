# Function for take away or delivery...
def take_away():

  print("Hi sir, welcome to Dream Pizza shop")
  print("\nWe are providing pick up and delivery options for pizza orders!")
  # Loop question for asking the user want to receive through take away or delivery...
  while True:
    receive = input(
      "\nHow do you like to receive your order either pickup or delivery? ").lower()

    if receive == "pickup" or receive == "pick up":
      pickup()
      break

    elif receive == "delivery":
      delivery()
      break

    else:
      print("Please answer pick up or delivery")


# Funtion for pick up...
def pickup():
  name = input("Enter customer's name please: ")
  print("Here is the available pizzas.")
  print("\nHere are the avilable pizzas and their prices")
  print("_____________________________________________")

  # Printing the pizza list and their prices...
  for i in range(len(pizza)):
    print("{}".format(i + 1) + '\t' + pizza[i] + '\t ' + price[i])

  print()
  # Made a list just to carry the number outside the while loop...
  num_pizza = []
  while True:

    try:
      num = int(input("How many pizza would you like to order? maximum is 5: "))
      num_pizza = num
      if num_pizza > 5 or num_pizza < 1:
        print("Invalid number, please enter a valid number!")
        continue
      break

    except ValueError:
      print("Please enter a number!")

  print(num_pizza)

  # variable for cost and a list for user order...
  user_order_prices = []
  total_cost = 0.0
  user_order = []
  # Asking for number of pizza order...
  for i in range(num_pizza):
    while True:
      try:
        menu_num = int(
          input("Enter the pizza number your {} pizza order: ".format(i+1)))
        if 1 <= menu_num <= 12:
          chosen_pizza = pizza[menu_num-1]
          user_order.append(chosen_pizza)
          if 1 <= menu_num <= 7:
            total_cost = total_cost + 8.50
            user_order_prices.append(8.50)
          elif 8 <= menu_num <= 12:
            total_cost = total_cost + 13.50
            user_order_prices.append(13.50)
          break
        else:
          print("Please enter a valid number!")

      except ValueError:
        print("Enter a valid number!")

  # Printing the info, order, and price...
  print('\n' + name)
  print("You have ordered:")
  for i in range(len(user_order)):
    print('\t' + user_order[i] + ":-" +'\t' + str(user_order_prices[i]))

  print("Total amount will be ${}.".format(total_cost))

  # Ready for next order
  next_order = input("\nDo you want to place another order? ").lower()
  while next_order not in ("yes" , "no"):
    print("Please enter yes or no!")
    next_order = input("Do you want to place another order? ").lower()

  if next_order == "yes":
    take_away()
  else:
    print("Thank you so much for your order!")


# Funtion for delivery...
def delivery():
  print("Please provide your details!")
  name = input("Name: ")
  address = input("Address: ")
  while True:
    try:
      phone_num = int(input("Phone number: "))
      break

    except ValueError:
      print("Please Enter your phone number!")

  print("Here are the avilable pizzas and their prices")
  print("_____________________________________________")
  # Printing list of pizza...
  for i in range(len(pizza)):
    print("{}".format(i + 1) + '\t' + pizza[i] + '\t ' + price[i])

  print()
  # made a array just to carry the number outside the while loop...
  num_pizza = ""
  while True:
    # try except for number error...
    try:
      num = int(input("How many pizza would you like to order? maximum is 5: "))
      num_pizza = num
      if num_pizza > 5 or num_pizza < 1:
        print("Invalid number, please enter a valid number!")
        continue
      break

    except ValueError:
      print("Please enter a number!")

  # a variable for cost and menu number...
  total_cost = 0.0
  # adding the delivery charge to the total charge...
  total_cost = total_cost + 3
  # a list for pices of user order...
  user_order_prices = []

  menu_num = ""

  print(num_pizza)
  user_order = []

  for i in range(num_pizza):
    while True:
      try:
        menu_num = int(input("Enter the pizza number your {} pizza order: ".format(i+1)))
        if 1 <= menu_num <= 12:
          chosen_pizza = pizza[menu_num-1]
          user_order.append(chosen_pizza)
          if 1 <= menu_num <= 7:
            total_cost = total_cost + 8.50
            user_order_prices.append(8.5)
          elif 8 <= menu_num <= 12:
            total_cost = total_cost + 13.50
            user_order_prices.append(13.5)
          break
        else:
          print("Please enter a valid number!")

      except ValueError:
        print("Enter a valid number!")

    # checking and appending to user order list


  print('\n' + name)
  print(address)
  print(phone_num)
  print("\nYou have ordered: ")
  for i in range(len(user_order)):
    print('\t' + user_order[i] + ":-" +'\t' + str(user_order_prices[i]))

  print("\nTotal amount will be ${}.".format(total_cost))
  print("Delivery charge included!($3)")
  # for next order...
  next_order = input("\nDo you want to place another order? ").lower()

  while next_order not in ("yes" , "no"):
    print("Please enter yes or no!")
    next_order = input("Do you want to place another order? ").lower()

  if next_order == "yes":
    take_away()
  else:
    print("Thank you so much for your order!")



# Pizza list just for displaying the menu considering easy to read...
pizza = [
    "Bella Pizza           ", "Caprese pizza         ",
    "Neapolitan pizza      ", "Sicilian pizza        ",
    "Pizza Margherita      ", "Detroit pizza         ",
    "New York style pizza  ", "Pizza Quattro formaggi",
    "Chicago pizza         ", "Pepperoni             ",
    "Bagel pizza           ", "Marinara              "
]
# Price for displaying menu...
price = [
    '($8.50)', '($8.50)', '($8.50)', '($8.50)', '($8.50)', '($8.50)','($8.50)',
  '($13.50)', '($13.50)', '($13.50)', '($13.50)', '($13.50)'
]

# calling take away function...

take_away()