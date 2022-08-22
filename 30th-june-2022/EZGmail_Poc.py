
import ezgmail
import pprint
ezgmail.init()
print(ezgmail.EMAIL_ADDRESS)
threads = ezgmail.search('See the attached files')
#ezgmail.send('sahoorakesh627@gmail.com','subject', 'happy birthday')
unread = ezgmail.unread()
print(unread[0].messages[0].downloadAttachment('Resume.pdf', 'Desktop'))