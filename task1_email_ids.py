import imaplib
import email
from email.header import decode_header


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("tusharyadavnewacc@gmail.com", "zgheuehgbfcpibaq")
mail.select("inbox")

status, messages = mail.search(None, "UNSEEN")
email_ids = messages[0].split()

print(email_ids)

for e_id in email_ids:
    status, msg_data = mail.fetch(e_id, "(RFC822)")

    msg = email.message_from_bytes(msg_data[0][1])

    subject, encoding = decode_header(msg["Subject"])[0]

    