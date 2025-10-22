# server main code - rishi
# - 
# client main code - lalitha

- fail aithe -> registration failed ani cheppi reason print cheyyi. reason server send chesina response lo untadhi(e.g: user already exists)

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
VIEW
server ni connect avvadaniki socket create cheyyandi
socket=socket.socket()
client_socket,client_addr=socket.connect(('192.3.3.3',9999))
- connected to server ani print chyyali
Cart and Stock classes ki objects create cheyyandi
(variable names)
- cart
- stock

user_loggedin=True/False
user_wallet_balance=False/number

handleonboarding()
- welcome screen display cheyyali
- using l,r,e ane options ni batti login details ledha registration details input() ni use chesi collect cheskovali
- collect cheskonnna data ni OnboardingUser classes lo unna methods ni call cheyyali
- registration process
    - pass collected data to start_registration() function
    - if True returned 
      - registration successful ani print chesi
      - welcome screen print again
    - if true return avvakunte
      - message print chesi malli welcome screen ni print cheyyali
- login process
    - pass collected data to start_login() function
    - if (True,string) return aithe
      - login successful ani print chesi
      - stock object ni vachina string tho update cheyyali using update_stock() function
      - user_loggedin ni True cheyyali
      - return True 
    - if (false,string) return aithe
      - message print chesi malli welcome screen ni print cheyyali

User login avvagane 1 threads start avvali
- server ninchi stock data vachinapudu stock object ni update cheyyali
- oka function with name run_stock_updater() ni create chesi danini thread lo run cheyyali

dispaly_stock_cart_wallet()
- cart and stock variable ni use chesi stock and cart ni display cheyyali kinda ichina format lo



MODEL
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




# class OnboardingUser - manu
#  - start_registration(name,password,address,phoneno)
#    - server ki data send cheyyali client socket use chesi send() function vadi
        - "registration:name,password,address,phoneno"
     - server daggara nunchi success/fail message collect chesko recv() function tho
        - success aithe -> "success"
        - fail aithe -> "fail:reasonmessage"
#    - success/fail aithe -> return True/"reasonmessage"

#  - start_login(username,password)
#    - server ki data send cheyyali client socket use chesi send() function vadi
        - "login:username,password"
     - server daggara nunchi success/fail message collect chesko recv() function tho
        - success aithe -> "success:l123,laptop,20000,5|m123,mouse,300,9&wallet_balance"
        - fail aithe -> "fail:reasonmessage"
#    - if success, return : (True, tharvatha unna string ni return cheyyali)
#    - if fail, return (False,"reasonmessage")


# Dummy server for testing OnboardingUser class


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




"""
Case-1: Cart empty unnapudu
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Wallet Balance: Rs.100000
Enter your input:

Case-2: Cart lo items unnapudu
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
Cart total: 68300
Wallet Balance: Rs.100000
Cart Options : add,edit(e),remove(r),buy(b)
Enter your input:

WHEN ADDING TO CART
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
Cart total: 68300
Cart Options : add,edit(e),remove(r),buy(b)
Enter your input:2

Step-2
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
------------------------
Enter the Keyboard quantity you want to buy(ENTER-default to 1): 2

Step-3
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
3.Keyboard qt:2 -Rs.1600
Cart total: 68300
Cart Options : add,edit(e),remove(r),buy(b)
Enter your input:




EDITING THE CART
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
Cart total: 68300
Cart Options : add,edit(e),remove(r),buy(b)
Enter your input:e1

Step-2
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
------------------------
Enter the new quantity for Laptop: 1

Step-3
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:1 - Rs.34000
2.Mouse qt:1 - Rs.300
Cart total: 34300
Cart Options : add,edit,remove,buy
Enter your input:




REMOVING AN ITEM FROM CART
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
Cart total: 68300
Cart Options : add,edit,remove,buy
Enter your input:r2

Step-2
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
Cart total: 68000
Cart Options : add,edit,remove,buy
Enter your input:




BUYING THE ITEMS IN THE CART
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
1.Laptop qt:2 - Rs.68000
2.Mouse qt:1 - Rs.300
Cart total: 68300
Wallet Balance: Rs.100000
Cart Options : add,edit,remove,buy
Enter your input:b

Step-2
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Order placed successfully! Total amount: Rs.68300
Wallet Balance: Rs.31700
Enter your input:




CHECKING ORDER HISTORY AFTER BUYING
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Wallet Balance: Rs.31700
Enter your input:o

Step-2
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Wallet Balance: Rs.31700
Order History:
1.Order-1: Laptop qt:2 - Rs.68000, Mouse qt:1 - Rs.300, Total: Rs.68300 - status: Purchased
Enter your input:




LOGGING OUT
Step-1
MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Wallet Balance: Rs.31700
Enter your input:l

Step-2
Logged out successfully.


Onboarding screen after logging out
Welcome to MyKart Store
1. Login (l) 2. Register (r) 3. Exit (e)
Enter your input:l

Step-2
Enter your username: user1
Enter your password: pass1

Step-3
Login successful!
Welcome back to MyKart Store

MyKart Store
Manage account- Order history(o)- Logout(l)
1. Laptop-Rs.34000 2.Keyboard-Rs.800 3.Mouse-Rs.300 4.Bluetooth Speaker-Rs.1200
Your Cart
(empty)
Wallet Balance: Rs.31700
Enter your input:


Registering a new user
Step-1
Welcome to MyKart Store
1. Login (l) 2. Register (r) 3. Exit (e)
Enter your input:r

Step-2
Enter your desired username: user2
Enter your password: pass2
Enter your password again: pass2
Enter your address: Nehru Nagar, Hyderabad 500013
Enter your phone number: 9876543210

Step-3
Registration successful! You can now log in.
Welcome to MyKart Store
1. Login (l) 2. Register (r) 3. Exit (e)
Enter your input:


"""
