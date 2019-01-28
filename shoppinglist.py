#The smtplib module defines an SMTP client session object
# that can be used to send mail to any Internet machine with an daemon
import smtplib

# EmailMessage provides the core functionality for setting and querying header fields
# For accessing message bodies, and for creating or modifying structured messages.
from email.message import EmailMessage

#The getpass module provides a portable way to handle password prompts from terminal securely.
from getpass import getpass

#Declarations
name = ""
GMAIL_USERNAME = ""
GMAIL_PASSWORD = ""
recipient = ""
quantities = []
products = []


def get_details():
    global GMAIL_PASSWORD,GMAIL_USERNAME,recipient
    # Accept Sender and Recipient details
    name = str(input("Name:   "))
    GMAIL_USERNAME = str(input("Email:  "))
    GMAIL_PASSWORD = str(input("Password:   "))
    recipient = str(input("Recipient"))


def accept_list():
    global products, quantities
    # To accept Number of Products to be added in List from user
    while True:
        try:
            n = int(input(f"Hello {name}, How many products do you want to add to the shopping cart?"))
        except ValueError:
            print("Please enter a number")
        else:
            break

    # Lists to store products and their quantities
    # Could have used a dictionary too

    # Accept Product name and Quantity
    for x in range(n):  #n is local variable
        product = str(input("Enter the product name:"))
        while True:
            try:
                quantity = int(input('Enter the quantity of {product}'))
            except ValueError:
                print('Please enter a number')
            else:
                break

        # Append Product and its Quantity for every iteration
        products.append(product)
        quantities.append(quantity)

    print('These products have been added to the list:')


def display():
    global products, quantities
    #Just print out what the user entered
    #The purpose of zip() is to map the similar index of multiple containers
    #So that they can be used just using as single entity.
    for x,y in zip(products, quantities):
        print(f"{x} x {y}")


def send():
    global GMAIL_USERNAME,GMAIL_PASSWORD,recipient,products,quantities
    # Create the container email message.
    message=EmailMessage()
    message['Subject']="Shopping List"
    message['From']="Kshitij Vengurlekar"
    message['To']=recipient
    # m is the multiline string which will be sent in Email Body
    m = ""

    # Generate m from user inbo
    for i in range(len(products)):
        m=m+str(products[i])+" x "+str(quantities[i])+"\n"

    message.set_content(m)

    try:
        a = smtplib.SMTP_SSL(  'smtp.gmail.com', 465)
        a.ehlo()
        a.login(GMAIL_USERNAME,GMAIL_PASSWORD)
        a.send_message(message)
        a.quit()
    except:
        print("Error")
    else:
        print("Email has been Sent")

get_details()
accept_list()
display()
send()
print("Thank You")

exit()
