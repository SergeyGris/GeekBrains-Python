import re


def email_parse(email):
    pattern = re.compile(r'(?P<username>\w*?[._+-]*?\w*?)(?:@)(?P<domain>[a-zA-Z.-0-7]+?\.[a-zA-Z]{2,})')
    rez = pattern.search(email)
    rez_dict = rez.groupdict()
    if rez.group('username') == '':
        raise ValueError
    print(rez_dict)


email_lst = ['svg95@list.ru', 'mamba-74@gugu7.com', 'my_mail@gmail.com', '1995@mail.com',
             'asfasgdav12313-@mail-77.ru', 'abra&kadara?@gmail.com']
for email in email_lst:
    try:
        email_parse(email)
    except ValueError:
        print(f'wrong email: {email}')
