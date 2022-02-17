import os
import email, imaplib
from bs4 import BeautifulSoup as bs

def get_mail_client(email_address, password):
    SMTP_SERVER = 'imap.gmail.com'
    SMTP_PORT = 993
    mail = imaplib.IMAP4_SSL(SMTP_SERVER, SMTP_PORT)
    mail.login(email_address, password)
    return mail

def scrape_gmail():

    mail = get_mail_client(email_address)
    status, messages = mail.select('INBOX')
    data = []   
    links = []
    
    for i in range(0, int(messages[0])):
      res, msg = mail.fetch(str(i + 1), '(RFC822)')

      for response in msg:
          if isinstance(response, tuple):
              msg = email.message_from_bytes(response[1])
              
              if msg.is_multipart():
                  for part in msg.walk():
                      content_type = part.get_content_type()
                      content_disposition = str(part.get("Content-Disposition"))
                      
                      try:
                          body = part.get_payload(decode=True).decode()
                      except:
                          pass
                      
                      if content_type == "text/plain" and "attachment" not in content_disposition:
                          data.append(body)
              else:
                  content_type = msg.get_content_type()
                  body = msg.get_payload(decode=True).decode()
                  if content_type == "text/plain":
                      data.append(body)

              # Use BeautifulSoup if the content type is HTML        
              if content_type == 'text/html':
                  soup = bs(str(body), 'lxml')

      # Go through all links, shorten them, and add to list
      # Also add the job positions to list        
      for a in soup.find_all('a', href=True):
          if "view" in a['href']:
              links.append(a['href'].split('?')[0])
          
      # Leaves only the links that lead to the job around and remove duplicates
      links[:] = list(dict.fromkeys([x for x in links if 'view' in x]))
       
    mail.close()
    mail.logout()
    
    return links
