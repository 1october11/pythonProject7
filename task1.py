import re


def email_parse(email_adress):
    RE_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&])+\.\w+)', re.IGNORECASE)
    if not RE_email.match(email_adress):
        raise ValueError(f'wrong email:{email_adress}')
    print(RE_email.match(email_adress).groupdict())


try:
    email_parse('sashaoktbr@yandex.ru')
except ValueError as err:
    print(err)