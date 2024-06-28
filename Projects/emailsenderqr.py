import qrcode


email_address = input("Enter receipient:")
subject = input("Enter Subject:")
body = input("Enter body:")

mail = f"mailto:{email_address}?subject={subject}&body={body}"

mailqr = qrcode.make(mail)
mailqr.save("SendEmail.png")