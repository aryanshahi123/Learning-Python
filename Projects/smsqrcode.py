import qrcode

#Create your own contact card:
name = input("Enter your name:")
phone_number = input("Enter your contact number:")
email_address = input("Enter your email address")
contact = f"MECARD:N:{name};TEL:{phone_number};EMAIL:{email_address};;;"
contact_qr = qrcode.make(contact)
contact_qr.save("AryanContact.png")