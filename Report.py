import os
import random
import re
import json
import time
import requests.cookies
from pathlib import Path
from requests.utils import dict_from_cookiejar


def GET_REPORT_URL(u_id, r_type):
    Rtype = ''
    URL_TO_REPORT_FAKE_ACCOUNT = 'https://mbasic.facebook.com/rapid_report/basic/actions/?context=%7B%22session_id%22%3A%22108949e4-d352-4c4f-b75c-4c0e9b7b6d89%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22frx_report_action%22%3A%22NO_REPORT%22%2C%22rapid_reporting_tags%22%3A%5B%22profile_fake_name%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22frx_feedback_submitted%22%3Atrue%2C%22reportable_ent_token%22%3A%22{}%22%7D&action_key=REPORT_CONTENT'.format(
        u_id)
    URL_TO_REPORT_FAKE_NAME = 'https://mbasic.facebook.com/cix/screen/basic/frx_confirmation_screen/?state=%7B%22session_id%22%3A%2252dd2e49-8d8c-42b1-a041-2863cbefb0a5%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22rapid_reporting_tags%22%3A%5B%22profile_fake_name%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22reportable_ent_token%22%3A%22{}%22%7D'.format(
        u_id)
    URL_TO_REPORT_Inappropriate_Things = 'https://mbasic.facebook.com/cix/screen/basic/frx_confirmation_screen/?state=%7B%22session_id%22%3A%2252dd2e49-8d8c-42b1-a041-2863cbefb0a5%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22rapid_reporting_tags%22%3A%5B%22profile_posting_inappropriate_things%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22reportable_ent_token%22%3A%22{}%22%7D'.format(
        u_id)
    URL_TO_REPORT_HARASSMENT = 'https://mbasic.facebook.com/cix/screen/basic/frx_confirmation_screen/?state=%7B%22session_id%22%3A%2252dd2e49-8d8c-42b1-a041-2863cbefb0a5%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22rapid_reporting_tags%22%3A%5B%22harassment_or_bullying%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM%22%2C%22reportable_ent_token%22%3A%22{}%22%7D'.format(
        u_id)
    URL_TO_REPORT_PRETEND_ME = 'https://mbasic.facebook.com/cix/screen/basic/frx_confirmation_screen/?state=%7B%22session_id%22%3A%2252dd2e49-8d8c-42b1-a041-2863cbefb0a5%22%2C%22support_type%22%3A%22frx%22%2C%22type%22%3A2%2C%22initial_action_name%22%3A%22RESOLVE_PROBLEM%22%2C%22story_location%22%3A%22profile_someone_else%22%2C%22entry_point%22%3A%22profile_report_button%22%2C%22reporting_ufo_key%22%3A%22ufo-a96aefca-5082-4a1e-a050-6e4b40bc932c%22%2C%22frx_report_action%22%3A%22REPORT_WITH_CONFIRMATION%22%2C%22rapid_reporting_tags%22%3A%5B%22profile_impersonation%22%2C%22profile_impersonation_me%22%5D%2C%22actions_taken%22%3A%22RESOLVE_PROBLEM.REPORT_CONTENT%22%2C%22frx_feedback_submitted%22%3Atrue%2C%22reportable_ent_token%22%3A%22{}%22%7D'.format(
        u_id)
    if r_type == 1:
        Rtype = URL_TO_REPORT_FAKE_ACCOUNT
    elif r_type == 2:
        Rtype = URL_TO_REPORT_FAKE_NAME
    elif r_type == 3:
        Rtype = URL_TO_REPORT_Inappropriate_Things
    elif r_type == 4:
        Rtype = URL_TO_REPORT_HARASSMENT
    elif r_type == 5:
        Rtype = URL_TO_REPORT_PRETEND_ME
    else:
        print('Invalid Entry !')
    return Rtype


def report(uid, report_t, t, use_p, count):
    global rProxy, c_user
    session.headers = ("Cookie", Get_Cookie(count))
    if use_p.lower() == 'y':
        try:
            r = session.get(GET_REPORT_URL(uid, report_t),
                            allow_redirects=True)
            if 'fb_dtsg' in r.content:
                print("Report {} : Ok".format(count))
                lines = open('proxies.txt', 'r').read().splitlines()
                line = random.choice(lines)
                rProxy = line.strip()
                proxies = {'http': '{}'.format(rProxy),
                           'https': '{}'.format(rProxy)}
                session.proxies = proxies
                print("Now Lets Report With Proxy ->" + '[ {} ]'.format(rProxy))
                time.sleep(float(t))
            else:
                print("Report --> Fail --> Cookies --> Number : ".format(count))
                try:
                    os.mkdir('DAccounts')
                except OSError:
                    pass
                b = open('DAccounts/diedCookies.txt', 'w')
                b.write('{}'.format(count) + '\n')
                b.close()
        except requests.ConnectionError:
            print('Check Your Connection! -> Proxy Connection Fail -> [ {} ]'.format(rProxy))
            try:
                out = open('Died_Proxies.txt', 'a')
                out.write('Died Proxy : ' + rProxy + '\n')
                out.close()
                with open("proxies.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for x in d:
                        if x != "{}".format(rProxy):
                            f.write(x)
                    f.truncate()
                f.close()
            except KeyError:
                pass
            pass
    else:
        try:
            r = session.get(GET_REPORT_URL(uid, report_t),
                            allow_redirects=True)
            if 'fb_dtsg' in r.content:
                print("Report {} : Ok".format(count))
                time.sleep(float(t))
            else:
                print("Report --> Fail --> Cookies --> Number : ".format(count))
                try:
                    os.mkdir('DAccounts')
                except OSError:
                    pass
                b = open('DAccounts/diedCookies.txt', 'w')
                b.write('{}'.format(count) + '\n')
                b.close()
        except requests.ConnectionError:
            print('Check Your Connection!')
            pass


def Find_Uid(url_to_report):
    f = re.compile('"entity_id":"([0-9]+)"')
    session.headers = ("Cookie", Get_Cookie(1))
    page = session.get(url_to_report)
    return f.findall(page.content.decode())


def Get_Cookie(c):
    my_cookie = Path('cookies/{}.txt'.format(c))
    if my_cookie.is_file():
        with open('cookies/{}.txt'.format(c), 'r') as f:
            cookies = requests.utils.cookiejar_from_dict(json.load(f))
            session.cookies.update(cookies)
    else:
        print('Cookies File Not Found')


session = requests.session()
print('''
                Programmed By Hameed Almusawi
           ------------- ------------- -------------
                  Instagram : ab_almusawi1
          
         ''')
id_TO_REPORT = input("Enter ID Of Account TO Report: ")
print('''
              COMMAND               DESCRIPTION
           -------------       -----------------------------

            1                     REPORT_FAKE_ACCOUNT
            2                     REPORT_FAKE_NAME
            3                     REPORT_INAPPROPRIATE_THINGS
            4                     REPORT_HARASSMENT
            5                     REPORT_PRETEND_ME
         ''')
report_type = raw_input("Enter Report Type By Using Numbers  : ")
report_count = raw_input("Enter How Many Reports You Want? ReportsNum = CookiesNum : ")
Time_To_Sleep = raw_input("Enter Time(Seconds) To Sleep Between Reports : ")
use_p = raw_input('Do You Want To Use Proxies ? Y/n : ')
i = 0
for i in range(int(report_count)):
    report(id_TO_REPORT, int(report_type), int(Time_To_Sleep), use_p, i)
