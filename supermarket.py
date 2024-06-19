import datetime


print("welcome to  more supermarket")
print("have a nice day sir\madam")
print("flore->\n  shirt->300 \n   saree ->150\n  pants->500\n medicans->2\n food-> 3 \n jewells->4\n")
username="arjun"	
password="4747"

one_shirt=300
one_saree=150
one_pants=500
medicans=2
food=3
jewells=4


if username=="":
     print("pls enter your username")
if password=="":
     print("pls enter your password")

if username=="arjun" and password=="4747":
      print("login successfull pls enter ")
else:
     print("invaid username or password")
                       
flore=["shirt","saree","pants","medicans","food","jewells"]
your_order=input("enter your_order :")
     
if your_order in flore :
    print(f"yes!..(your_order)is available")
    how_many=int(input(f"how_many{"shirt","saree","pants"}you want_or_which_flore:"))

    if your_order=="shirt":
        total=one_shirt*how_many
        if total>=1000:
            offer_total=total-100
            print(f"you ordered more than 1000 yupees so your total is {offer_total}")
        else:
                print(f"your ordered (how_many) {your_order }so , your total bill is {total}")
    elif your_order== "saree":
         total= one_saree*how_many
         if total>=1000:
              offer_total=total-150
              print(f"(you ordered more than 1000 rupees so your total is {offer_total})")
         else:
              print(f"you ordered {how_many}{your_order}so, your total bill is {total}") 
    elif your_order=="pants":
          total=one_pants*how_many
          if total>=1000:
               offer_total=total-130
               print(f"you ordered more than 1000 rupwwa ao your offer_total bill is {offer_total}")
               
               
          else:
               print(f"you ordered{how_many}{your_order}so, your total bill is {total}")
    elif your_order=="food":
         print(f"you go to the 3 flore")
         
    elif your_order=="medicans":
         print("if you go to the 2 flore")
    elif your_order=="jewells":
         print(f"you want it you will go to fourth flore")
else:
     print(f"sorry  {your_order}is on another branch,stok is not available right now")
print(f"thank you sir\madam pls come again")

x=datetime.datetime.now()
current_say=x.strftime("%A")
y=x.strftime("%B")

print(y)
price=float(input("enter the price{total}:"))
gst=14
cgst=price*((gst/2)/100)
sgst=cgst
total=price +gst+cgst
               
               
print("price:",price)
print("cgst:",cgst)
               
print("total amount:",total)


             
