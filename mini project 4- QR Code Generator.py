''' QR Code Generator'''
'''Using Python we'll genertae a QR code.You can just scan the QR code and money will be sent to the bank associated with
 the QR Code.You can use any payment apps like phonepay,google pay,paytm etc.'''

# Install qrcode package    - to generate the qr code
# Install pillow package    - to show the qr code

'''Step 1: Take upi id as an input from the user.  (Ex: userupi123@okbankname)
   Step 2: Payment URL is defined for each payment apps that we use.  (Ex: url for phonepay,url for gpay)
   Step 3: Particular qr codes will be generated for each payment apps.
   Step 4: The generated QR codes will be saved in our device in image format.
   Step 5: Display the QR code using Pillow Viewer.'''


# url format for payment apps
#  upi://pay?pa=payee_address&pn=payee_name&am=amount&cu=currency&[optional_parameters].
''' pa- Payees virtual payment address- upi id
    pn- Payees name
    am= amount you want to pay.If you don't want to mention it then skip.
    cu- currency type ,like it'll be INR for phonepay,gpay etc.But for paypal it'll be in dollars. So if want to specify them then do that.
    optional parameters:
    mc-merchant category code
    tid- transaction id'''

import qrcode

#  give your genuine upi id.
upi_id=input("Enter your UPI ID:")

# Defining the payment url based on payment apps. Pyment urls will be diff for each payment apps.
# You can modify these urls based on the payment apps you want to support.

# %20 means a space within a string. + operator can also be used to add space.
# Three different types you can use to add the receiepient name.It will be shown in the payment page.

phonepe_url=f"upi://pay?pa={upi_id}&pn=Ravina+UN&mc=1234"
googlepay_url=f"upi://pay?pa={upi_id}&pn=Ravina%20U%20N&mc=1234"
bhimupi_url=f"upi://pay?pa={upi_id}&pn=Reciepient%20Name&mc=1234"

# Create qr code for each payment apps

phonepay_qr=qrcode.make(phonepe_url)
googlepay_qr=qrcode.make(googlepay_url)
bhimupi_qr=qrcode.make(bhimupi_url)


# Saave these image files

phonepay_qr.save("phonepay_qr.png")
googlepay_qr.save("googlepay_qr.png")
bhimupi_qr.save("bhimupi_qr.png")


# Display the qr codes

phonepay_qr.show()
googlepay_qr.show()
bhimupi_qr.show()



