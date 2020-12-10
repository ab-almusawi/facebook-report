import os
import json
import requests.cookies
from requests.utils import dict_from_cookiejar

PROTECTED_URL = 'https://m.facebook.com/groups/318395378171876?view=members'
LOGIN_URL = 'https://m.facebook.com/login.php'
FB_URL = 'https://m.facebook.com'


def Login2Fb(lo):
    Response = session.get(FB_URL)
    rsc = Response.cookies
    session.cookies = rsc
    response = session.post(LOGIN_URL, cookies=rsc, data={
        'email': raw_input("Enter Id/Email/PhoneNumber: "),
        'pass': raw_input("Enter Password: ")
    }, allow_redirects=False)
    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:
        Save_Cookie(lo)
        return True
    else:
        print("Invalid Email Or Password !")
        lo += 1
        Login2Fb(i)


def Save_Cookie(c):
    try:
        os.mkdir('cookies')
    except OSError:
        pass
    with open('cookies/{}.txt'.format(c), 'w') as f:
        json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
    print("[ Cookies {} Saved ]".format(c))


print('''
                Programmed By Hameed Almusawi
           ------------- ------------- -------------
                  Instagram : ab_almusawi1

         ''')
session = requests.session()
Accounts_N = int(input("Enter Number Of Accounts To Use : "))
i = 1
for i in range(Accounts_N):
    Login2Fb(i)
print(session.cookies)

