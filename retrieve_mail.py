import imapclient
import pprint
import imaplib
imaplib._MAXLINE=10000000
imapObj=imapclient.IMAPClient('imap.gmail.com',ssl=True)
usr_name=raw_input('enter ur gmail address:')
passwd=raw_input('enter passwd for this account:')
imapObj.login(usr_name,passwd)
pprint.pprint(imapObj.list_folders)
imapObj.select_folder('INBOX',readonly=True)
UIDs=imapObj.search(['SINCE 22-Jul-2016'])
rawMessg=imapObj.fetch(UIDs,['BODY[]'])
pprint.pprint(rawMessg)
imapObj.logout()
