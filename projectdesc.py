
# server main code - rishi
# - 
# client main code - lalitha


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

# class OnboardingUser - manu
#  - start_registration()
#    - collect username, password, address, phone
#    - add data to file using Database class
#    - create a debit card with 1L balance, card no should be unique, create it using the last debit card no in file
#    - return True/False

#  - start_login()
#    - collect username and password
#    - verify username and password
#    - if valid, return True
#    - if invalid, return False

# class Cart - likitha
# - items =[] -------- items = [(l123,1),(bs123,1),(k123,1)]
# - add_to_cart(product_id,quantity) - return True/False
# - remove_from_cart(product_id) - return True/False
# - view_cart() - returns list of items in cart
# - checkout(debit_card_no) - return True/False

