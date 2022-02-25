import imaplib
import email
from email.header import decode_header

imap_host = 'imap.gmail.com'
imap_username = 'username123@sample.com'
imap_password = 'P@assW0Rd!123'

# Connect to host using SSL
imap = imaplib.IMAP4_SSL('imap.gmail.com', 993)

# Login to server
imap.login(imap_username, imap_password)

imap.select('"[Gmail]/All Mail"')

status, messages = imap.search(None, 'FROM "sample-senderemail@sampleemail.com"')

messages = messages[0].split(b' ')

# Fetches parts of email message and decodes
for mail in messages:
    _, emailmsg = imap.fetch(mail, "(RFC822)")
    for response in emailmsg:
        if isinstance(response, tuple):
            emailmsg = email.message_from_bytes(response[1])
            # Decodes the email subject
            subject = decode_header(emailmsg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # If subject is in bytes, decodes to a string
                subject = subject.decode()

            # Prints "Deleting + (subject of the e-mail)"
            print("Deleting", subject)
    # Moves e-mail to Trash folder
    imap.store(mail, '+X-GM-LABELS', '\\Trash')


# Permanently removes e-mails labeled as "Trash" from selected mailbox
imap.expunge()

# Closes selected mailbox
imap.close()

# Shuts down connection to the server
imap.logout()