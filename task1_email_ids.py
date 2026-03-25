import imaplib
import email
from email.header import decode_header


mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login("tusharyadavnewacc@gmail.com", "zgheuehgbfcpibaq")
mail.select("inbox")

status, messages = mail.search(None, "UNSEEN")
email_ids = messages[0].split()

for e_id in email_ids:
    status, msg_data = mail.fetch(e_id, "(RFC822)")

    msg = email.message_from_bytes(msg_data[0][1])

    subject, encoding = decode_header(msg["Subject"])[0]

    if isinstance(subject, bytes):
        subject = subject.decode(encoding if encoding else "utf-8")
    
    sender = msg.get("From")

    print("From: ", sender)
    print("Subject: ", subject)
    print("-"*40)

    body = ""

    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode = True).decode(errors = "ignore")
                break
    else:
        body = msg.get_payload(decoode=True).decode(errors = "ignore")
    
    print("Body: ", body[:200])
    print("="*50)