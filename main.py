import smtplib as s

def get_recipient_name(email_address):
    if email_address == "RECIPIENT1ID":
        recipient_name = "Name1"
    elif email_address == "RECIPIENT2ID":
        recipient_name = "Name2"
    else:
        recipient_name = "Name3"
    
    return recipient_name

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('SENDERID', 'PASSWORD')

subject = "Fantastic response to our Game!"
body = """\
We are thrilled to announce that our game, THE LOST MYSTIC ORNAMENT,
has been a huge success with around 48k downloads on Playstore.
We are deeply grateful to you for playing it. We kindly request you
to take a moment to rate and review this game on Playstore
to help us grow even more. Your feedback means a lot to us.
Thank you for being part of our gaming journey!

Yours friendly,
Ahmad
Developer MACHAU Games
"""

listadd = ['RECIPIENT1ID', 'RECIPIENT2ID', "RECIPIENT3ID"]

for recipient_email in listadd:
    recipient_name = get_recipient_name(recipient_email)
    message = f"subject: {subject}\n\nHi {recipient_name}!,\n\n{body}"
    ob.sendmail('SENDERID', recipient_email, message)

print("Mail sent successfully.")
ob.quit()