# server main code - rishi
# - 
# client main code - lalitha


SERVER SIDE CODE
--------------------------
# def updategamedata(name,turns):
#   f=open("gamedata.txt","a")
#   f.write(f"{name},{turns}\n")
#   f.close()
# def readgamedata():
#   f=open("gamedata.txt","r")
#   data=f.readlines()
#   return data

# class Database - bhagya - CRUD - create,read,update,delete
#  - add_user(username,password,card_no) - return True/False
#  - read_users() - returns list of users

#  - add_debitcars(card_no,balance) - return True/False
#  - read_debitcards() - returns list of debit cards

#  - add_products(prodid,name,price, quantity) - return True/False
#  - update_products(prodid,quantity) - reduce or increase quantity - return True/False
#  - read_products() - returns list of products

#  - add_orders(order_id,username,product_id,status,time) - return True/False
#  - update_orders(order_id,status) - return True/False
#  - read_orders() - returns list of orders



CLIENT SIDE CODE
-------------------------

##MODEL
class StockItem
  product_id
  name
  price
  available_quantity

class Stock
- products = [list of stockitem objects]
- update_stock(stockstring) 
  - empty the products list
  - process the stockstring and create objects for StockItem and append to products list
- display_stock() - print the available products to the customer(below)
"""
MyKart Store
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
"""



# class OnboardingUser - manu
#  - start_registration()
#    - collect username, password, address, phone
#    - server ki data send cheyyali client socket use chesi send() function vadi
     - server daggara nunchi success/fail message collect chesko recv() function tho
#      - success aithe -> registration successful ani print chesi, server nunchi vachina debit card details print cheyyi
       - fail aithe -> registration failed ani cheppi reason print cheyyi. reason server send chesina response lo untadhi(e.g: user already exists)
#    - return True/False

#  - start_login()
#    - collect username and password
#    - server ki data send cheyyali client socket use chesi send() function vadi
     - server daggara nunchi success/fail message collect chesko recv() function tho
#    - if valid, return True
#    - if invalid, return False

# class CartItem
# - product_id
# - name
# - quantity

# class Cart - likitha
# - items =[] -------- items = [(l123,laptop,1),(bs123,speakr,1),(k123,kb,1)]
# - add_to_cart(product_id,name,quantity) - return True/False
# - update_item_quantity(product_id,quantity) - return True/False
# - remove_from_cart(product_id) - return True/False
# - view_cart() - returns list of items in cart
# - checkout(debit_card_no) - return True/False
