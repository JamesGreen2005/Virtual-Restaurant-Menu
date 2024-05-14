# This code tells if the a specific item is chosen it will check if we have that in the list if it does it will check the price the food is if it finds both it will combine the total for the food and drink if it can neither find the food or drink item it will automatically go to error

def findPrice (listItems, listPrices, userChoice, defaultPrice=0):
  for i in range(len(listItems)):
    if userChoice == listItems[i]:
      price = listPrices[i]
      return price
  return 0
  
  # Return 0 if user's input does not match any items in the list
     
# Displays the food menu and it also displays the cost of the item

food = ["burger","cheese burger","chicken noodle soup","hotdog","chicken sandwich","chicken nuggets","none"]

print ("Randy's Restaurant")

print (" Food Menu")

print(" burger $15 \n cheese burger $20 \n chicken noodle soup $5 \n hotdog $10 \n chicken sandwich $5 \n chicken nuggets $5")

# print text welcomes the customer to randy's restaurant

print()

print ("Hello welcome to Randy's Restaurant What would you like to eat today? If your not that hungry type \nnone and maybe try some of our delicious sides.")

inp1 = input ()

prices = [15,20,5,10,5,5,0]

#this is the side menu it has all the side choices for your main course it prints out the prices for you all you pick is if you want a side or not

print (" Side Menu")

side = ["french fries","onion rings","waffle fries","curly fries","none"]

print (" french fries $2 \n onion  rings $3 \n waffle fries $4 \n curly fries $4")

PricesS = [2,3,4,4,0]

print ("Would you like a side with your", inp1 ,"if not please type none and try one of our drinks or dessert \ninstead.")

inp2 = input ()

# This is when the customer picks out what they would like to drink with their food and side you can pick out a single drink item or type none for no drink 

print(" Drink Menu")

drink = ["coke","ice tea", "dr pepper","water","gatorade","coffee","none"]

print(" coke $2 \n ice tea $3 \n dr pepper $2 \n water $0 \n gatorade $4 \n coffee $5")

pricesD = [2,3,2,2,0,4,5]

print ("Why not wash down your",inp1,"and",inp2,"with one of our many drink \nchoices? If you don't want a beverage please type none.")

inp3 = input ()

# this is the dessert menu you pick out you dessert item here to pair with your maine course,side,and drink if you don't want a dessert item type none 

print(" Dessert Menu")

dessert = ["chocolate chip cookie" , "apple pie","seasonal pie", "strawberry shake","chocolate shake","vanilla shake","none"]

print(" chocolate chip cookie $3 \n apple pie $4 \n seasonal pie $5 \n strawberry shake $10 \n chocolate shake $10 \n vanilla shake $10")

pricesM = [3,4,5,10,10,10,0]

print("How about you try one of our fabulous dessert items I recommend the chocolate chip cookie. \n If you don't feel like having dessert today please type none.")

inp4 = input ()

# This will calculate the total price of your food, side, drink, and dessert if you typed none on either of these choices it won't calculate a price on that item

total = findPrice(food, prices, inp1, defaultPrice=0) + findPrice(side, PricesS, inp2, defaultPrice=0) + findPrice(drink, pricesD, inp3, defaultPrice=0) + findPrice(dessert, pricesM, inp4, defaultPrice=0)

# Displays the total price of the food,drink, and dessert combine

print( "Your total is $",total)

print("have a wonderful day!")



